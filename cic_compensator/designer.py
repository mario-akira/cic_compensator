import numpy as np
from scipy import signal

def cic_response(f, R, N, fs):
    f_norm = f / fs
    H = (R * np.sinc(f_norm * R) / np.sinc(f_norm))**N
    return H / np.max(H)

def design_fir_compensator(cfg, f, f_pass, gain_db):
    Hcic = cic_response(f, cfg.R, cfg.N, cfg.fs)
    H_desired = np.zeros_like(f)
    mask = f <= f_pass
    H_desired[mask] = 1 / Hcic[mask]

    fir = signal.firwin2(cfg.taps, f, H_desired, fs=cfg.fs)
    w, h = signal.freqz(fir, fs=cfg.fs)
    gain_target = 10**(gain_db / 20)
    fir = fir * (gain_target / np.max(np.abs(h)))

    return fir, Hcic, h
