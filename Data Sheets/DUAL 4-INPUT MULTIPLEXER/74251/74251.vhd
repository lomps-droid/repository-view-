library IEEE;
use IEEE.std_logic_1164.all;

entity main is
port(
	OE : in std_logic;
	selects : in std_logic_vector ( 2 downto 0 );
	position_switch : in std_logic_vector ( 7 downto 0 );
	z : out std_logic;
	z_invert : out std_logic
);
end main;

architecture main_arch of main is
begin
process(OE, selects,position_switch)
begin
if not OE = '1' then
	if selects = "---" then
		z <= 'Z';
		z_invert <= 'Z';
	end if;
end if;
if not OE = '0' then
	if selects = "LLL" then
		z <= position_switch(0);
		z_invert <= not position_switch(0);
	elsif selects = "LLH" then
		z <= position_switch(1);
		z_invert <= not position_switch(1);
	elsif selects = "LHL" then
		z <= position_switch(2);
		z_invert <= not position_switch(2);
	elsif selects = "LHH" then
		z <= position_switch(3);
		z_invert <= not position_switch(3);
	elsif selects = "HLL" then
		z <= position_switch(4);
		z_invert <= not position_switch(4);
	elsif selects = "HLH" then
		z <= position_switch(5);
		z_invert <= not position_switch(5);
	elsif selects = "HHL" then
		z <= position_switch(6);
		z_invert <= not position_switch(6);
	elsif selects = "HHH" then
		z <= position_switch(7);
		z_invert <= not position_switch(7);
	end if;
end if;
end process;
end main_arch;