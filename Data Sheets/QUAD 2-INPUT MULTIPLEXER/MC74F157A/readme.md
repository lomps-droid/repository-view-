# MC74F157A
The MC74F157A is a high-speed quad 2-input multiplexer. Four bits of data from two sources can be selected using the common Select and Enable inputs.

The four buffered outputs present the selected data in the true (non-inverted) form. 

The F157A can also be used to generate any four of the 16 different functions to two variables.

# How we make this code

Well , first we read the Truth Table and we incorporate in lines:

```
(s0 = '1' and i1 = '0' )
(s0 = '1' and i1 = '1' )
(s0 = '0' and i0 = '0' )
(s0 = '0' and i0 = '1' )

```

<img src="https://i.imgur.com/kzbXca0.png">



## Images
Simulator download: https://github.com/hneemann/Digital


<img src="https://i.imgur.com/wqxswCQ.png" alt="Simulator" width="640px" height="480px">
