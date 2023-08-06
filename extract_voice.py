import whisper
import moviepy.editor as mp

model = whisper.load_model("base")
file_name = input("Enter the file name: ")

clip = mp.AudioFileClip(file_name)
wav_file = f"{file_name.split('.')[0]}.wav"
clip.write_audiofile(wav_file)

result = model.transcribe(wav_file)

# Get clips from the result
clips = []
for segment in result['segments']:
    start = segment['start']
    end = segment['end']
    clip = mp.AudioFileClip(wav_file).subclip(start, end)
    clips.append(clip)

# Concatenate the clips
final_clip = mp.concatenate_audioclips(clips)
final_clip.write_audiofile(f"{file_name.split('.')[0]}_extracted.wav")