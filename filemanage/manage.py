import os
import logging
import mimetypes
import shutil
import time
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

# Directory paths
source_dir = "/Users/2004r/Downloads"
gallery_dir = "/Users/2004r/Pictures/Saved Pictures"
music_dir = "/Users/2004r/Music"
file_dir = "/Users/2004r/Documents/files"

def move(dest, source_path, name):
    try:
        # Ensure destination directory exists
        os.makedirs(dest, exist_ok=True)
        
        dest_path = os.path.join(dest, name)
        if os.path.exists(dest_path):
            name, ext = os.path.splitext(name)
            counter = 1
            while os.path.exists(os.path.join(dest, f"{name}_{counter}{ext}")):
                counter += 1
            new_name = f"{name}_{counter}{ext}"
            dest_path = os.path.join(dest, new_name)
        
        # Add debug logging
        logging.debug(f"Moving file:\nFrom: {source_path}\nTo: {dest_path}")
        
        # Check if source file exists
        if not os.path.exists(source_path):
            logging.error(f"Source file does not exist: {source_path}")
            return None
            
        shutil.move(source_path, dest_path)
        return os.path.basename(dest_path)
    except Exception as e:
        logging.error(f"Error in move function: {str(e)}")
        return None

class MyEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        logging.info("Event Handler Initialized")
        logging.info(f"Source Directory: {source_dir}")
        logging.info(f"Gallery Directory: {gallery_dir}")
        logging.info(f"Music Directory: {music_dir}")
        logging.info(f"Files Directory: {file_dir}")

    def on_created(self, event):
        if event.is_directory:
            return

        try:
            # Get the full path and file name
            source_path = event.src_path
            name = os.path.basename(source_path)
            
            # Add debug logging
            logging.info(f"New file detected: {name}")
            logging.info(f"Full path: {source_path}")
            
            # Wait a bit to ensure file is fully written
            time.sleep(1)
            
            # Check if file still exists (wasn't quickly deleted)
            if not os.path.exists(source_path):
                logging.warning(f"File no longer exists: {source_path}")
                return

            # Get mime type
            mime_type, _ = mimetypes.guess_type(name)
            logging.info(f"Detected mime type: {mime_type}")

            # Process based on file type
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                logging.info(f"Processing image file: {name}")
                new_name = move(gallery_dir, source_path, name)
                if new_name:
                    logging.info(f"Successfully moved image {name} to {gallery_dir} as {new_name}")
            
            elif name.lower().endswith(('.mp3', '.wav', '.flac')):
                logging.info(f"Processing music file: {name}")
                new_name = move(music_dir, source_path, name)
                if new_name:
                    logging.info(f"Successfully moved music {name} to {music_dir} as {new_name}")
            
            elif mime_type == "application/pdf":
                logging.info(f"Processing PDF file: {name}")
                new_name = move(file_dir, source_path, name)
                if new_name:
                    logging.info(f"Successfully moved PDF {name} to {file_dir} as {new_name}")
            else:
                logging.info(f"Unhandled file type: {name} (mime: {mime_type})")

        except Exception as e:
            logging.error(f"Error processing {name}: {str(e)}", exc_info=True)

if __name__ == "__main__":
    # Set up more detailed logging
    logging.basicConfig(
        level=logging.DEBUG,  # Changed to DEBUG for more detailed logging
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create all necessary directories
    for directory in [gallery_dir, music_dir, file_dir]:
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Ensured directory exists: {directory}")

    logging.info("Starting Observer")
    logging.info(f"Source directory exists: {os.path.exists(source_dir)} ({source_dir})")
    logging.info(f"Gallery directory exists: {os.path.exists(gallery_dir)} ({gallery_dir})")
    logging.info(f"Music directory exists: {os.path.exists(music_dir)} ({music_dir})")
    logging.info(f"Files directory exists: {os.path.exists(file_dir)} ({file_dir})")
    logging.info("==========================")

    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()

    logging.info("Monitoring started...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        logging.info("Observer Stopped")