# Importing files
from .core import FilterManager, CICFIRConfig
from .designer import design_fir_compensator, cic_response
from .hardware import generate_verilog, polyphase_decompose, quantize
from .simulator import simulate_system, plot_response


__version__ = "0.1.0"


__all__ = [
    "FilterManager",
    "CICFIRConfig",
    "design_fir_compensator",
    "generate_verilog",
    "plot_response"
]
