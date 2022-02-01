import slab
from matplotlib import pyplot as plt
import pathlib
import os

DIR = pathlib.Path(os.getcwd())

file_category = 'pinknoise_short'

filepath = DIR / 'samples' / file_category / 'a_weighted'

filenames = ['AW_A_pinknoise_0.wav',
             'AW_A_pinknoise_0_1m.wav',
             'AW_A_pinknoise_0_2m.wav',
             'AW_A_pinknoise_0_4m.wav',
             'AW_A_pinknoise_0_8m.wav',
             'AW_A_pinknoise_0_16m.wav']
threshs = []
for filename in filenames:
    stimulus = slab.Binaural(filepath / filename)
    stairs = slab.Staircase(start_val=50, n_reversals=18)
    print(f'Starting staircase with {filename}')
    for level in stairs:
        stimulus.level = level
        stairs.present_tone_trial(stimulus)
    threshs.append(stairs.threshold())
    print(f'Threshold for {filename} Hz: {stairs.threshold()} dB')