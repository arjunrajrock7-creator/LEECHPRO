# 🚀 DC BoTs Deployment Guide

This document provides a comprehensive walkthrough for setting up your **DC BoTs** instance on various platforms.

---

## 📋 Mandatory Environment Variables

Before deploying, ensure you have gathered the following credentials. These are essential for the bot to authenticate and function correctly.

| Variable | Description | Source |
| :--- | :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token | [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Your Telegram User ID | [@userinfobot](https://t.me/userinfobot) |
| `TELEGRAM_API` | Your API ID | [my.telegram.org](https://my.telegram.org) |
| `TELEGRAM_HASH` | Your API Hash | [my.telegram.org](https://my.telegram.org) |
| `DATABASE_URL` | MongoDB Atlas URI | [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) |

---

## 🐳 Docker Deployment (Recommended)

Docker is the preferred method for deployment as it ensures an isolated and consistent environment.

### 1. Prerequisites
- Docker and Docker Compose installed on your VPS.

### 2. Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git && cd yourrepo

# Prepare your configuration
cp config.env.sample config.env
nano config.env  # Enter your credentials

# Deploy with Docker Compose
docker-compose up -d --build
```

### 3. Alternative (Direct Docker Build)
```bash
docker build -t dc-bot .
docker run -d --name dc-bot --env-file config.env dc-bot
```

---

## 💜 Heroku Deployment

Heroku provides a quick way to host the bot with minimal server management.

### 1. Buildpacks
You **must** add the following buildpacks in this specific order:
1. `heroku/python`
2. `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`

### 2. Manual Deployment via CLI
```bash
# Login and Create App
heroku login
heroku create your-app-name

# Set Buildpacks
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git

# Deploy
git push heroku master
```

---

## 🛠 Advanced Storage Setup

### 📁 Google Drive Integration
- **TOKEN_PICKLE**: Generate this using `generate_drive_token.py` and convert the resulting file to a Base64 string for your `config.env`.
- **DRIVE_ID**: The unique ID of the folder or Team Drive where you want to store files.

### ☁️ RClone Support
1. Create your `rclone.conf` locally.
2. Encode the content to Base64: `cat rclone.conf | base64`.
3. Paste the string into `RCLONE_CONFIG` in your `config.env`.

---

> **💡 Pro Tip**: Always use the `/usetting` command inside Telegram after deployment to fine-tune your bot's behavior and UI!
