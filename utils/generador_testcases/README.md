Generador de TestCases

Ejemplo:

python generador_testcases.py -M 1 10 "" 1 1


Flag -M:

Primer  argumento  : filas

Segundo argumento  : columnas

Tercer  argumento  : espacio entre caracter y caracter

Cuarto  argumento  : número de caracteres entre espacios

Quinto  argumento  : Todo 0->números 1->caracteres


Flag -i:

Con el flag -i los ceros indican que en la posicion que ocupan se genere un número y los unos que se genere un caracter.
Ejemplo:
python generador_testcases.py -M 1 10 "" 1 1 -i "01000"

1
9b284wqdff

La segunda posicion se establece un caracter la primera tercera cuarta y quinta numeros.



Flag -f:

con el flag -f se fija el simbolo escrito en las posiciones que ocupan salvo el caracter ^ que no modifica la posicion.
Ejemplo:
python generador_testcases.py -M 1 10 "" 1 1 -f "A^0AA"

1
Ab0AAqaset  

La primra tercera y cuarta posicion tienen los valores A 0 A A respectivamente la segunda un caracter al azar




Flag -n:

Numero de testcases por ronda
Ejemplo:
python generador_testcases.py -M 1 10 "" 1 1 -n "[1,2,1]"

1
agbbtijmnr
2
yxxjfnrurv
vndcxwapfw
1
lczcwmrjhy




Ejemplo global:
python generador_testcases.py -M 1 10 "" 1 1 -f "0" -i "^A" -n "[4,1]"

4
09jfzdquju
08fzpemwvg
09xkxkpapa
04kkctkxpv
1
08zznofwfh



