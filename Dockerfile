FROM python:3.10-slim-buster

# Set working directory
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl git aria2 ffmpeg rclone \
    libavformat-dev libavcodec-dev libavdevice-dev \
    libavfilter-dev libavutil-dev libswresample-dev \
    libswscale-dev libpostproc-dev \
    gcc g++ make python3-dev jq \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster package management (optional but recommended for WZML-X)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Copy and install requirements
COPY requirements.txt .
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make scripts executable
RUN chmod +x start.sh

# Entry point
CMD ["bash", "start.sh"]
