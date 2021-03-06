def getKaiserWindow(pass1, pass2):
    Fstop1 = pass1 - 60 # first stopband frequency
    Fpass1 = pass1 # First Passband Frequency
    Fpass2 = pass2 # Second Passband Frequency
    Fstop2 = pass2 + 60 # Second Stopband Frequency
    Astop1 = 60 # First Stopband Attenuation (dB)
    Apass  = 1 # Passband Ripple (dB)
    Astop2 = 60 # Second Stopband Attenuation (dB)
    Fs     = 16000 # Sampling Frequency

# h = fdesign.bandpass('fst1,fp1,fp2,fst2,ast1,ap,ast2', Fstop1, Fpass1, ...
#     Fpass2, Fstop2, Astop1, Apass, Astop2, Fs);
#
# Hd = design(h, 'kaiserwin');