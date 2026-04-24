from cic_compensator import FilterManager, CICFIRConfig

def main():
    # 1. Configurar os parâmetros (conforme seu código original)
    cfg = CICFIRConfig(
        R=25, 
        N=12, 
        M=4, 
        taps=72, 
        fs=100e6
    )
    
    # 2. Inicializar o Gerenciador
    manager = FilterManager(cfg)
    
    # 3. Projetar o filtro
    print("Projetando o filtro...")
    f_pass = 500e3
    gain_db = 3
    coeffs = manager.build(f_pass=f_pass, gain_db=gain_db)
    
    print(f"Filtro gerado com {len(coeffs)} coeficientes.")

    # 4. Simular e mostrar resultados (abre o gráfico)
    print("Abrindo simulação...")
    manager.show_results(f_pass=f_pass)

    # 5. Exportar o Verilog
    print("Gerando hardware...")
    manager.export_hardware("filtro_teste.v")
    print("Sucesso! Verifique o arquivo filtro_teste.v")

if __name__ == "__main__":
    main()
