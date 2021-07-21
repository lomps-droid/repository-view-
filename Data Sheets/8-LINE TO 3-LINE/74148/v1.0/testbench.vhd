library IEEE;
use IEEE.std_logic_1164.all;

entity testbench is end;


architecture test of testbench is

signal i_enable_input, i_group_signal, i_enable_output : std_logic;
signal i_data_input : std_logic_vector ( 7 downto 0 ) := "00000000";
signal i_data_output : std_logic_vector ( 2 downto 0);

signal enable_input : std_logic := '1';
signal data_input : std_logic_vector ( 7 downto 0 ) := "11111111";

begin

UTT : entity work.data_74148 port map ( enable_input_inverted => i_enable_input, data_input_inverted => i_data_input, group_signal_inverted => i_group_signal, enable_output_inverted => i_enable_output, data_output_inverted => i_data_output);

estimulo : process
begin
	wait for 10 ns;
	i_enable_input <= '1';
	i_data_input <= "10110111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000000";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000001";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000011";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00001111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00011111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00111111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "01111111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "01001110";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "11111111";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait for 10 ns;
	--clear
	i_enable_input <= '0';
	i_data_input <= "00000000";
	enable_input <= not i_enable_input;
	data_input <= not i_data_input;
	wait;
end process;
end test;
	
	