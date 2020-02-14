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
    def check_argument_list(arg):
        if len(arg) > 0:
            if arg[0] == "[" and arg[len(arg) - 1] == "]":
                aux = arg[1:-1]
                if len(aux) > 0:
                    cases = aux.split(",")
                    for i in range(len(cases)):
                        cases[i] = int(cases[i])
                    return cases

        return ""


class Generator_test:
    def imp_ristra(
        self, rows=1, columns=1, char=" ", ncar=1, tipo="", intercalado="", n=1
    ):
        a = ""
        cont = 0
        intercalado = Utiles.check_argument_list(intercalado)
        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if cont < len(intercalado):  # Mejorable
                        if intercalado[cont] == 0:
                            a += Utiles.randomnumber(ncar, 0, 9)
                        else:
                            a += Utiles.randomword(ncar)
                    else:
                        if tipo == "I":
                            a += Utiles.randomnumber(ncar, 0, 9)
                        else:
                            a += Utiles.randomword(ncar)
                    cont += 1
                    if j != columns - 1:
                        a += char
                if i != rows - 1:
                    a += "\n"
            print(a)
            a = ""

    def imp_hola(self, m):
        print(m)



gen = Generator_test()

parser = argparse.ArgumentParser()

parser.add_argument("-M", type=str, nargs="*", dest="matrix", help="Genera matriz nxn")

parser.add_argument("-g", type=str, nargs="*", dest="gen", help="Genera texto")

args = parser.parse_args()

# Cutre
if args.matrix:
    a1 = int(args.matrix[0])
    a2 = int(args.matrix[1])
    a3 = str(args.matrix[2])
    a4 = int(args.matrix[3])
    a5 = str(args.matrix[4])
    a6 = str(args.matrix[5])
    a7 = str(args.matrix[6])
    cases = Utiles.check_argument_list(a7)
    for i in cases:
        print(i)
        gen.imp_ristra(a1, a2, a3, a4, a5, a6, i)

elif args.gen:
    a1 = str(args.gen[0])
    gen.imp_hola(a1)