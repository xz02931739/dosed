import h5py
import numpy as np
from matplotlib import pyplot as plt


file = './tests/test_files/h5/23c61485-a9a5-478b-8115-f34b883876b8.h5'

## check the structure of the file
with h5py.File(file, 'r') as f:
    print(f.keys())
    ## ['eeg_0', 'eeg_1', 'spindle'] as the keys

    ## check the structure of the eeg_0 dataset
    print(f['eeg_0'])
    ## <HDF5 dataset "eeg_0": shape (1000,), dtype "<f8">
    ## get the data from the dataset
    eeg_0_data = f['eeg_0'][:]
    
    ## check the structure of the spindle dataset
    print(f['spindle'])
    ## there are 2 members in the spindle dataset
    print(f['spindle'].keys())
    ## ['duration', 'start']

    ## get the data from the spindle dataset
    spindle_duration = f['spindle']['duration'][:]
    spindle_start = f['spindle']['start'][:]

    print(spindle_duration.shape, spindle_start.shape)

    print(spindle_duration[:10])
    print(spindle_start[:10])


    k0 = f['spindle/duration']
    print(k0.shape, k0.dtype)