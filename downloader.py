import os
x = input("Enter URL >> ")
os.system(f"yt-dlp -x --audio-format mp3 --user-agent 'Mozilla/5.0' {x}")
