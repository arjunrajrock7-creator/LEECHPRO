# Deployment Guide for WZML-X Mirror Leech Bot

This guide provides step-by-step instructions for deploying a high-performance Telegram Mirror-Leech Bot based on the WZML-X (Wanda Zebra) or Mirror-leech-python framework.

## 1. Prerequisites

Before starting, ensure you have the following:

- **Telegram Bot Token**: Get it from [@BotFather](https://t.me/BotFather).
- **API ID & API HASH**: Get these from [my.telegram.org](https://my.telegram.org).
- **MongoDB URL**: A database connection string from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- **Google Drive Credentials**: `token.pickle` and `DRIVE_ID`.
- **RClone Config**: `rclone.conf` if you plan to use other cloud storages.

---

## 2. Environment Variables

Create a `config.env` file (refer to `config.env.sample`) and fill in the mandatory variables:

### Core Settings
- `BOT_TOKEN`: Your Telegram Bot Token.
- `OWNER_ID`: Your Telegram User ID.
- `TELEGRAM_API`: Your API ID.
- `TELEGRAM_HASH`: Your API HASH.
- `DATABASE_URL`: Your MongoDB connection string.

### Advanced Video Tools (-vt)
These variables enable features similar to the 'DC BoTs' version:
- `ENABLE_VT`: Set to `True`.
- `METADATA_AUTHOR`: Default name for 'Encoded By' tag.
- `VT_DUMP_CHAT`: Chat ID where processed videos will be dumped.
- `AUTO_MERGE`: Set to `True` if you want automatic merging of multi-part files.

---

## 3. Deployment Options

### Option A: Local or VPS (Using Docker) - Recommended

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Prepare config.env:**
   ```bash
   cp config.env.sample config.env
   # Edit config.env with your values
   ```

3. **Build and Run:**
   ```bash
   docker build -t wzml-bot .
   docker run -d --env-file config.env --name wzml-bot wzml-bot
   ```

### Option B: Heroku

1. **Create a new Heroku app.**
2. **Add Config Vars:** Go to Settings -> Reveal Config Vars and add all variables from `config.env.sample`.
3. **Deploy using Container Registry:**
   ```bash
   heroku container:push worker
   heroku container:release worker
   ```
   *Note: Ensure you have `heroku.yml` or a valid `Dockerfile` for Heroku.*

---

## 4. Advanced Features Usage

### Video Tools (-vt)
You can use the `-vt` flag when sending a link to the bot to open the Video Tool menu or perform direct actions:
- **Compress**: `-vt compress`
- **Trim**: `-vt trim HH:MM:SS HH:MM:SS`
- **Watermark**: `-vt watermark`
- **Metadata**: `-vt metadata "Title" "Author"`
- **Merge**: Use `/merge` command or `-vt merge`.

### User Settings
Users can use the `/usetting` command to customize their own:
- Thumbnails
- Captions
- Upload Destinations (GD/Telegram)

### Auto-Merge
If `AUTO_MERGE` is enabled, the bot will automatically detect multi-part files (like .001, .002 or part1, part2) and combine them after downloading.

---

## 5. Getting Google Drive Credentials

1. Go to [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project and enable Google Drive API.
3. Create OAuth 2.0 Credentials (Desktop App).
4. Download `credentials.json`.
5. Run a local python script to generate `token.pickle`:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   python3 generate_pickle.py
   ```
6. Upload `token.pickle` to a secret link or encode it to Base64.
