from yt_dlp import YoutubeDL
import platform
import subprocess
import os
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'

output_dir = os.path.join(os.getcwd(), 'downloads')
ydl_opts={

    'format':'bestvideo+bestaudio/best',
    'merge_output_format':'mp4',
    'outtmpl':'%(title)s.%(ext)s',
    'postprocessors':[{
        'key':'FFmpegVideoConvertor',
        'preferedformat':'mp4'
    }]
}
with YoutubeDL() as ydl:
    print('Downloading...')
    ydl.download([url])
    print('Downloaded!')
video = os.path.join(output_dir, 'PSY - GANGNAM STYLE(강남' + '스타일) M_V.mp4')
def playfull(path):
    if platform.system()=="Windows":
        subprocess.run(['start', 'vlc','--fullscreen',video], shell=True)
print('Playing...')
playfull(video)





 
