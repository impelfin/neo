import yt_dlp
import openai
from pathlib import Path
import os
import textwrap
import deepl

## Part 1
#
# 유튜브 비디오 정보를 가져오는 함수
def get_youtube_video_info(video_url):
    ydl_opts = {
        'cookies' :'./data/cookies.txt',
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True
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
        return f'Error: {e}'

# 파일 이름에 부적합한 문자를 제거하는 함수
def remove_invalid_char_for_filename(input_str):
    invalid_characters = '<>:"/\|?*'
    for char in invalid_characters:
        input_str = input_str.replace(char, '_')
    input_str = input_str.rstrip('.')  # 마지막 '.' 제거를 더 간결하게 처리
    return input_str

# 유튜브 비디오를 오디오 파일로 다운로드하는 함수 
def download_youtube_as_mp3(video_url, folder, file_name=None):
    video_info = get_youtube_video_info(video_url)
    
    if isinstance(video_info, str) and video_info.startswith("Error"):
        print(video_info)
        return None, None

    title = video_info['title']
    filename_no_ext = remove_invalid_char_for_filename(title)

    if file_name == None:
        download_file = f"{filename_no_ext}"
    else:
        download_file = f"{file_name}"

    outtmpl_str = Path(folder) / download_file

    ydl_opts = {
        'cookies' :'./data/cookies.txt',
        'format' : "bestaudio/best",
        'outtmpl' : str(outtmpl_str),
        'noplaylist' : True,
        'quiet' : True,
        'no_warnings' : True,
        'extractaudio' : True,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return title, outtmpl_str
    except Exception as e:
        return str(e), None
    
video_url = "https://www.youtube.com/watch?v=EKqQvzyVAh4"
download_folder = "./data"
file_name = "youtube_video_KBS_news"

title, download_path = download_youtube_as_mp3(video_url, download_folder, file_name)

if download_path:
    print(f"- 유튜브 제목 : {title}")
    print(f"- 다운로드한 파일명 : {download_path.name}")
else:
    print(f"Error downloading video : {title}")

print('-' * 50)


## Part 2 
#
# Audio 자막을 Text로 변환. 다중언어인 경우 영어로 출력
def audio_transcribe(input_path, resp_format="text", lang="en"):
    input_path = str(input_path) + ".mp3"
    with open(input_path, "rb") as f:
        transcript = openai.Audio.transcribe(
            model = "whisper-1",
            file=f,
            language = lang,
            response_format = resp_format
        )

    path = Path(input_path)
    if resp_format == "text":
        output_file = f"{path.parent}/{path.stem}.txt"
    else:
        output_file = f"{path.parent}/{path.stem}.srt"

    output_path = Path(output_file)

    with open(output_file, "w", encoding='utf-8') as f:
        f.write(transcript)

    return transcript, output_path

audio_path = download_path

print(f"- [오디오 파일명] {audio_path.name}\n")
r_format = "text"

transcrpt, output_path = audio_transcribe(audio_path, r_format)
shorten_text = textwrap.shorten(transcrpt, width=150, placeholder=" [...이하 생략...]")

print(f"- [텍스트 추출 형식] {r_format}\n")
print(f"- [출력 파일] {output_path.name}\n")
print(f"- [음성 추출 결과(일부 출력)]\n {shorten_text[:137]}\n")

print('-' * 50)


## Part 3
#
# 영어 자막을 한국어 자막으로 번역
def translate_text_file(input_path, target_lang="KO"):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    auth_key = os.environ["DEEPL_AUTH_KEY"]
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_lang)

    path = Path(input_path)
    output_file = f"{path.parent}/{path.stem}_번역_{target_lang}{path.suffix}"

    output_path = Path(output_file)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text)

    return output_path

input_path = output_path
translate_file = translate_text_file(input_path)

print(f"- [번역 파일] {translate_file.name}\n")


## Part 4
#
# 한국어 자막으로 학습하여 질문에 답변
def answer_from_given_info(question_info, prompt):
    user_content = f"{prompt} 다음 내용을 바탕으로 질문에 답해 줘. {question_info}"

    message = [
        { "role": "user", "content": user_content }
    ]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message,
        max_tokens = 500,
        stop = ["."],
        temperature = 0.2,
    )

    return response['choices'][0]['message']['content']

file_name = translate_file
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

print('-' * 50)

question_info = text
prompt = "마이크로 소프트는 OpenAI 개발에 얼마를 투자했나요?"
print(prompt)
response = answer_from_given_info(question_info, prompt)
print(response)
print('-' * 50)

prompt = "KBS가 인터뷰한 사람은 누구인가요?"
print(prompt)
response = answer_from_given_info(question_info, prompt)
print(response)
print('-' * 50)
