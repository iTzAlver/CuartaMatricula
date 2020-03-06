import argparse
import random
import string
import subprocess
import os

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

    @staticmethod
    def read_file(rutatexto=""):
        f = open(os.getcwd()+"\\"+ rutatexto, "r")
        t=""
        while(True):
            linea = f.readline()
            if not linea:
                break
            t+=linea
        f.close()
        return t
        

class Generator_test:
    def imp_ristra(self, rows, columns, char=" ", ncar=1, inicioint="0" , finalint="0" , fijado="" , inicionf="0" , finalnf="0" , nofijado="0" , n=1):
        a = ""
        texto = ""
        b=0
        ind1=0
        contc = 1
        contf = 1
        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if (contc >= int(inicioint) and contc <= int(finalint)) or args.t == False:  
                        a += Utiles.randomnumber(ncar, 0, 9)
                    else:
                        a += Utiles.randomword(ncar)
                    if j != columns - 1:
                        a += char
                    if len(fijado)>0 and ind1<len(fijado): 
                        if (contc >= int(inicionf) and contc <=int(finalnf)) and (str(contf) not in nofijado):
                            if fijado != "" and fijado[ind1] != "^" :
                                a=a[:b]+fijado[ind1]+a[(b+1):]
                            ind1+=1
                    b+=(1+len(char))
                    contc += 1
                if i != rows - 1:
                    a += "\n"
                    b = len(a)
                contc=1
                ind1 = 0
                contf+=1

            texto+=a
            if k < n-1:
                texto+="\n"
            a = ""
            b=0
        return texto


gen = Generator_test()

parser = argparse.ArgumentParser()

parser.add_argument("-M", type=str, nargs=3, dest="matrix", help="Genera matriz nxn")
parser.add_argument("--t", help='Cambia numeros por caracteres',action="store_true")
parser.add_argument("-f", type=str, nargs=1, dest="ejecuta", help='Crea un subproceso del ejecutable con el que se quieren probar los casos')
parser.add_argument("-fno", type=str, nargs=2, dest="ejecuta_casos_externos", help='Crea un subproceso del ejecutable ,pero se alimenta con casos externos')
parser.add_argument("-fij", type=str, nargs="*", dest="fijado", help='Fijado de caracteres en algunas posiciones')
parser.add_argument("-no", type=str, nargs=1,dest="nfijado",help='Fijado de caracteres en algunas posiciones')
parser.add_argument("-int", type=str, nargs="*", dest="intercalado", help='Elige que posiciones son caracteres o numeros')
parser.add_argument("--nonl", help="No imprime el nº ronda",action="store_true")
parser.add_argument("--nonc", help="No imprime el nº columnas",action="store_true")
parser.add_argument("--invn", help="Invierte el orden de los mensajes nº ronda nº columna",action="store_true")
parser.add_argument("-n", type=str, nargs=1, dest="size", help='Numero de lineas')
parser.add_argument("-nchar", type=int, nargs=1, dest="nchar", help='Numero de caracteres por columna')

args = parser.parse_args()

if args.ejecuta_casos_externos:
    ruta=args.ejecuta_casos_externos[0]
    rutatexto=args.ejecuta_casos_externos[1]
    t=Utiles.read_file(rutatexto)
    p = subprocess.run([os.getcwd()+"\\"+ ruta],text=True, input=t)


elif args.matrix:
    a1 = Utiles.check_argument_list(args.matrix[0])
    a2 = Utiles.check_argument_list(args.matrix[1])
    a3 = args.matrix[2]
    a4 = 1
    a5="0"
    a6="0"
    a7=""
    a8=""
    a9=""
    a10=""
    a11=[1]

    if args.nchar:
        a4 = int(args.nchar[0])

    if args.intercalado: 
        a5 = str(args.intercalado[0])
        a6 = a5
        if(len(args.intercalado) == 2):
            a6 = str(args.intercalado[1])    

    if args.fijado:
        a7 = str(args.fijado[0])
        if(len(args.fijado) == 2):
            a8 = str(args.fijado[1])
            a9 = a8
        if(len(args.fijado) ==3):
            a8 = str(args.fijado[1])
            a9 = str(args.fijado[2])
            if(args.nfijado):
                a10 = str(args.nfijado[0]) 

    if args.size:
        a11 = str(args.size[0]) 
        a11=Utiles.check_argument_list(a11)

    cuentar=0
    cuentac=0
    inv=False
    cuenta=min(len(a1)-1,len(a2)-1)
    texto_a_ejecutar=""
    for i in a11:
        if args.invn == True:
            print(a2[cuentar])
            print(i)
            inv=True
        if args.nonl == False and not inv:
            print(i)
        if args.nonc == False and not inv:
            print(a2[cuentar])
        text=gen.imp_ristra(a1[cuentar], a2[cuentac], a3, a4, a5, a6, a7 , a8 , a9 , a10 , int(i))
        print(text)
        if(cuentar<cuenta):
            cuentar+=1
        if(cuentac<cuenta):
            cuentac+=1
        texto_a_ejecutar+=text

    if args.ejecuta:
        ruta=args.ejecuta[0]
        p = subprocess.run([os.getcwd()+"\\"+ ruta],text=True, input=texto_a_ejecutar)
