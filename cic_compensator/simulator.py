import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def simulate_system(f, fir, Hcic, fs):
    """
    Simulates CIC+FIR filters response
    """
    w, h = signal.freqz(fir, worN=len(f), fs=fs)

    H_total = np.abs(Hcic * np.abs(h))

    return w, h, H_total

def plot_response(f, Hcic, h, H_total, f_pass):
    """
    Ploting the response
    """
    eps = 1e-12

    plt.figure(figsize=(10,6))
    plt.plot(f, 20*np.log10(np.abs(Hcic)+eps), label="CIC")
    plt.plot(f, 20*np.log10(np.abs(h)+eps), label="FIR")
    plt.plot(f, 20*np.log10(H_total+eps), label="CIC+FIR")

    plt.axvline(f_pass, linestyle="--", label="f_pass")

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("dB")
    plt.title("System Response")
    plt.grid()
    plt.legend()
    plt.show()

def print_stats(fir, sh_fir):
    """
    Show data from filter simulation and project.
    """
    print("-" * 30)
    print("Filter Stats")
    print("-" * 30)
    print(f"Number of Taps: {len(fir)}")
    print(f"Shift suggestion: {sh_fir}")
    print(f"DC Gain (FIR): {20 * np.log10(np.sum(fir)):.2f} dB")
    print("-" * 30)
