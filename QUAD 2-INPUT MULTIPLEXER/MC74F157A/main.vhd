library IEEE;
use IEEE.std_logic_1164.all;

entity main_project is
port(
	e1, s0 , i0,i1 : in std_logic;
	z : out std_logic
);
end main_project;

architecture implement of main_project is
begin
	process(e1, s0 , i0,i1)
	begin
	if not e1 = '0' then
		if (s0 = '1' and i1 = '0' ) then
			z <= '0';
		elsif (s0 = '1' and i1 = '1' ) then
			z <= '1';
		elsif (s0 = '0' and i0 = '0' ) then
			z <= '0';
		elsif (s0 = '0' and i0 = '1' ) then
			z <= '1';
		end if;
	else --If |E1 = High Voltage Level ( 1 ) the values S, i0 and i1 don't care.
		z <= '0';
	end if;
	end process;
end implement;