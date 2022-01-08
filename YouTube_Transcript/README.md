Instructions 

1. Copy your video channel's URL in YouTube website.
2. Paste it in your terminal after running the Python application. 
3. Press the enter key.
4. Read a transcript after opening the HTML file.

Issues

1/8/2022

"pafy" module had issues with dislike counts in YouTube, because I was not able to retrieve a transcript. After commenting out "self._dislikes = self._ydl_info['dislike_count']" on line 54 in backend_youtube_dl.py, I was able to retrieve a transcript from YouTube.
