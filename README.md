# CIC + FIR Filter Design Tool
---
## 📖 Overview
This project aims to study Python library creation.  
The tool assists in **designing and simulating multi-phase FIR compensation filters** for CIC filters.  

It allows you to:
- Parameterize the CIC filter design.  
- Design the corresponding FIR filter.  
- Simulate the designed filters.  
- Automatically generate a **Verilog** file with the designed filter.

---

## 🚀 Features
- Parametric CIC filter definition.  
- Automatic FIR compensation filter design.  
- Simulation of designed filters.  
- Export to Verilog code.  

---

## 📂 Project Structure
```
cic_compensator/
├── cic_compensator/         # source folder
│   ├── __init__.py          # init file
│   ├── core.py              # core for the system
│   ├── designer.py          # calculator for filters
│   ├── simulator.py         # simulator for filters
│   └── hardware.py          # verilog code generator
├── pyproject.toml           # dependencies
└── README.md                # guide file
```
---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
```


