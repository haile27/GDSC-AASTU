import os
import shutil
import time

def is_recent_file(file_path):
    stat = os.stat(file_path)
    modification_time = stat.st_mtime
    creation_time = stat.st_ctime

    current_time = time.time()

    twenty_four_hours = 24 * 60 * 60
    return current_time - modification_time <= twenty_four_hours or current_time - creation_time <= twenty_four_hours

def update_file(file_path):
    with open(file_path, 'a') as file:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"\nUpdated at {current_time}")

if not os.path.exists("last_24hours"):
    os.makedirs("last_24hours")

files = os.listdir()

recent_files = [file for file in files if is_recent_file(file)]

for file in recent_files:
    update_file(file)
    shutil.move(file, os.path.join("last_24hours", file))