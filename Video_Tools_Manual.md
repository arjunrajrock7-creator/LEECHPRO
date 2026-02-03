# 🎬 Video Tools Manual (`-vt`)

The **Video Tools** suite is a signature feature of **⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡**, allowing you to manipulate media files directly during the mirroring process.

---

## 🛠 How to Trigger

To use these tools, simply add the `-vt` flag at the end of your mirror or leech command:

```text
/leech https://example.com/movie.mkv -vt
```

After the download finishes, the bot will present an **Inline Menu** with processing options.

---

## 💎 Available Processing Tools

### 📦 1. Intelligent Compression
- **Mode**: Optimized FFMPEG presets.
- **Benefit**: Significantly reduces file size while preserving visual fidelity. Perfect for mobile viewing.
- **Settings**: Customizable via `FFMPEG_CMDS` in `config.env`.

### ✂️ 2. Precision Trimming
- **Action**: Extract specific clips from a larger video.
- **Usage**: Input the start and end timestamps (e.g., `00:05:00` to `00:07:30`).

### 🖼 3. Dynamic Watermarking
- **Action**: Overlay an image or text logo on your video.
- **Setup**: Provide a PNG file path or GDrive ID in `WATERMARK_PATH`.
- **Branding**: Ensures your content is uniquely yours.

### 🔗 4. Advanced Merging
The bot supports three types of merging:
1. **Video + Video**: Join multiple episodes or parts.
2. **Video + Audio**: Add background music or dual-audio tracks.
3. **Video + Subtitle**: Hardcode (permanent) or Softcode (selectable) subtitles.

### 📝 5. Metadata Tagging
- **Title**: Update the global title of the video stream.
- **Encoded By**: Add your signature branding to the encoder metadata field.

---

## 🤖 Automation & UI

### 📊 Screenshot Grids
Generate a professional contact sheet of your video.
- **Grid Layout**: Customize the rows and columns (e.g., `2x2`, `4x4`) via `THUMBNAIL_LAYOUT`.

### 🔄 Auto-Merge Mode
If enabled via `AUTO_MERGE=True`, the bot will scan for files with common prefixes (e.g., `Ep01.part1`, `Ep01.part2`) and combine them automatically without manual intervention.

---

> **⚠️ Warning**: Processing high-resolution videos (4K) requires significant CPU resources. Ensure your VPS has adequate performance if you plan on heavy transcoding.
