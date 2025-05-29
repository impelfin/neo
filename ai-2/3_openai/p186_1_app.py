import openai 

file_path = './data/서연의_하루_TTS_short.mp3'

audio_file = open(file_path, "rb")

response = openai.Audio.transcribe(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

audio_file.close()
print(response)