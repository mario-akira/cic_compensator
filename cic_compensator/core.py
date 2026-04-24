from .designer import design_fir_compensator
from .hardware import polyphase_decompose, quantize, generate_verilog
from .simulator import simulate_system, plot_response
import numpy as np

class CICFIRConfig:
    def __init__(self, R=10, N=3, M=4, taps=64, fs=100e6):
        self.R, self.N, self.M, self.taps, self.fs = R, N, M, taps, fs

class FilterManager:
    def __init__(self, config: CICFIRConfig):
        self.cfg = config
        self.fir_coeffs = None

    def build(self, f_pass, gain_db):
        f = np.linspace(0, self.cfg.fs/2, 2048)
        self.fir_coeffs, self.Hcic, self.h_fir = design_fir_compensator(self.cfg, f, f_pass, gain_db)
        return self.fir_coeffs

    def export_hardware(self, filename="fir_poly.v"):
        phases = polyphase_decompose(self.fir_coeffs, self.cfg.M)
        phases_q = quantize(phases)
        generate_verilog(phases_q, self.cfg.M, filename)

    def show_results(self, f_pass):
        f = np.linspace(0, self.cfg.fs/2, 2048)
        # h_fir aqui é o h calculado no design_fir_compensator
        w, h, H_total = simulate_system(f, self.fir_coeffs, self.Hcic, self.cfg.fs)
        plot_response(f, self.Hcic, h, H_total, f_pass)
