##
##

from asyncio.log import logger
from os import link
from pytube import YouTube

def on_complete(stream, file_path):
    print("complete")


def on_progress(stream, chunk, bytes_remaining):
    # print progress bar, mainly for long videos
    #print(bytes_remaining)
    print (100-(bytes_remaining / stream.filesize *100))



# video= YouTube('link')
link=input("Enter")

video=YouTube(link, on_progress_callback=on_progress,on_complete_callback=on_complete)


choice=input("v or a")
if(choice=="a" or choice=="A"):
            video.streams.get_audio_only().download()
elif (choice=="v" or choice=="V"):
            video.streams.get_highest_resolution().download()
else:
            print("Invalid entry. Please exit and try again.")

#download 





# video info 
# print (video.title)

# video streams
# for i in video.streams():
    #print (streams)

#print (video.streams.get_highest_resolution())