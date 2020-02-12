import argparse
import random
import string

class Utiles():
    @staticmethod
    def randomword(length):
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def reconocer_ristra(t_input):
        l_input=[]
        for i in t_input:
            l_input.append(ord(i))
        return l_input

class Generator_test():

    def imp_ristra(self,rows=1,columns=1,char=" ",ncar=1,n=1,word=False,zero=False):
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
                        a+=Utiles.randomword(ncar)
                        if j != columns-1:
                            a+=char

                if i != rows-1:
                    a+="\n"
            print(a)
            a=""
        
    def imp_ristra_reconocida(self,m):
        lista_char=Utiles.reconocer_ristra(m)
        for i in lista_char:
            print(i)


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

parser.add_argument('-M',type=str,nargs='*',dest='matrix',help="Genera matriz nxn")

parser.add_argument('-g',type=str,nargs='*',dest='gen',help="Genera texto")
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
    gen.imp_ristra(a1,a2,a3,a4,a5,a6)
elif args.gen:
    a1 = str(args.gen[0])
    gen.imp_ristra_reconocida(a1)

