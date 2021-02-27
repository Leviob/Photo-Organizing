# Photo Organizing
### When exporting the entire collection of photos from Google Photos or from my old iPhone, the result is not at all user friendly. The purpose of these programs is to rename all the photos using dates from their metadata so that they can be browsed in a logical order. 

## iPhone Organizing
I should preface this project by saying, if I were using a Mac, this process would be unnecessary. Rather, I've resorted to copying the photo files directly from my phone to my Linux PC. The copied photos are distributed within several folders. Inside each folder are photos from similar dates, but the file names used are inconsistent. Photos taken with the phone's camera have a sequential pattern, except the edited copies are prepending with an "E", and saved photos have a seemingly random naming convention - it's a bit of a mess. The file's modified date is sometimes months away from the date the photo was taken, so sorting by that is still not correct. 

`ios_photo_organizing.py` iterates over every file in the directories where my photos are saved. It collects the date the photo was taken, or if that does not exist in the metadata, the Date Modified. It uses the collected date to rename the files. Screenshots are identified and saved to a separate directory from all other photos and videos using the same naming convention. 

As an example, say the following unorganized files are in my `ios_photos_directory`:

    photo.JPG
    saved_image.JPG
    saved_video.MP4
    screenshot.PNG

The files would be copied to the `sorted_photos` and `screenshots` directories, with their names modified:

    2020-03-01 11:48:00 saved_image.JPG
    2020-03-04 13:42:45 photo.JPG
    2020-05-12 08:22:24 saved_video.MP4
    
    2020-06-14 21:37:25 screenshot.PNG

The result is a directory of my photos and videos in chronological order, with a separate directory for screenshots. 

## Google Photos Organizing
Eventually I plan to implement `google_takout_photo_organizing.py` which will organize the photos exported using Google Takeout. 
