library IEEE;
use IEEE.std_logic_1164.all;


entity nome is
port(
ativar : in std_logic_vector ( 5 downto 0 );
-- GL = ativar(0)
-- g1 = ativar(1)
-- g2 = ativar (2)
y0,y1,y2,y3,y4,y5,y6,y7 : out std_logic
);
end nome;

architecture nome_da_archi of nome is
begin
process(ativar)
begin
if ativar(2) = '1' then 
y0<='1';y1<='1';y2<='1';y3<='1';y4<='1';y5<='1';y6<='1';y7<='1';
end if;
if ativar(1) = '0' then y0<='1';y1<='1';y2<='1';y3<='1';y4<='1';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010000" then y0<='0';y1<='1';y2<='1';y3<='1';y4<='1';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010001" then y0<='1';y1<='0';y2<='1';y3<='1';y4<='1';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010010" then y0<='1';y1<='1';y2<='0';y3<='1';y4<='1';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010011" then y0<='1';y1<='1';y2<='1';y3<='0';y4<='1';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010100" then y0<='1';y1<='1';y2<='1';y3<='1';y4<='0';y5<='1';y6<='1';y7<='1';end if;
if ativar = "010101" then y0<='1';y1<='1';y2<='1';y3<='1';y4<='1';y5<='0';y6<='1';y7<='1';end if;
if ativar = "010110" then y0<='1';y1<='1';y2<='1';y3<='1';y4<='1';y5<='1';y6<='0';y7<='1';end if;
if ativar = "010111" then y0<='1';y1<='1';y2<='1';y3<='1';y4<='1';y5<='1';y6<='1';y7<='0';end if;



end process;
end nome_da_archi;