import librosa
import pandas as pd

# Load the audio file
filename = 'Popia.ogg'
y, sr = librosa.load(filename, sr=None)

# Detect the beats
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beats, sr=sr)

# Save the beat times to a CSV file
beat_data = {'beat_times': beat_times}
df = pd.DataFrame(beat_data)
df.to_csv('beat_times.csv', index=False)
