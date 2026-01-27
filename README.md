<p align="center">
  <img src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="HemanthBot Logo" width="200">
</p>

<h1 align="center">⌬ 𝐇𝐞𝐦𝐚𝐧𝐭𝐡 𝐁𝐨𝐭 (𝐖𝐙𝐌𝐋-𝐗)</h1>

<p align="center">
  <i>A powerful, feature-rich Telegram Mirror & Leech bot based on the wzv3 branch.</i>
</p>

<p align="center">
  <a href="http://t.me/ALONEKINGSTAR77">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" alt="Telegram Channel">
  </a>
  <a href="http://t.me/ALONEKINGSTAR77">
    <img src="https://img.shields.io/badge/Support-Group-orange?style=for-the-badge&logo=telegram" alt="Support Group">
  </a>
</p>

---

## 🌟 Key Features

- **🚀 Multiple Sources:** Mirror/Leech from Direct Links, Torrents, NZB, YouTube-DLP, and Rclone paths.
- **☁️ Cloud Support:** Upload to Google Drive, Rclone-supported clouds, or directly to Telegram.
- **📦 Zip Pipeline:** Automated DOWNLOAD ➜ EXTRACT ➜ MERGE ➜ UPLOAD workflow via `/zipmerge`.
- **🎬 Auto Episode Merge:** Intelligent episodic video detection and lossless merging into a single file.
- **🛠 Highly Customizable:** Support for custom metadata, thumbnails, name substitution, and FFmpeg commands.
- **📱 Premium UI:** Stylish Unicode fonts and detailed status messages.

---

## 🚀 VPS Deployment Guide (Ubuntu/Debian)

Deploying HemanthBot is straightforward using Docker. Follow these steps for a clean installation.

### 1️⃣ System Update
Ensure your VPS is running the latest packages:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2️⃣ Install Required Tools
Install Git and other essential utilities:
```bash
sudo apt install git wget nano -y
```

### 3️⃣ Install Docker & Docker Compose
The easiest way to install Docker is using the official script:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 4️⃣ Clone the Repository
Clone your project to the VPS:
```bash
git clone https://github.com/Hemanth/HemanthBot mirrorbot
cd mirrorbot
```

### 5️⃣ Configuration
Copy the sample configuration file and edit it with your credentials:
```bash
cp config_sample.py config.py
nano config.py
```

**Essential Variables:**
- `BOT_TOKEN`: Get from [@BotFather](http://t.me/BotFather)
- `OWNER_ID`: Your Telegram ID (type `/id` to [@MissRose_bot](http://t.me/MissRose_bot))
- `TELEGRAM_API` & `TELEGRAM_HASH`: Get from [my.telegram.org](https://my.telegram.org)
- `DATABASE_URL`: Your MongoDB connection string.

*💡 Pro Tip: Use `CTRL+O`, `Enter`, and `CTRL+X` to save and exit nano.*

### 6️⃣ Launch the Bot
Start the bot in the background using Docker Compose:
```bash
sudo docker-compose up -d --build
```

---

## 🛠 Management Commands

| Action | Command |
| :--- | :--- |
| **View Logs** | `sudo docker-compose logs -f` |
| **Restart Bot** | `sudo docker-compose restart` |
| **Stop Bot** | `sudo docker-compose stop` |
| **Update/Rebuild** | `sudo docker-compose up -d --build` |

---

## 🏅 Credits & Support

- **Owner/Developer:** [Hemanth](http://t.me/ALONEKINGSTAR77)
- **Telegram Username:** [@alonekingstar77](http://t.me/ALONEKINGSTAR77)
- **Telegram Channel:** [Join Here](http://t.me/ALONEKINGSTAR77)

---
<p align="center">
  <b>Powered by Hemanth</b>
</p>
