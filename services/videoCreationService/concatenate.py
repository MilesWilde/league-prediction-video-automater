# Code to join different mp4 video files
import glob
import os


def concatenate():
    stringa = "ffmpeg -i \"concat:"
    list_video = glob.glob("clips/*.mp4")
    list_file_temp = []
    for f in list_video:
        file = "temp" + str(list_video.index(f) + 1) + ".ts"
        os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
        list_file_temp.append(file)
    print(list_file_temp)
    for f in list_file_temp:
        stringa += f
        if list_file_temp.index(f) != len(list_file_temp) - 1:
            stringa += "|"
        else:
            stringa += "\" -c copy  -bsf:a aac_adtstoasc finished_movie/final.mp4"
    print(stringa)
    os.system(stringa)


# concatenate()


def remove_files():
    # Delete temp files
    fileList = glob.glob('*.ts')

    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)


# remove_files()

