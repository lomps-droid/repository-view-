library IEEE;
use IEEE.std_logic_1164.all;

entity c74352 is
port(
	select_inputs : in std_logic_vector ( 1 downto 0);
	data_inputs : in std_logic_vector ( 3 downto 0);
	output_enable : in std_logic;
	output_z : out std_logic
);
end c74352;

architecture implement of c74352 is
begin
process(select_inputs, data_inputs,output_enable)
begin
if output_enable = '1' then
	output_z <= '1';
end if;
if output_enable = '0' then
	if select_inputs = "00" then
		if data_inputs(0) = '0' then
			output_z <= '1';
		elsif data_inputs(0) = '1' then
			output_z <= '0';
		end if;
	end if;
	if select_inputs = "10" then
		if data_inputs(1) = '0' then
			output_z <= '1';
		elsif data_inputs(1) = '1' then
			output_z <= '0';
		end if;
	end if;
	if select_inputs = "01" then
		if data_inputs(2) = '0' then
			output_z <= '1';
		elsif data_inputs(2) = '1' then
			output_z <= '0';
		end if;
	end if;
	if select_inputs = "11" then
		if data_inputs(3) = '0' then
			output_z <= '1';
		elsif data_inputs(3) = '1' then
			output_z <= '0';
		end if;
	end if;
end if;
		

end process;
end implement;
