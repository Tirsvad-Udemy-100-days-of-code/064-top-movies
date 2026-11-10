"""!
@file capture.py
@brief Capture named screenshots of a running web page with a headless browser.

Runs inside the Docker image of this folder, never on the host desktop.
Usage: python capture.py BASE_URL OUT_DIR name=/path [name=/path ...]
"""

import logging
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

## Logger of this tool.
LOG = logging.getLogger("capture")

## Browser window size used for every screenshot.
VIEWPORT = {"width": 1100, "height": 800}


def capture(base_url: str, out_dir: Path, targets: dict[str, str]) -> list[Path]:
    """!
    @brief Open each path in headless Chromium and save a full-page PNG.
    @param base_url Address of the running application, without a trailing slash.
    @param out_dir Folder that receives the PNG files.
    @param targets Map of file stem to URL path.
    @return The files written.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for name, path in targets.items():
            page.goto(base_url.rstrip("/") + path, wait_until="networkidle")
            target = out_dir / f"{name}.png"
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
    if len(argv) < 3 or any("=" not in item for item in argv[2:]):
        LOG.error("%s", __doc__)
        return 2
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    targets = dict(item.split("=", 1) for item in argv[2:])
    for file in capture(argv[0], Path(argv[1]), targets):
        LOG.info("wrote %s", file)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
