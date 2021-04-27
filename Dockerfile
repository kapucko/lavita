FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

ENV BUILD_DEPS="build-essential curl"

COPY requirements.txt /app/
RUN apt update && apt install -y $BUILD_DEPS && \
    pip install --no-cache-dir -r requirements.txt && \
    apt -y autoremove && apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/cache/* /var/lib/apt/lists/*


COPY . /app
ARG package_version
ENV PACKAGE_VERSION=$package_version

USER nobody
