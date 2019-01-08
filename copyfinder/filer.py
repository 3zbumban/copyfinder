import os
import tkinter as tk
import wave
from tkinter import filedialog

teststring = "I:\\[SAMPLES]"


def gui_get_path():
    """
    Gui to ask for target dir
    :return: selceted dir
    """
    root = tk.Tk()
    root.withdraw()
    sdir = filedialog.askdirectory()
    print(type(sdir))
    return sdir


def get_u_hash_file(wav_obj):
    """
    Get unikue hash
    :param wav_obj: benötigt wave.open obj
    :return: hash der frameliste und :return: hashesubereinzelne strings
    """
    length = wav_obj.getnframes()
    framz = []
    for i in range(0, length):
        cframe = wav_obj.readframes(i)
        framz.append(cframe.hex())
    framehash = hash(frozenset(framz))
    print("hole frames und frame hashes...")
    return frozenset(framz).__hash__(), framehash


def open_wav_f(fiel):
    """open wave in binary
    :return: wave obj
    """
    return wave.open(fiel, 'rb')


def go_dirs(t_dir=teststring):
    """
    Durch dirs gehen
    :param t_dir: target dir str
    :return: TODO
    """
    f = []
    for dirpaths, dirnames, fielnames in os.walk(t_dir):
        print(dirpaths)
        print(dirnames)
        print(fielnames)
    return f


def main():
    testf = open_wav_f("Southside Kick.wav")
    f, h = get_u_hash_file(testf)
    print(f, h)


if __name__ == '__main__':
    main()
