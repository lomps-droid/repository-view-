library IEEE;
use IEEE.std_logic_1164.all;

entity main_project is
port(
	-- Input
	sel : in std_logic_vector ( 2 downto 0 ); -- s0, s1 , s2
	enable : in std_logic; -- E , |E
	position : in std_logic_vector ( 7 downto 0 ); -- e0 , e1 ... e7
	--Output 
	z , z_invertido : out std_logic
	);
end main_project;

architecture implementar of main_project is
begin
process(sel, enable)
begin
	if not enable = '0' then
		if sel = "000" then
			z <= position(0);
			z_invertido <= not position(0);
		elsif sel = "001" then
			z <= position(1);
			z_invertido <= not position(1);
		elsif sel = "010" then
			z <= position(2);
			z_invertido <= not position(2);
		elsif sel = "011" then
			z <= position(3);
			z_invertido <= not position(3);
		elsif sel = "100" then
			z <= position(4);
			z_invertido <= not position(4);
		elsif sel = "101" then
			z <= position(5);
			z_invertido <= not position(5);
		elsif sel = "110" then
			z <= position(6);
			z_invertido <= not position(6);
		elsif sel = "111" then
			z <= position(7);
			z_invertido <= not position(7);
		end if;
	elsif not enable = '1' then
		z <= '0';
		z_invertido <= '1';
	end if;
end process;
end implementar;