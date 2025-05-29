import yt_dlp
from pathlib import Path

def get_youtube_video_info(video_url):
    ydl_opts = {
        'cookies' :'./data/cookies.txt',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            return {
                'id' : video_info.get('id'),
                'title' : video_info.get('title'),
                'upload_date': video_info.get('upload_date'),
                'channel' : video_info.get('channel'),
                'duration' : video_info.get('duration_string'),
            }
    except Exception as e:
        print("yt_dlp.YoutubeDL(ydl_opts) error")
        return f'Error: {e}'

def remove_invalid_char_for_filename(input_str):
    invalid_characters = '<>:"/\|?*'

    for char in invalid_characters:
        input_str = input_str.replace(char, '_')

    while input_str.endswith('.'):
        input_str = input_str[:-1]

    return input_str

def download_youtube_video(video_url, folder, filename=None):
    video_info = get_youtube_video_info(video_url)
    
    if isinstance(video_info, str) and video_info.startswith("Error"):
        print(video_info)
        return None, None

    title = video_info['title']
    filename_no_ext = remove_invalid_char_for_filename(title)

    if filename is None:
        download_file = f"{filename_no_ext}.mp4"
    else:
        download_file = filename

    outtmpl_str = f'{folder}/{download_file}'

    download_path = Path(outtmpl_str)

    ydl_opts = {
        'cookies' :'./data/cookies.txt',
        'extract_audio': True,
        'format': 'bestaudio',
        'outtmpl': outtmpl_str,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=True)
        title = video_info.get('title', None)

    return title, download_path

video_url = 'https://youtu.be/RcGyVTAoXEU?si=49Frho5vGyYQsGxd'
download_folder = './data'
file_name = "youtube_download"
video_title, download_path = download_youtube_video(video_url, download_folder, file_name)

print("- 유튜브 제목 : ", video_title)
print("- 다운로드한 파일명 : ", download_path.name)
