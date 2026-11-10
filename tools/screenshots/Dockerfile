# Headless browser image that serves the demo app and captures screenshots.
# Nothing here touches the host desktop (framework/process/gui-testing.md).
FROM python:3.13-slim
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PLAYWRIGHT_BROWSERS_PATH=/opt/pw
RUN apt-get update \
    && apt-get install -y --no-install-recommends libatomic1 \
    && pip install --no-cache-dir playwright \
    && python -m playwright install --with-deps chromium \
    && chmod -R a+rX /opt/pw \
    && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home shot
COPY entrypoint.sh /entrypoint.sh
COPY capture.py /opt/capture.py
RUN chmod +x /entrypoint.sh
USER shot
WORKDIR /home/shot
ENTRYPOINT ["/entrypoint.sh"]
