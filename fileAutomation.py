import logging
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# =====================================================
# 🔧 USER CONFIGURATION (Fill These Paths)
# =====================================================

WATCH_FOLDER = ""  # Example: "C:\\Users\\User\\Downloads"
FOLDER_SFX = ""
FOLDER_MUSIC = ""
FOLDER_VIDEOS = ""
FOLDER_IMAGES = ""
FOLDER_DOCS = ""

# =====================================================
# 📦 File Extension Categories
# =====================================================

IMAGE_TYPES = [
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw",
    ".bmp", ".heic", ".svg", ".ico", ".jfif", ".jp2", ".cr2", ".arw", ".eps"
]

VIDEO_TYPES = [
    ".mp4", ".mov", ".avi", ".wmv", ".mkv", ".flv", ".webm", ".mpeg",
    ".mpg", ".m4v", ".ogg", ".mp2", ".qt"
]

AUDIO_TYPES = [
    ".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma"
]

DOCUMENT_TYPES = [
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".odt"
]

# =====================================================
# 🛠 Utility Functions
# =====================================================

def generate_unique_filename(dest_folder: str, filename: str) -> str:
    base_name, ext = splitext(filename)
    counter = 1

    while exists(f"{dest_folder}/{filename}"):
        filename = f"{base_name}({counter}){ext}"
        counter += 1

    return filename


def relocate_file(destination: str, entry_obj, filename: str):
    if exists(f"{destination}/{filename}"):
        unique_name = generate_unique_filename(destination, filename)
        rename(join(destination, filename), join(destination, unique_name))

    move(entry_obj, destination)

# =====================================================
# 📂 File Handler Class
# =====================================================

class AutoOrganizer(FileSystemEventHandler):

    def on_modified(self, event):
        with scandir(WATCH_FOLDER) as folder_items:
            for item in folder_items:
                name = item.name

                self._handle_audio(item, name)
                self._handle_video(item, name)
                self._handle_image(item, name)
                self._handle_document(item, name)

    # -------------------------------------------------

    def _handle_audio(self, item, name):
        for ext in AUDIO_TYPES:
            if name.lower().endswith(ext):
                dest = FOLDER_SFX if item.stat().st_size < 10_000_000 or "sfx" in name.lower() else FOLDER_MUSIC
                relocate_file(dest, item, name)
                logging.info(f"[AUDIO] Moved: {name}")
                break

    def _handle_video(self, item, name):
        for ext in VIDEO_TYPES:
            if name.lower().endswith(ext):
                relocate_file(FOLDER_VIDEOS, item, name)
                logging.info(f"[VIDEO] Moved: {name}")
                break

    def _handle_image(self, item, name):
        for ext in IMAGE_TYPES:
            if name.lower().endswith(ext):
                relocate_file(FOLDER_IMAGES, item, name)
                logging.info(f"[IMAGE] Moved: {name}")
                break

    def _handle_document(self, item, name):
        for ext in DOCUMENT_TYPES:
            if name.lower().endswith(ext):
                relocate_file(FOLDER_DOCS, item, name)
                logging.info(f"[DOC] Moved: {name}")
                break


# =====================================================
# ▶️ Script Runner
# =====================================================

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    organizer_handler = AutoOrganizer()
    observer = Observer()
    observer.schedule(organizer_handler, WATCH_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
