library IEEE;
use IEEE.std_logic_1164.all;




entity teste is end;

architecture testbench of teste is

signal i_enable_input, i_group_signal, i_enable_output : std_logic;
signal i_data_input : std_logic_vector ( 7 downto 0 );
signal i_data_output : std_logic_vector ( 2 downto 0);



begin

UTT : entity work.chip_74148 port map ( enable_input_inverted => i_enable_input, data_input_inverted => i_data_input, group_signal_inverted => i_group_signal, enable_output_inverted => i_enable_output, analogic_output_inverted => i_data_output);

process
begin

	wait for 10 ns;
	i_enable_input <= '1';
	i_data_input <= "10110111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000000";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000001";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000011";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00000111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00001111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00011111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "00111111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "01111111";
	wait for 10 ns;
	i_enable_input <= '0';
	i_data_input <= "11111111";

end process;
end testbench;
