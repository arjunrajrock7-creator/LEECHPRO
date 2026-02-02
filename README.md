# WZML-X Advanced Mirror Leech Bot

A high-performance Telegram Mirror-Leech Bot based on the WZML-X (Wanda Zebra) or Mirror-leech-python repository, featuring advanced Video Tools and multi-cloud support.

## 🚀 Key Features

- **Mirror & Leech**: Support for Google Drive, Telegram, and RClone-supported clouds.
- **Advanced Video Tools (-vt)**:
  - Compress videos to various qualities (720p, 480p, etc.).
  - Trim and Watermark videos during the leech process.
  - Merge multiple video/audio/subtitle tracks.
  - Metadata editing (Title, Encoded By).
- **Automation**: Auto-Merge of multi-part files, Auto-Thumbnail generation.
- **User Customization**: `/usetting` for personalized thumbnails, captions, and upload paths.
- **Search**: Integrated torrent and file search.

## 🛠 Deployment

For detailed deployment instructions, please refer to the [DEPLOYMENT.MD](DEPLOYMENT.md) guide.

### Quick Start (Docker)
1. Copy `config.env.sample` to `config.env` and fill it.
2. Build: `docker build -t wzml-bot .`
3. Run: `docker run -d --env-file config.env --name wzml-bot wzml-bot`

## 📄 Configuration

A detailed template with all available environment variables can be found in [config.env.sample](config.env.sample).

## 🤝 Support
Join our Telegram channel for updates: [@WZML_X](https://t.me/WZML_X)
