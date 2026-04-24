import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def simulate_system(f, fir, Hcic, fs):
    """
    Calcula a resposta combinada do sistema.
    """
    # worN=len(f) garante que o vetor h tenha o mesmo tamanho que f e Hcic
    w, h = signal.freqz(fir, worN=len(f), fs=fs)
    
    # Cálculo da magnitude combinada
    H_total = np.abs(Hcic * np.abs(h))
    
    return w, h, H_total

def plot_response(f, Hcic, h_fir, H_total, f_pass):
    """
    Gera o gráfico comparativo das respostas em frequência.
    """
    eps = 1e-12  # Evita log10(0)

    plt.figure(figsize=(10, 6))
    
    # Plot das magnitudes em dB
    plt.plot(f, 20 * np.log10(np.abs(Hcic) + eps), label="Resposta CIC", linewidth=1.5)
    plt.plot(f, 20 * np.log10(np.abs(h_fir) + eps), label="Resposta FIR (Compensador)", linewidth=1.5)
    plt.plot(f, 20 * np.log10(H_total + eps), label="Sistema Total (CIC + FIR)", color='black', fontweight='bold')

    # Linha vertical indicando a frequência de passagem
    plt.axvline(f_pass, color='red', linestyle="--", alpha=0.7, label=f"f_pass ({f_pass/1e3:.1f} kHz)")

    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Análise de Compensação CIC-FIR")
    plt.grid(True, which="both", linestyle='--', alpha=0.5)
    plt.legend()
    
    # Limita o eixo Y para melhor visualização se necessário
    plt.ylim([-100, 10]) 
    
    plt.tight_layout()
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
