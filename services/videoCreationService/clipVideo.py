from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob


#index of .mp4 video to be clipped, start time of clip in seconds, end time of clip in seconds
myParams = [0,1,7]

def clip_video():

# code to clip a segment from the raw footage
    files = glob.glob("unedited_videos/*.mp4")
    print([(n, f) for n, f in enumerate(files)])

    index = int(myParams[0])
    start = int(myParams[1])
    end = int(myParams[2])

    ffmpeg_extract_subclip(
        files[index], start, end, targetname="clips/edited_clip_" + str(index + 1) + ".mp4")

clip_video()
