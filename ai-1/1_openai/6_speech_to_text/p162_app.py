import openai 

audio_file = open("audio.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript.text)
