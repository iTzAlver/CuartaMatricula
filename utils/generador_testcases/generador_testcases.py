import argparse
import random
import string


class Utiles:
    @staticmethod
    def randomword(length):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(length))

    @staticmethod
    def randomnumber(length, i1, i2):
        return "".join(str(random.randint(i1, i2)) for i in range(length))

    @staticmethod
    def check_argument_list(arg):
        aux=[]
        if len(arg) > 0:
            if arg[0] == "[" and arg[len(arg) - 1] == "]":
                aux = arg[1:-1]
                if len(aux) > 0:
                    cases = aux.split(",")
                    for i in range(len(cases)):
                            cases[i] = int(cases[i])
                    return cases
            else:
                try:
                    a=int(arg)
                except ValueError:
                    a=0

                aux.append(a)
    
        return aux

class Generator_test:
    def imp_ristra(
        self, rows, columns, char=" ", ncar=1, tipo=0, intercalado="", fijado="" , n=1
    ):
        a = ""
        b=0
        cont = 0
        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if cont < len(intercalado):  # Mejorable
                        if int(intercalado[cont]) == 0:
                            a += Utiles.randomnumber(ncar, 0, 9)
                        else:
                            a += Utiles.randomword(ncar)
                    else:
                        if tipo == 0:
                            a += Utiles.randomnumber(ncar, 0, 9)
                        else:
                            a += Utiles.randomword(ncar)
 
                    if j != columns - 1:
                        a += char

                    if cont<len(fijado):
                        if fijado[cont] != "" and fijado[cont] != "^" :
                            a=a[:b]+fijado[cont]+a[(b+1):]
                        b+=(1+len(char))

                    cont += 1

                cont=0
                if i != rows - 1:
                    a += "\n"

            print(a)
            a = ""

gen = Generator_test()

parser = argparse.ArgumentParser()

parser.add_argument("-M", type=str, nargs=5, dest="matrix", help="Genera matriz nxn")

parser.add_argument('-i', type=str, nargs=1, dest="intercalado", help='intercalado')

parser.add_argument('-f', type=str, nargs=1, dest="fijado", help='fijado')

parser.add_argument('-n', type=str, nargs=1, dest="size", help='n lineas')


args = parser.parse_args()


if args.matrix:
    a1 = str(args.matrix[0])
    a2 = str(args.matrix[1])
    a3 = str(args.matrix[2])
    a4 = int(args.matrix[3])
    a5 = int(args.matrix[4])
    a6=""
    a7=""
    a8=[1]

if args.intercalado: 
    a6 = str(args.intercalado[0])
if args.fijado:
    a7 = str(args.fijado[0])

if args.size:
    a8 = str(args.size[0]) 
    a8=Utiles.check_argument_list(a8)

cuentar=0
cuentac=0
a1=Utiles.check_argument_list(a1)
a2=Utiles.check_argument_list(a2)
for i in a8:
    print(i)
    gen.imp_ristra(a1[cuentar], a2[cuentac], a3, a4, a5, a6, a7 ,int(i))
    if(cuentar<len(a1)-1):
        cuentar+=1
    if(cuentac<len(a2)-1):
        cuentac+=1
