import scipy.io.wavfile as wav
import numpy as np
import python_speech_features.sigproc as sp
import matplotlib.pyplot as plt
from scipy import signal

def audioread(input_filename, preemph_coeff = 0.95):
    ##### reading file
    (fs,signal) = wav.read(input_filename)
    #print("Sampling frequency = %d" %(fs))
    
    if signal.dtype == 'int16':
        nb_bits = 16 # -> 16-bit wav files
    elif signal.dtype == 'int32':
        nb_bits = 32 # -> 32-bit wav files
    
    max_nb_bit = float(2 ** (nb_bits - 1))
    samples = signal / (max_nb_bit + 1.0)
    
    ### normalizing 
    maximum = np.max(np.abs(samples))  ## finding maximum value
    sig_norm = samples/maximum
    
    ### preemphasis
    sig_preemph = sp.preemphasis(sig_norm, coeff = preemph_coeff)
    return sig_preemph, fs


def extract_spectrogram(speech_signal, fs, framesize, shift, nfft, plotFlag = False):
    
    freq, time, spec = signal.spectrogram(speech_signal, fs,nperseg=framesize,noverlap=shift,nfft=nfft,mode='magnitude',scaling='spectrum')
    
    if plotFlag == True:
        cmap = plt.get_cmap('jet')
        plt.pcolormesh(time, freq, np.log(spec),cmap=cmap)

    return freq, time, spec
        
