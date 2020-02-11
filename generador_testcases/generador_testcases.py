import argparse
import random

class Generator_test():

    def imprimir_matriz(self,rows=1,columns=1,zero=0,n=1):
        a=""
        gen=[]
        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if zero == 0:
                        a+=str(random.randint(0,9))
                        if j != columns-1:
                            a+=" "
                    else:
                        a+=str(0)
                        if j != columns-1:
                            a+=" "

                if i != rows-1:
                    a+="\n"
            gen.append(a)
            a=""
            print(gen[k])
            if k != n-1:
                print("\n")

#    def imprimir_matriz(self,fmt):
#        if fmt == 'std':
#            print("Illo ")
#        elif fmt == 'iso':
#            print("HOla majo")
#        elif fmt == 'unix':
#            print("prueba")
#        elif fmt == 'tz':
#            print("Gol del borusia")


gen=Generator_test()

parser = argparse.ArgumentParser()

parser.add_argument('-f', dest='format', choices=['std', 'iso', 'unix', 'tz'],
                    help="shows datetime in given format")
parser.add_argument('-M', type=int,nargs=2,dest='matrix',help="Genera matriz nxn")

args = parser.parse_args()
fmt = args.format

try:
    a1 = int(args.matrix[0])
    a2 = int(args.matrix[1])
except TypeError as e:
    print("Error al introducir parametros")

gen.imprimir_matriz(a1,a2)
#gen.imprimir_texto(fmt)
