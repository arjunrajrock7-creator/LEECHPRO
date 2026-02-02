# 🚀 DC BoTs Deployment Guide

This guide provides step-by-step instructions for deploying the high-performance Telegram Mirror-Leech Bot based on WZML-X.

---

## 📋 Mandatory Environment Variables

To make the bot function exactly like the "DC BoTs" version, ensure these variables are set in your `config.env`:

| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather. |
| `OWNER_ID` | Your Telegram User ID. |
| `TELEGRAM_API` | Your API ID from https://my.telegram.org. |
| `TELEGRAM_HASH` | Your API Hash from https://my.telegram.org. |
| `DATABASE_URL` | MongoDB Atlas URI for settings and user data. |
| `UPSTREAM_REPO` | `https://github.com/SilentDemonSD/WZML-X` |
| `UPSTREAM_BRANCH` | `wzv3` |
| `EE_VIDEO_TOOL` | Set to `True` for the Video Tool menu. |

---

## 🐳 Docker Deployment (Recommended)

### 1. Prerequisites
- Docker and Docker Compose installed on your VPS.

### 2. Steps
1. Clone your repository:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git && cd yourrepo
   ```
2. Create and edit `config.env`:
   ```bash
   cp config.env.sample config.env
   nano config.env
   ```
3. Build and Run the container:
   ```bash
   docker build -t dc-bot .
   docker run -d --name dc-bot --env-file config.env dc-bot
   ```
   *Alternatively, use Docker Compose:*
   ```bash
   docker-compose up -d
   ```

---

## 💜 Heroku Deployment

### 1. Prerequisites
- Heroku account and Heroku CLI.

### 2. Steps
1. Log in to Heroku:
   ```bash
   heroku login
   ```
2. Create a new app:
   ```bash
   heroku create your-app-name
   ```
3. Add mandatory buildpacks:
   ```bash
   heroku buildpacks:add heroku/python
   heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
   ```
4. Configure environment variables in the Heroku Dashboard (Settings > Config Vars).
5. Push your code:
   ```bash
   git push heroku master
   ```

---

## 💻 Local Deployment

### 1. Prerequisites
- Python 3.10+
- FFmpeg and Aria2 installed in system PATH.

### 2. Steps
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Fill `config.env`.
3. Start the bot:
   ```bash
   python3 -m bot
   ```

---

## 🛠 Advanced Features Usage

- **/usetting**: Opens the user settings menu to customize thumbnails, captions, and upload destinations.
- **/leech [link]**: Download a file and upload it to Telegram.
- **/mirror [link]**: Download a file and upload it to Google Drive.
- **Video Tools (-vt)**: Add `-vt` at the end of a /leech or /mirror command to open the Video Tool menu (Merge, Trim, Compress, etc.).
