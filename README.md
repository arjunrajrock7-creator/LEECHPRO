<p align="center">
  <img src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="HemanthBot Logo" width="250">
</p>

<h1 align="center">⌬ 𝐇𝐞𝐦𝐚𝐧𝐭𝐡 𝐁𝐨𝐭 (𝐖𝐙𝐌𝐋-𝐗)</h1>

<p align="center">
  <i>The Ultimate Mirror & Leech Solution for Telegram. Built for speed, efficiency, and power.</i>
</p>

<p align="center">
  <a href="http://t.me/ALONEKINGSTAR77">
    <img src="https://img.shields.io/badge/Telegram-Channel-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Channel">
  </a>
  <a href="http://t.me/ALONEKINGSTAR77">
    <img src="https://img.shields.io/badge/Support-Group-orange?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  </a>
</p>

---

## 💎 Exclusive Features

| Feature | Description |
| :--- | :--- |
| **🚀 Hybrid Leech** | Uses both Bot and User sessions to maximize upload speeds and bypass limits. |
| **📦 Zip Pipeline** | Automated DOWNLOAD ➜ EXTRACT ➜ MERGE ➜ UPLOAD flow for massive convenience. |
| **🎬 Episode Merge** | Intelligent detection and lossless merging of episodic video files. |
| **☁️ Multi-Cloud** | Native support for Google Drive, Rclone, and Telegram Leeching. |
| **🛠 Metadata Engine** | Inject custom titles, authors, and years directly into your media files. |
| **📱 Premium UI** | Clean, attractive status messages with stylish Unicode fonts. |

---

## 📜 Bot Commands Index

### 📤 Mirroring & Leeching
| Command | Alias | Description |
| :--- | :--- | :--- |
| `/mirror` | `/m` | Mirror any link/file to your configured cloud storage. |
| `/leech` | `/l` | Leech any link/file directly to Telegram. |
| `/zipmerge` | `/zm` | Run the automated Zip Pipeline (Extract + Merge). |
| `/qbmirror` | `/qm` | Mirror torrents via qBittorrent. |
| `/qbleech` | `/ql` | Leech torrents via qBittorrent. |
| `/ytdl` | `/y` | Download from YouTube and other social media via yt-dlp. |
| `/ytdlleech` | `/yl` | Leech from social media directly to Telegram. |

### 🛠 Tools & Management
| Command | Description |
| :--- | :--- |
| `/status` | Monitor real-time progress of all active tasks. |
| `/cancel` | Stop a specific task by its GID or by replying to it. |
| `/search` | Search for torrents using integrated API plugins. |
| `/list` | Browse and search files within your Google Drive. |
| `/mediainfo` | Get technical details (codec, bitrate, etc.) of a file. |
| `/userset` | Personalize your experience (Thumbnails, Metadata, Flags). |
| `/stats` | View system resource usage and bot statistics. |

---

## 🚀 Pro VPS Deployment Guide

### 🛠 Prerequisites
Ensure you have a VPS running **Ubuntu 22.04+** or **Debian 11+**.

### 1️⃣ Prepare Environment
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git wget nano python3 python3-pip -y
```

### 2️⃣ Install Docker & Compose
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 3️⃣ Setup the Bot
```bash
git clone https://github.com/Hemanth/HemanthBot mirrorbot
cd mirrorbot
cp config_sample.py config.py
nano config.py
```
> **Note:** Fill in your `BOT_TOKEN`, `OWNER_ID`, `API_ID`, `API_HASH`, and `DATABASE_URL`.

### 4️⃣ Fire It Up!
```bash
sudo docker-compose up -d --build
```

---

## 🛠 Advanced Management

| Action | Command |
| :--- | :--- |
| **Live Logs** | `sudo docker-compose logs -f` |
| **Safe Stop** | `sudo docker-compose stop` |
| **Quick Restart** | `sudo docker-compose restart` |
| **Apply Updates** | `git pull && sudo docker-compose up -d --build` |

---

## 🏅 Credits & Support

- **Visionary:** [Hemanth](http://t.me/ALONEKINGSTAR77)
- **Dev Team:** [@alonekingstar77](http://t.me/ALONEKINGSTAR77)
- **Official Channel:** [Hemanth Updates](http://t.me/ALONEKINGSTAR77)

<p align="center">
  <b>© 2025 HemanthBot. All Rights Reserved.</b>
</p>
