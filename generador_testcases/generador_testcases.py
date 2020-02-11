import argparse
import random
import string
import sys

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class Generator_test():

    def imprimir_matriz(self,rows=1,columns=1,n=1,zero=False):
        a=""
        gen=[]
        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if zero==False:
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

    def imprimir_ristra(self,rows,ncar,nveces=1,word=False,zero=False):
        text=""
        gen=[]
        for k in range(nveces):
            if nveces>1:
                print(str(rows))
            for i in range(rows):
                if word!=False:
                    text+=randomword(ncar)
                else:
                    if zero==False:
                        for j in range(ncar):
                            text+=str(random.randint(0,9))
                    else:
                        text+=str(0)*ncar
                        text+="\n" 
                gen.append(text)
                text=""
                print(gen[i])
            gen.clear()

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
parser.add_argument('-M', type=int,nargs='*',dest='matrix',help="Genera matriz nxn")

parser.add_argument('-g', type=int,nargs='*',dest='gen',help="Genera texto")

args = parser.parse_args()
fmt = args.format

#Cutre
if args.matrix:
    a1 = int(args.matrix[0])
    a2 = int(args.matrix[1])
    a3 = int(args.matrix[2])
    a4 = int(args.matrix[3])
    gen.imprimir_matriz(a1,a2,a3,a4)
elif args.gen:
    a1 = int(args.gen[0])
    a2 = int(args.gen[1])
    a3 = int(args.gen[2])
    a4 = int(args.gen[3])
    a5 = int(args.gen[4])
    gen.imprimir_ristra(a1,a2,a3,a4,a5)


