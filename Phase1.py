import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import numpy as numpy
import librosa as lib

# 3.1
data, samplerate = sf.read('singing.wav')

# 3.2
soundSize = data.shape
if soundSize[1] > 1:
    # convert to mono
    data = sum(data, 2)/data.shape[1]

# 3.3
sd.play(data, samplerate)

# 3.4
sf.write('monoSinging.wav', data, samplerate)

# 3.5
# plotting audio as a function of sample num
sampleNumVector = numpy.linspace(1, soundSize[1], soundSize[1])
plt.figure(1)
plt.plot(sampleNumVector, data)

# 3.6
if samplerate > 16000:
    data = lib.load(data, samplerate=16000)

# 3.7
    newSize = data.shape

# Duration of signal is number of samples divided by freq
duration = newSize[1]/16000


#  From time = 0 to duration of signal with n samples.
x = numpy.linspace(0, duration, newSize[1])
cosSignal = numpy.cos(2000*numpy.pi*x)
plt.figure(1)
plt.plot(x, cosSignal)

sd.play(cosSignal, samplerate)