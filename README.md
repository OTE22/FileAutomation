# FileAutomation  
Automated file sorting system using Python + Watchdog  
GitHub Repository: **https://github.com/OTE22/FileAutomation**

[![GitHub Repo](https://img.shields.io/badge/GitHub-OTE22%2FFileAutomation-black?logo=github)](https://github.com/OTE22/FileAutomation)

---

## 🚀 Overview

**FileAutomation** is a lightweight Python script that monitors a folder in real time and automatically moves files into categorized destination folders based on file type, size, and naming rules.

This project helps keep your Downloads folder clean and organized without manual effort.

---

## ✨ Features

- 🔄 **Real-time folder monitoring**
- 🗂 **Auto-sorting into categories**:
  - Images
  - Videos
  - Audio (Music / SFX)
  - Documents
- 🆔 **Duplicate file handling**
  - Creates unique filenames like `file(1).png`, `file(2).png`
- 📝 **Detailed logging**
- ⚡ Lightweight and easy to configure

---

## 📂 Supported File Types

### 🖼 Images  
`.jpg`, `.jpeg`, `.png`, `.gif`, `.raw`, `.bmp`, `.heic`, `.svg`, `.ico`, etc.

### 🎬 Videos  
`.mp4`, `.mov`, `.avi`, `.wmv`, `.webm`, `.mpeg`, etc.

### 🎵 Audio  
`.mp3`, `.wav`, `.aac`, `.m4a`, `.flac`, `.wma`

### 📄 Documents  
`.pdf`, `.docx`, `.doc`, `.pptx`, `.xls`, `.xlsx`, `.odt`

---

## 📌 How It Works

1. The script watches `source_dir` for changes.
2. Any new or modified file is checked against known extensions.
3. The file is moved to the matching destination folder.
4. Audio files <10MB OR those containing `"SFX"` are moved to the **SFX folder**.
5. If a file already exists in the target location, the script generates a unique name.

---

## ⚙️ Configuration (Required)

Edit these values at the top of the script:

```python
source_dir = "C:\\Users\\User\\Downloads"
dest_dir_sfx = "C:\\Users\\User\\Sorted\\Audio\\SFX"
dest_dir_music = "C:\\Users\\User\\Sorted\\Audio\\Music"
dest_dir_video = "C:\\Users\\User\\Sorted\\Videos"
dest_dir_image = "C:\\Users\\User\\Sorted\\Images"
dest_dir_documents = "C:\\Users\\User\\Sorted\\Documents"
````

✔ Make sure all destination folders exist
✔ Use **double backslashes** `\\` on Windows

---

## 📦 Installation

Install required dependency:

```bash
pip install watchdog
```

Clone the repository:

```bash
git clone https://github.com/OTE22/FileAutomation.git
cd FileAutomation
```

---

## ▶️ Run the Script

```bash
python file_automation.py
```

Once running, the script watches your folder continuously and sorts files instantly.

---

## 🧪 Example Log Output

```
2025-11-14 12:45:10 - Moved audio file: song.mp3
2025-11-14 12:45:12 - Moved document file: report.pdf
2025-11-14 12:45:15 - Moved image file: photo.png
2025-11-14 12:45:20 - Moved video file: clip.mp4
```

---

## 📁 Project Structure

```
FileAutomation/
│
├── file_automation.py      # Main script
├── README.md               # Documentation
└── requirements.txt        # Optional dependencies file
```

---

## 🧠 Script Logic Summary

### `make_unique(dest, name)`

Generates a new filename if the file already exists.

### `move_file(dest, entry, name)`

Moves the file and handles duplicate renaming.

### `MoverHandler(FileSystemEventHandler)`

Handles detection of new/changed files and routes them to the right category.

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork this repo
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, please ⭐ **star the repository**:

👉 [https://github.com/OTE22/FileAutomation](https://github.com/OTE22/FileAutomation)

Your support motivates continued development!

```