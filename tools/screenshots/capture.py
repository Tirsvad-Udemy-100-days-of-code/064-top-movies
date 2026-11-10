"""!
@file capture.py
@brief Capture named screenshots of a running web page with a headless browser.

Runs inside the Docker image of this folder, never on the host desktop.
Usage: python capture.py BASE_URL OUT_DIR TARGET [TARGET ...]

A TARGET is `name=/path`, optionally followed by steps separated by `>`:

    name=/path>fill:SELECTOR=VALUE>click:SELECTOR

The page at /path is opened, the steps run in order, and the page is then saved as name.png.
`fill:SELECTOR=VALUE` types VALUE into the field SELECTOR (the selector must not contain `=`).
`click:SELECTOR` clicks the element and waits for the page to settle; the selector is any
Playwright selector, such as `#submit` or `text=The Matrix Reloaded`. Neither a selector nor
a value may contain `>`.
Example: `r4-select=/add>fill:#title=The Matrix>click:#submit`
"""

import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

## Logger of this tool.
LOG = logging.getLogger("capture")

## Browser window size used for every screenshot.
VIEWPORT = {"width": 1100, "height": 800}

## Separator between the path of a target and its steps, and between steps.
STEP_SEPARATOR = ">"

## Step that types a value into a field.
ACTION_FILL = "fill"

## Step that clicks an element.
ACTION_CLICK = "click"


@dataclass(frozen=True, slots=True)
class Step:
    """!
    @brief One browser action to run before the screenshot.
    """

    ## Either ACTION_FILL or ACTION_CLICK.
    action: str
    ## Playwright selector of the element.
    selector: str
    ## Text to type; empty for a click.
    value: str = ""


@dataclass(frozen=True, slots=True)
class Target:
    """!
    @brief One screenshot to take.
    """

    ## File stem of the PNG.
    name: str
    ## URL path to open first.
    path: str
    ## Actions to run after the page is open.
    steps: tuple[Step, ...] = ()


def parse_step(text: str) -> Step:
    """!
    @brief Parse `fill:SELECTOR=VALUE` or `click:SELECTOR`.
    @param text The step as written on the command line.
    @return The step.
    @throws ValueError When the step is not in one of the two forms.
    """
    action, separator, rest = text.partition(":")
    if separator and action == ACTION_CLICK and rest:
        return Step(ACTION_CLICK, rest)
    if separator and action == ACTION_FILL:
        selector, equals, value = rest.partition("=")
        if equals and selector:
            return Step(ACTION_FILL, selector, value)
    raise ValueError(f"bad step {text!r}: use fill:SELECTOR=VALUE or click:SELECTOR")


def parse_target(text: str) -> Target:
    """!
    @brief Parse `name=/path` with optional `>step` parts.
    @param text The target as written on the command line.
    @return The target.
    @throws ValueError When the target or one of its steps is malformed.
    """
    head, *step_texts = text.split(STEP_SEPARATOR)
    name, equals, path = head.partition("=")
    if not equals or not name or not path.startswith("/"):
        raise ValueError(f"bad target {text!r}: use name=/path[>step...]")
    return Target(name, path, tuple(parse_step(step) for step in step_texts))


def run_step(page: Page, step: Step) -> None:
    """!
    @brief Run one step in the browser.
    @param page The open page.
    @param step The step to run.
    """
    if step.action == ACTION_FILL:
        page.fill(step.selector, step.value)
    else:
        page.click(step.selector)
        page.wait_for_load_state("networkidle")


def capture(base_url: str, out_dir: Path, targets: list[Target]) -> list[Path]:
    """!
    @brief Open each target in headless Chromium, run its steps and save a full-page PNG.
    @param base_url Address of the running application, without a trailing slash.
    @param out_dir Folder that receives the PNG files.
    @param targets The screenshots to take.
    @return The files written.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for item in targets:
            page.goto(base_url.rstrip("/") + item.path, wait_until="networkidle")
            for step in item.steps:
                run_step(page, step)
            target = out_dir / f"{item.name}.png"
            page.screenshot(path=str(target), full_page=True)
            written.append(target)
        browser.close()
    return written


def main(argv: list[str]) -> int:
    """!
    @brief Command line entry point.
    @param argv Arguments after the program name.
    @return Exit code, 0 on success and 2 on a usage error.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if len(argv) < 3:
        LOG.error("%s", __doc__)
        return 2
    try:
        targets = [parse_target(item) for item in argv[2:]]
    except ValueError as error:
        LOG.error("%s", error)
        return 2
    for file in capture(argv[0], Path(argv[1]), targets):
        LOG.info("wrote %s", file)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
