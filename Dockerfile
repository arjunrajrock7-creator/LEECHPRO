FROM python:3.10-slim-buster

# Set working directory
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Install system dependencies
# Including:
# - git, curl, jq: standard utilities
# - aria2, ffmpeg, rclone: download and processing tools
# - qbittorrent-nox, sabnzbdplus: torrent and usenet clients
# - default-jre: required for JDownloader
# - libmagic1: required for python-magic
# - cpulimit: used in setpkgs.sh
RUN apt-get update && apt-get install -y \
    curl git aria2 ffmpeg rclone qbittorrent-nox sabnzbdplus \
    default-jre libmagic1 cpulimit \
    libavformat-dev libavcodec-dev libavdevice-dev \
    libavfilter-dev libavutil-dev libswresample-dev \
    libswscale-dev libpostproc-dev \
    gcc g++ make python3-dev jq \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for HT-BOTZ-X custom binary names
RUN ln -s /usr/bin/aria2c /usr/bin/blitzfetcher && \
    ln -s /usr/bin/qbittorrent-nox /usr/bin/stormtorrent && \
    ln -s /usr/bin/ffmpeg /usr/bin/mediaforge && \
    ln -s /usr/bin/rclone /usr/bin/ghostdrive && \
    ln -s /usr/bin/sabnzbdplus /usr/bin/newsripper

# Install uv for faster package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Copy and install requirements
COPY requirements.txt .
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make scripts executable
RUN chmod +x start.sh setpkgs.sh

# Entry point
CMD ["bash", "start.sh"]
