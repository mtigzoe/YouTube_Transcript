from youtube_transcript_api import YouTubeTranscriptApi
import re
import pafy 
import os 
  
source = input("Copy and paste your YouTube url: ")
source_video_id = pafy.new(source) 
video_id = source_video_id.videoid
srt = YouTubeTranscriptApi.get_transcript(video_id)
 
with open("subtitles.html", "w") as f:
    
        
    for i in srt:
        
        f.write("{}\n".format(i))
        print("Open the HTML file and read the transcript.")


