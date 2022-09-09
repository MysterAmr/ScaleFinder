import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "scale.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Play notes')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

notesMap = {16.35:'C', 17.32:'C#/Db', 18.35:'D', 19.45:'D#', 20.60:'E', 21.83:'F', 23.12:'F#/Gb', 24.50:'G', 25.96:'G#/Ab', 27.50:'A', 29.14:'A#/Bb', 30.87:'B'}
scales = {'C Major':('C', 'D', 'E', 'F', 'G', 'A', 'B'), 'B Major':('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#')}
notes = []

def FindScale(frames):
  
  for freq in frames:
    if freq in notesMap.keys():
      notes.append(freq)

  for key, values in scales.items():
          for value in values:
            common = 1 
