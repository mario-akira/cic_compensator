import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def simulate_system(f, fir, Hcic, fs):
    """
    Calcula a resposta combinada CIC+FIR projetados
    """
    w, h = signal.freqz(fir, worN=len(f), fs=fs)

    H_total = np.abs(Hcic * np.abs(h))

    return w, h, H_total

def plot_response(f, Hcic, h, H_total, f_pass):
    eps = 1e-12

    plt.figure(figsize=(10,6))
    plt.plot(f, 20*np.log10(np.abs(Hcic)+eps), label="CIC")
    plt.plot(f, 20*np.log10(np.abs(h)+eps), label="FIR")
    plt.plot(f, 20*np.log10(H_total+eps), label="CIC+FIR")

    plt.axvline(f_pass, linestyle="--", label="f_pass")

    plt.xlabel("Frequência (Hz)")
    plt.ylabel("dB")
    plt.title("Resposta do sistema")
    plt.grid()
    plt.legend()
    plt.show()

def print_stats(fir, sh_fir):
    """
    Exibe informações técnicas no terminal sobre o filtro projetado.
    """
    print("-" * 30)
    print("ESTATÍSTICAS DO FILTRO")
    print("-" * 30)
    print(f"Número de Taps: {len(fir)}")
    print(f"Shift sugerido: {sh_fir}")
    print(f"Ganho DC (FIR): {20 * np.log10(np.sum(fir)):.2f} dB")
    print("-" * 30)
