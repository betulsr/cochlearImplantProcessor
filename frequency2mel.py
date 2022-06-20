import numpy as numpy

def frequency2mel(freq):
    k = int()
    if k.size == 0:
        k = 1000 / numpy.log(1 + 1000 / 700) # 1127.01048
    af = abs(freq)
    mel = numpy.sign(freq)* numpy.log(1 + af / 700) * k
    mr = (700 + af) / k

    return [mel, mr]
