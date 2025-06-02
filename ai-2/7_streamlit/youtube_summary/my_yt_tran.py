import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# 유튜브 비디오 정보를 가져오는 함수
def get_youtube_video_info(video_url):
    ydl_opts = {            # 다양한 옵션 지정
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False) # 비디오 정보 추출
        video_id = video_info['id']              # 비디오 정보에서 비디오 ID 추출
        title = video_info['title']              # 비디오 정보에서 제목 추출
        upload_date = video_info['upload_date']  # 비디오 정보에서 업로드 날짜 추출
        channel = video_info['channel']          # 비디오 정보에서 채널 이름 추출
        duration = video_info['duration']        # 비디오 정보에서 길이 추출

    return video_id, title, upload_date, channel, duration

# 유튜브 비디오 URL에서 비디오 ID를 추출하는 함수
def get_video_id(video_url):
    # yt-dlp 모듈을 사용하여 유튜브 비디오 정보를 추출합니다.
    ydl_opts = {'quiet': True, 'no_warnings': True}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        return video_info['id']

# 유튜브 동영상 자막을 직접 가져오는 함수
def get_transcript_from_youtube(video_url, lang='en'):
    # 비디오 ID 추출
    video_id = get_video_id(video_url)

    try:
        # 자막 가져오기
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])

        # 텍스트 형식으로 변환
        text = " ".join([entry['text'] for entry in transcript])  # ✅ 올바른 접근

        return text

    except NoTranscriptFound:
        raise NoTranscriptFound("자막을 찾을 수 없습니다.")
    except TranscriptsDisabled:
        raise TranscriptsDisabled("자막이 비활성화된 영상입니다.")
    except Exception as e:
        raise Exception(f"자막 가져오기 실패: {str(e)}")
