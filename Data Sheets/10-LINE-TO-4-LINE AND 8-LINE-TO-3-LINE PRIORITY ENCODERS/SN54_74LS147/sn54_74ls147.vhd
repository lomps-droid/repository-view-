library IEEE;
use IEEE.std_logic_1164.all;


entity nome is
port(
entrada : in std_logic_vector ( 8 downto 0 );
D,C,B,A : out std_logic
);
end nome;

architecture expressao of nome is 
begin
process(entrada)
begin
    --entrada <= "111111111";
    D <= '0' when entrada(8) = '0' else
        '0' when entrada(7) = '0' else
        '1' when entrada(6) = '0' else
        '1' when entrada(5) = '0' else
        '1' when entrada(4) = '0' else
        '1' when entrada(3) = '0' else
        '1' when entrada(2) = '0' else
        '1' when entrada(1) = '0' else
        '1' when entrada(0) = '0';

    C <= '1' when entrada(8) = '0' else
        '1' when entrada(7) = '0' else
        '0' when entrada(6) = '0' else
        '0' when entrada(5) = '0' else
        '0' when entrada(4) = '0' else
        '0' when entrada(3) = '0' else
        '1' when entrada(2) = '0' else
        '1' when entrada(1) = '0' else
        '1' when entrada(0) = '0';

    B <= '1' when entrada(8) = '0' else
        '1' when entrada(7) = '0' else
        '0' when entrada(6) = '0' else
        '0' when entrada(5) = '0' else
        '1' when entrada(4) = '0' else
        '1' when entrada(3) = '0' else
        '0' when entrada(2) = '0' else
        '0' when entrada(1) = '0' else
        '1' when entrada(0) = '0';

    A <= '0' when entrada(8) = '0' else
        '1' when entrada(7) = '0' else
        '0' when entrada(6) = '0' else
        '1' when entrada(5) = '0' else
        '0' when entrada(4) = '0' else
        '1' when entrada(3) = '0' else
        '0' when entrada(2) = '0' else
        '1' when entrada(1) = '0' else
        '0' when entrada(0) = '0';
end process;
end expressao;