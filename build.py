import os

os.system("f2py -c wavespectra/specpart/specpart.f90 wavespectra/specpart/specpart.pyf -m wavespectra.specpart")
