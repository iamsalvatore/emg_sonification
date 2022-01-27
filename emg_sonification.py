import simpleaudio as sa
import numpy as np
from pathlib import Path
import pandas as pd


def import_audio(file):
    emg_data=pd.read_csv(file, sep=",")
    channel1_data = emg_data[emg_data.columns[0]]

    return channel1_data

def emg_sonification(channel1_data):
    sample_rate = 44100
    audio = np.array(channel1_data)
    audio *= 32767 / max(abs(audio))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()
    return play_obj


def main():
    file = Path('/Users/salvatoreesposito/Downloads/emg.csv')
    channel1_data = import_audio(file)
    emg_sonification(channel1_data)