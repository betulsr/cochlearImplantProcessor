import numpy as numpy

def mel2frequency(mel):
    k = int()
    if k.size == 0:
        k = 1000 / numpy.log(1 + 1000 / 700) # 1127.01048

    freq = 700 * numpy.sign(mel)*(numpy.exp(abs(mel) / k) - 1)
    mr = (700 + abs(freq)) / k

    return [freq, mr]


