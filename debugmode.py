from asyncio import subprocess
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver
import os
import time
import subprocess
import tkinter
from tkinter import filedialog

cwddir = os.getcwd()

folder = cwddir

root = tkinter.Tk()
root.attributes('-topmost', True)
root.withdraw()

while True:
    choice = input("ディレクトリを変更しますか？ 'yes' or 'no' [Y/n]: ")
    if choice in ['Y','y', 'ye', 'yes']:
        folder = filedialog.askdirectory(initialdir = cwddir) 
        break
    elif choice in ['n', 'no']:
        folder = cwddir
        break
# 対象ディレクトリ
DIR_WATCH = folder
# 対象ファイル名のパターン
PATTERNS = ['*.py']
def on_modified(event):
    filepath = event.src_path
    filename = os.path.basename(filepath)
    print('%s changed' % filename)
    subprocess.call('python %s' % filepath)
# event_handler = LoggingEventHandler()
event_handler = PatternMatchingEventHandler(PATTERNS)
event_handler.on_modified = on_modified

observer = PollingObserver()
observer.schedule(event_handler, DIR_WATCH, recursive=True)
observer.start()
try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    observer.stop()
observer.join()
