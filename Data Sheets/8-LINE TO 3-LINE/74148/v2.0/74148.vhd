library IEEE;
use IEEE.std_logic_1164.all;

entity chip_74148 is
port(
	--Inputs
	enable_input_inverted : in std_logic; -- E1
	data_input_inverted : in std_logic_vector ( 7 downto 0 ); -- I0 ~ I7
	--Outputs
	group_signal_inverted : out std_logic; --GS
	analogic_output_inverted : out std_logic_vector ( 2 downto 0 ); -- A0 ~ A2
	enable_output_inverted : out std_logic --EO
	
);
end chip_74148;


architecture data_chip of chip_74148 is
begin
process(enable_input_inverted, data_input_inverted)
begin
if ( enable_input_inverted = '1') then

	group_signal_inverted <= '1';
	analogic_output_inverted <= "111";
	enable_output_inverted <= '1';
end if;
if ( enable_input_inverted = '0') then
	if (data_input_inverted = "11111111") then
		group_signal_inverted <= '1';
		analogic_output_inverted <= "111";
		enable_output_inverted <= '0';
	end if;
	
	for i in 0 to 7 loop
		if (data_input_inverted(i) = '0') then
			group_signal_inverted <= '0';
			enable_output_inverted <= '1';
			if i = 0 then analogic_output_inverted <= "000";
			elsif i = 1 then analogic_output_inverted <= "100";
			elsif i = 2 then analogic_output_inverted <= "010";
			elsif i = 3 then analogic_output_inverted <= "110";
			elsif i = 4 then analogic_output_inverted <= "001";
			elsif i = 5 then analogic_output_inverted <= "101";
			elsif i = 6 then analogic_output_inverted <= "011";
			elsif i = 7 then analogic_output_inverted <= "111";
			end if;
			exit;
		end if;
	end loop;
end if;
end process;
end data_chip;
