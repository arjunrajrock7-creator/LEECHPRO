# 🎬 Video Tools Manual (-vt)

The Video Tools feature allows you to process videos during the Leech/Mirror process. To activate it, simply append `-vt` to your command.

### 🛠 How to Use
**Example:**
```
/leech https://example.com/video.mp4 -vt
```
Once the download is complete, a menu will appear with the following options:

---

### 1. 📦 Compress Video
- **Goal**: Reduce file size while maintaining quality.
- **How it works**: Uses FFMPEG with pre-defined or custom CRF values.
- **DC BoTs Mode**: Optimized for high-speed compression without significant quality loss.

### 2. ✂️ Trim & Crop
- **Goal**: Upload only a specific part of the video.
- **Usage**: You can specify start and end times (e.g., `00:00:10` to `00:01:00`).

### 3. 🖼 Watermark
- **Goal**: Protect your content with a custom logo or text.
- **Requirement**: Set `WATERMARK_PATH` in `config.env` with a GDrive ID or local path to your PNG watermark.

### 4. 🔗 Merge Tools
- **Video + Video**: Combine multiple video files into one.
- **Video + Audio**: Replace or add an audio track to a video.
- **Video + Subtitle**: Hardcode or softcode subtitles into the video.

### 5. 📝 Metadata Editing
- **Title**: Change the 'Title' tag of the video.
- **Author/Encoded By**: Add your own branding to the 'Encoded By' metadata tag.

### 6. 🖼 Screenshot & Thumbnail Mode
- **Goal**: Generate a grid of screenshots or a specific thumbnail.
- **Configuration**: Use `THUMBNAIL_LAYOUT` (e.g., `3x3`) to control the output grid.

---

## 🤖 Automation Features

### Auto-Merge
If `AUTO_MERGE` is set to `True` in `config.env`, the bot will automatically attempt to merge files if they follow a specific naming convention (e.g., `Part1`, `Part2`).

### Metadata Cleaner
Automatically removes metadata from downloaded files to ensure a "clean" upload with only your custom tags.
