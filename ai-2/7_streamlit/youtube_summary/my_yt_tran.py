import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_youtube_video_info(video_url):
    ydl_opts = {
        'cookies' :'./data/cookies.txt',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        return {
            'id' : video_info.get('id'),
            'title' : video_info.get('title'),
            'upload_date': video_info.get('upload_date'),
            'channel' : video_info.get('channel'),
            'duration' : video_info.get('duration_string'),
        }
    
def get_video_id(video_url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        return video_info.get('id')

def get_transcript_from_youtube(video_url, lang='en'):
    video_id = get_video_id(video_url)
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])

    text_formatter = TextFormatter()
    text_formatted = text_formatter.format_transcript(transcript)
    return text_formatted