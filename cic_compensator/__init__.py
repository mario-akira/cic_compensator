# Importa as classes e funções principais dos módulos internos
from .core import FilterManager, CICFIRConfig
from .designer import design_fir_compensator, cic_response
from .hardware import generate_verilog, polyphase_decompose, quantize
from .simulator import simulate_system, plot_response

# Define a versão da biblioteca
__version__ = "0.1.0"

# Opcional: Define o que será importado ao usar "from cic_compensator import *"
__all__ = [
    "FilterManager",
    "CICFIRConfig",
    "design_fir_compensator",
    "generate_verilog",
    "plot_response"
]
