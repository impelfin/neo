import openai 

file_path = './data/서연의_하루_TTS_배경음악_short.mp3'

audio_file = open(file_path, "rb")

response = openai.Audio.translate(
    model="whisper-1",
    file=audio_file,
    response_format="json" # text, srt, vtt, json, verbose_json
)

audio_file.close()
print(response)