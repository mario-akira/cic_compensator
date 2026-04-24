import numpy as np

def polyphase_decompose(h, M):
    phases = []
    for k in range(M):
        phases.append(h[k::M])
    return phases

def quantize(phases, bits=16):
    scale = 2**(bits-1)
    return [np.round(p * scale).astype(int) for p in phases]

def generate_verilog(phases, M, filename="fir_poly.v"):
    def generate_verilog(phases, M, filename="fir_poly.v"):
    taps = len(phases[0])
    WIDTH = 16

    with open(filename, "w") as f:

        f.write(f"""
module fir_polyphase (
    input clk,
    input rst,
    input signed [{WIDTH-1}:0] x_in,
    input valid_in,
    output reg signed [{WIDTH-1}:0] y_out,
    output reg valid_out
);

reg signed [{WIDTH-1}:0] x [0:{taps-1}];
integer i;
""")

        # coeficientes
        for p, phase in enumerate(phases):
            f.write(f"\n// Fase {p}\n")
            f.write(f"reg signed [{WIDTH-1}:0] h{p}[0:{taps-1}];\n")
            f.write("initial begin\n")
            for i, c in enumerate(phase):
                f.write(f"    h{p}[{i}] = 16'h{c};\n")
            f.write("end\n")

        f.write(f"""
reg [{int(np.ceil(np.log2(M)))-1}:0] phase;

always @(posedge clk) begin
    if (rst)
        phase <= 0;
    else if (valid_in)
        phase <= phase + 1;
end

reg signed [31:0] acc;

always @(*) begin
    acc = 0;
    case(phase)
""")

        for p in range(M):
            f.write(f"{p}: begin\n")
            for i in range(taps):
                f.write(f"    acc = acc + x[{i}] * h{p}[{i}];\n")
            f.write("end\n")

        f.write("""
    endcase
end
""")

        f.write(f"""
always @(posedge clk) begin
    if (rst) begin
        valid_out <= 0;
        y_out <= 0;
    end else if (valid_in) begin

        x[0] <= x_in;
        for (i = 1; i < {taps}; i = i + 1)
            x[i] <= x[i-1];

        if (phase == {M-1}) begin
            y_out <= acc[30:15];
            valid_out <= 1;
        end else
            valid_out <= 0;
    end
end

endmodule
""")

    print(f"Verilog gerado: {filename}")
