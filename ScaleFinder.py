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

class Scale:
  def __init__(self, name, size):
    self.name = name # Name of scale
    self.size = size # Number of notes played corresponding to scale

A_major = Scale('A Major', 0)
A_minor = Scale('A Minor', 0)
B_major = Scale('B Major', 0)
B_minor = Scale('B Minor', 0)
C_major = Scale('C Major', 0)
C_minor = Scale('C Minor', 0)
D_major = Scale('D Major', 0)
D_minor = Scale('D Minor', 0)
E_major = Scale('E Major', 0)
E_minor = Scale('E Minor', 0)
F_major = Scale('F Major', 0)
F_minor = Scale('F Minor', 0)
G_major = Scale('G Major', 0)
G_minor = Scale('G Minor', 0)

notes_map = {16.35:'C', 17.32:'C♯/D♭', 18.35:'D', 19.45:'D♯/E♭', 20.60:'E', 21.83:'F', 23.12:'F♯/G♭', 24.50:'G', 
25.96:'G♯/A♭', 27.50:'A', 29.14:'A♯/B♭', 30.87:'B'}

scale_dict = {Amajor:('A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭'), Aminor: ('A', 'B', 'C', 'D', 'E', 'F', 'G'), 
Bmajor:('C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B'), Bminor: ('B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A'), 
Cmajor:('C', 'D', 'E', 'F', 'G', 'A', 'B'), Dmajor:('D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭'), 
Emajor:('E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D♯/E♭'), Fmajor:('F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'E'), 
Gmajor: ('G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭')}

notes = []

# This function will search for the scale
def FindScale(frames):
  for key, value in notes_map.items(): # This loop determine which notes were played
    if key in frames:
      notes.append(value)

  for key, values in scale_dict.items(): # This loop determines which note notes and the ith scale of scales.values have in common
    for value in values:
      if value in notes: # If notes and the ith scale of scales.values have a note in common, increment the size attribute of the corresponding scale
        key.size += 1
  
  return sorted(scale_dict.keys(), key=lambda x: x.size, reverse=True)[0].name

print('The scale is', FindScale(frames))
print('The notes you played were', notes)
  
