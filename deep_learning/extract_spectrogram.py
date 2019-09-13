import argparse
import sys
import os
from utils import audioread, extract_spectrogram
from tqdm import tqdm
import mmap
import matplotlib.pyplot as plt
import numpy as np

def main(protocolFile, datatype, wavFolder, outputFolder):
    
    #### create output directories
    dest_gen = os.path.join(outputFolder,datatype,'gen')
    dest_spoof = os.path.join(outputFolder,datatype,'spoof')

    if not os.path.exists(dest_gen):
        os.makedirs(dest_gen)
    else:
        print("Destination already exists")

    if not os.path.exists(dest_spoof):
        os.makedirs(dest_spoof)
    else:
        print("Destination already exists")
#####################################################################

    #### open the protocol file and read it line by line
    num_lines = sum(1 for line in open(protocolFile,'r'))
    fid = open(protocolFile,'r')
    for line in tqdm(fid,total = num_lines):   ### use tqdm for progress bar
        line = line.rstrip('\n').split(' ')
        waveFileName = line[0]
        label = line[1]
       
        #### read the wavefile
        waveFilePath = os.path.join(wavFolder,waveFileName)  
        [speech, fs] = audioread(waveFilePath, preemph_coeff = 0.97)


        ### create spectrograms
        framesize = int(20*(fs/1000))
        shift = int(10*(fs/1000))
        nfft = 1024
 
        [freq, time, spec] = extract_spectrogram(speech, fs, framesize, shift, nfft, plotFlag = False)

        #### plot spectrogram
        filename = waveFileName.split('.')[0]   ### remove .wav from the filename
        filename = filename + '.png'
        if label == 'genuine':
            dest_path = os.path.join(dest_gen,filename)
        else:
            dest_path = os.path.join(dest_spoof,filename)


        cmap = plt.get_cmap('jet')
        plt.pcolormesh(time, freq, np.log(spec),cmap=cmap)
        plt.axis('off')
        plt.savefig(dest_path)
        plt.close()

    
# ------------------------- __main__-------------------------------------
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='extract spectrograms')
    parser.add_argument('-pf', '--protocolFile', default=None, type=str,
                           help='path to protocolFile (default: None)')
    parser.add_argument('-t','--datatype', default = None, type = str,
                           help='train/validation/evaluation')
    parser.add_argument('-w','--wavFolder', default = None, type = str,
                          help='train/validation/evaluation')
    parser.add_argument('-o','--outputFolder', default = None, type = str,
                          help='train/validation/evaluation')
    
    args = parser.parse_args()

    if args.protocolFile is None:
        print('Protocol file name missing, provide --input argument')
        sys.exit(1)

    if args.datatype is None:
        print('Type missing, provide --datatype argument')
        sys.exit(1)
    
    if args.wavFolder is None:
        print('wavFolder missing, provide --wavFolder argument')
        sys.exit(1)

    if args.outputFolder is None:
        print('outputFolder missing, provide --outputFolder argument')
        sys.exit(1)

    main(args.protocolFile, args.datatype, args.wavFolder, args.outputFolder)
