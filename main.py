import os
import sys
import logging
import watchdog.observers as Observer
import watchdog.events as LoggingEventHandler

with os.scandir("/Users/jeremy/Desktop/siteweb_techno") as entries:
    for entry in entries:
        print(entry.name)

#file listner
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()