from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter, TextFormatter

def get_video_id(video_url):
    video_id = video_url.split("v=")[1][:11]

    return video_id

video_url = 'https://www.youtube.com/watch?v=Ks-_Mh1QhMc'
video_id = get_video_id(video_url)

transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

print(f"- Youtube Video ID : {video_id}")
for transcript in transcript_list:
    print(f"- [자막 언어] {transcript.language}, [자막 언어 코드] {transcript.language_code}")
print('-' * 50)

try:
    transcript_obj = transcript_list.find_transcript(['ko'])
except:
    transcript_obj = transcript_list.find_generated_transcript(['ko'])
transcript = transcript_obj.fetch()
print(transcript[0:3])
print('-' * 50)

srt_formatter = SRTFormatter()
srt_formatterted = srt_formatter.format_transcript(transcript)
print(srt_formatterted[:150])
print('-' * 50)

text_formatter = TextFormatter()
text_formatterted = text_formatter.format_transcript(transcript)
print(text_formatterted[:150])
print('-' * 50)

download_folder = './data'

srt_file = f'{download_folder}/{video_id}.srt'
print('- SRT 파일 저장 : ', srt_file)
with open(srt_file, 'w', encoding='utf-8') as f:
    f.write(srt_formatterted)

text_file = f'{download_folder}/{video_id}.txt'
print('- TXT 파일 저장 : ', text_file)
with open(text_file, 'w', encoding='utf-8') as f:
    f.write(text_formatterted)
