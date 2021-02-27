#! /usr/bin/python3

import shutil, os
from pathlib import Path
from PIL import Image
from datetime import datetime

Path('./sorted_photos').mkdir(exist_ok=True)
Path('./screenshots').mkdir(exist_ok=True)

photo_formats = ['.jpg', '.jpeg', '.png', '.gif']
video_formats = ['.mov', '.mp4']


for folderName, subfolders, filenames in os.walk('./ios_photos_directory'):
    for filename in filenames:
        p = Path(filename)
        extension = p.suffix.lower()

        if extension not in photo_formats and extension not in video_formats: # skip markup files
            continue
        destination_dir = Path('./sorted_photos')
        image_path = Path(folderName, p)

        if extension in photo_formats: 
            im = Image.open(image_path)
            resolution = im.size

            # Check if photo is a screenshot
                # Uncropped screenshots have a userComment (tag 37510) of "Screenshot" regardless of if they are edited
                # Cropped screenshots have an xResolution (tag 282) of 144, but no userComment tag
                # Screenshots restored from a backup have neither of the above, so assume `.png` files of my phone's resolution are screenshots
            try:
                if 'Screenshot' in str(im.getexif()[37510]): # Definitely a screenshot, userComment info is in: `im.getexif()[37510]`
                    destination_dir = Path('./screenshots')     
            except KeyError:
                try:
                    if im.getexif()[282][0] == 144: # Probably a cropped screenshot, xResolution info is in: `im.getexif()[282][0]`
                        destination_dir = Path('./screenshots')     
                except KeyError:
                    if extension == ".png" and (resolution == (640, 1136) or resolution == (1136, 640)): # Might be a screenshot
                        destination_dir = Path('./screenshots')                    

        # Check if the photo has a DateTimeOriginal, this info is stored in tag 36867.
        try:
            date_taken_str = im.getexif()[36867]
            date_taken = datetime.strptime(date_taken_str, '%Y:%m:%d %H:%M:%S')
        except (KeyError, NameError):
            # Use Date Modified for the `date_taken` as a last resort
            date_taken = datetime.fromtimestamp(image_path.stat().st_mtime)

        new_file_name = f'{date_taken} {p}'
        shutil.copy(image_path, Path(destination_dir, new_file_name))