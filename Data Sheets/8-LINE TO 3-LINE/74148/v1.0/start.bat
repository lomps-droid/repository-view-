ghdl -a 74148.vhd
ghdl -a testbench.vhd

ghdl -e testbench

ghdl -r  testbench --vcd=74148.vcd

gtkwave 74148.vcd