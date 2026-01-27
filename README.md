# ⌬ 𝐇𝐞𝐦𝐚𝐧𝐭𝐡 𝐖𝐙𝐌𝐋-𝐗

This is a powerful Telegram bot that can mirror/leech files from various sources to Cloud Drives or Telegram.

## 📌 Features
- Mirror/Leech from links, telegram files, torrents, nzb, rclone-cloud.
- Upload to rclone cloud, Google Drive or Telegram.
- Highly customizable and feature-rich.

---

## 🚀 VPS Deployment Guide

### 1. Prerequisites
Before you begin, ensure you have the following installed on your VPS:
- **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
- **Git**: `sudo apt install git -y`

### 2. Installation
Clone this repository and navigate into the directory:
```bash
git clone https://github.com/Hemanth/HemanthBot mirrorbot && cd mirrorbot
```

### 3. Configuration
Copy the sample config file and edit it with your credentials:
```bash
cp config_sample.py config.py
# Use nano or any other editor to fill in the required variables
nano config.py
```

### 4. Build and Run
You can easily build and run the bot using Docker Compose:
```bash
# Build and start the containers in detached mode
sudo docker-compose up -d --build
```

To view logs:
```bash
sudo docker-compose logs -f
```

To stop the bot:
```bash
sudo docker-compose stop
```

---

## 🏅 Credits & Support
- **Owner/Dev:** [Hemanth](http://t.me/ALONEKINGSTAR77)
- **Telegram Username:** [@alonekingstar77](http://t.me/ALONEKINGSTAR77)
- **Telegram Channel:** [Join Here](http://t.me/ALONEKINGSTAR77)

---
*Powered by Hemanth*
