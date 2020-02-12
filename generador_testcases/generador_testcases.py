import argparse
import random
import string
import sys

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class Generator_test():

    def imprimir_ristra(self,rows=1,columns=1,char=" ",ncar=1,n=1,word=False,zero=False):
        a=""
        for k in range(n):
            print(n)
            for i in range(rows):
                for j in range(columns):
                    if word == False:
                        if zero==False:
                            for l in range(ncar):
                                a+=str(random.randint(0,9))
                            if j != columns-1:
                                a+=char
                        else:
                            a+=str(0)
                            if j != columns-1:
                                a+=char
                    else:
                        a+=randomword(ncar)
                        if j != columns-1:
                            a+=char

                if i != rows-1:
                    a+="\n"
            print(a)
            a=""


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

parser.add_argument('-M', type=str,nargs='*',dest='matrix',help="Genera matriz nxn")

#parser.add_argument('-g', type=int,nargs='*',dest='gen',help="Genera texto")
#parser.add_argument('-f', dest='format', choices=['std', 'iso', 'unix', 'tz'],help="shows datetime in given format")

args = parser.parse_args()
#fmt = args.format

#Cutre
if args.matrix:
    a1 = int(args.matrix[0])
    a2 = int(args.matrix[1])
    a3 = str(args.matrix[2])
    a4 = int(args.matrix[3])
    a5 = int(args.matrix[4])
    a6 = int(args.matrix[5])
    gen.imprimir_ristra(a1,a2,a3,a4,a5,a6)

