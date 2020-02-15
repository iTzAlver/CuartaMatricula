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

    # Cutre ,creo que con argparse se puede mejorar
    @staticmethod
    def check_argument_numbers(arg):
        cont=0
        if len(arg) > 0:
            for i in arg:
                try:
                    int(i)
                except ValueError:
                    arg=arg[:cont]+"0"+arg[(cont+1):]
                cont+=1
            return arg

        return ""

    @staticmethod
    def check_argument_list(arg):
        if len(arg) > 0:
            if arg[0] == "[" and arg[len(arg) - 1] == "]":
                aux = arg[1:-1]
                if len(aux) > 0:
                    cases = aux.split(",")
                    for i in range(len(cases)):
                        try:
                            cases[i] = int(cases[i])
                        except ValueError:
                            cases[i] = ord(cases[i])
                    return cases

        return ""


class Generator_test:
    def imp_ristra(
        self, rows=1, columns=1, char=" ", ncar=1, tipo=0, intercalado="", fijado="" , n=1
    ):
        a = ""
        cont = 0
        intercalado=Utiles.check_argument_numbers(intercalado)
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
                    if cont<len(fijado):
                        if fijado[cont] != "" and fijado[cont] != "^":
                            a=a[:cont]+fijado[cont]+a[(cont+1):]

                    cont += 1
                
                    if j != columns - 1:
                        a += char
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
    a1 = int(args.matrix[0])
    a2 = int(args.matrix[1])
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

for i in a8:
    print(i)
    gen.imp_ristra(a1, a2, a3, a4, a5, a6, a7 ,int(i))
