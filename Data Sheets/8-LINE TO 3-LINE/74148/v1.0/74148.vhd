library IEEE;
use IEEE.std_logic_1164.all;


entity data_74148 is
port(
	enable_input_inverted : in std_logic;
	data_input_inverted : in std_logic_vector ( 7 downto 0 );
	group_signal_inverted : out std_logic;
	data_output_inverted : out std_logic_vector ( 2 downto 0 );
	enable_output_inverted : out std_logic
);
end data_74148;

architecture chip of data_74148 is

begin
process(enable_input_inverted,data_input_inverted)
begin
	if enable_input_inverted = '1' then
		group_signal_inverted <= '1';
		data_output_inverted <= "111";
		enable_output_inverted <= '1';
	end if;
	if enable_input_inverted = '0' then
		if data_input_inverted = "11111111" then
			group_signal_inverted <= '1';
			data_output_inverted <= "111";
			enable_output_inverted <= '0';
		end if;
		if data_input_inverted(0) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "000";
			enable_output_inverted <= '1';
		elsif data_input_inverted(1) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "100";
			enable_output_inverted <= '1';

		elsif data_input_inverted(2) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "010";
			enable_output_inverted <= '1';

		elsif data_input_inverted(3) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "110";
			enable_output_inverted <= '1';

		elsif data_input_inverted(4) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "001";
			enable_output_inverted <= '1';

		elsif data_input_inverted(5) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "101";
			enable_output_inverted <= '1';

		elsif data_input_inverted(6) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "011";
			enable_output_inverted <= '1';

		elsif data_input_inverted(7) = '0' then
			group_signal_inverted <= '0';
			data_output_inverted <= "111";
			enable_output_inverted <= '1';
		end if;
	end if;
end process;
end chip;