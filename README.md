# ⌬ 𝐇𝐞𝐦𝐚𝐧𝐭𝐡 𝐁𝐨𝐭 (𝐖𝐙𝐌𝐋-𝐗)

This is a powerful, feature-rich Telegram bot that allows users to mirror and leech files from various sources (Direct Links, Torrents, NZB, etc.) to Cloud Drives (Google Drive, Rclone supported clouds) or Telegram.

---

## 🚀 Step-by-Step VPS Deployment Guide

Follow these exact steps to deploy the bot on your Ubuntu/Debian VPS.

### 1. Update your VPS
First, make sure your system is up to date:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Git and Essential Tools
```bash
sudo apt install git wget nano -y
```

### 3. Install Docker and Docker Compose
Run the following commands to install Docker and Docker Compose automatically:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
Check if Docker is installed:
```bash
docker --version
```

### 4. Clone the Repository
Replace `YourGitHubUsername` with your actual username if you've forked this:
```bash
git clone https://github.com/Hemanth/HemanthBot mirrorbot && cd mirrorbot
```

### 5. Setup Configuration
Copy the sample configuration file:
```bash
cp config_sample.py config.py
```
Open it with nano:
```bash
nano config.py
```
**Mandatory Variables to Fill:**
- `BOT_TOKEN`: Your Telegram Bot Token from [@BotFather](http://t.me/BotFather)
- `OWNER_ID`: Your Telegram User ID from [@MissRose_bot](http://t.me/MissRose_bot) (type /id)
- `TELEGRAM_API`: Your Telegram API ID from [my.telegram.org](https://my.telegram.org)
- `TELEGRAM_HASH`: Your Telegram API Hash from [my.telegram.org](https://my.telegram.org)

*Press `CTRL+O`, `Enter`, and `CTRL+X` to save and exit nano.*

### 6. Build and Deploy
Now, start the bot using Docker Compose. This will download everything and start the bot in the background:
```bash
sudo docker-compose up -d --build
```

### 7. Managing the Bot
- **View Logs:** `sudo docker-compose logs -f`
- **Restart Bot:** `sudo docker-compose restart`
- **Stop Bot:** `sudo docker-compose stop`
- **Rebuild (after editing config):** `sudo docker-compose up -d --build`

---

## 🏅 Credits & Support
- **Owner/Dev:** [Hemanth](http://t.me/ALONEKINGSTAR77)
- **Telegram Username:** [@alonekingstar77](http://t.me/ALONEKINGSTAR77)
- **Support Group:** [Join Here](http://t.me/ALONEKINGSTAR77)

---
*Powered by Hemanth*
