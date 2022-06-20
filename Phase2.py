import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import numpy as numpy
import librosa as lib
from frequency2mel import frequency2mel
from mel2frequency import mel2frequency
from getKaiserWindow import getKaiserWindow


def phase2(fileName, extension, N):
    soundFile = '.'.join(fileName, extension)

    # 3.1
    data, samplerate = sf.read('singing.wav')

    # 3.2
    soundSize = data.shape
    if soundSize[1] > 1:
        # convert to mono
        data = sum(data, 2) / data.shape[1]

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
    duration = newSize[1] / 16000

    #  From time = 0 to duration of signal with n samples.
    x = numpy.linspace(0, duration, newSize[1])
    cosSignal = numpy.cos(2000 * numpy.pi * x)
    plt.figure(1)
    plt.plot(x, cosSignal)

    sd.play(cosSignal, samplerate)

    # Task 4: Filter Design

    # %Determine upper and lower bounds of human hearing in mels (unit of pitch)
    melsLowerBound = frequency2mel(100)
    melsUpperBound = frequency2mel(7900)  # Should be 8000.

    # Divide pitches into N channels of even width
    melsChannels = numpy.linspace(melsLowerBound, melsUpperBound, N + 1)

   # Convert channels from pitches (mels) to frequency (Hz)
    freqChannels = mel2frequency(melsChannels)

    arr = numpy.ones(N + 1)

   # Plotting visual rep of channel widths (pitch in mels)
    plt.figure(1)
    plt.plot(melsChannels, arr, '-x')

    # Plotting visual rep of channel widths (frequency in Hz)
    plt.figure(1)
    plt.plot(freqChannels, arr, '-o')


    # initialize an array to store each channel of the inputted sound
    soundChannels = numpy.zeros(N, numpy.length(data))

    # Task 5 - Filter the sound
    # use a filter to split the noise into N channels

    for elm in range(1,N):

        #Generate Kaiser Window filter with the given bands.
        filt = getKaiserWindow(freqChannels(elm), freqChannels(elm + 1))



