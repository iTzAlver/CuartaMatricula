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
        

def imp_ristra(rows, columns, char, ncar, inicioint, finalint, fijado, iniciof, lineanofijada, idiagp, idiags, n):
    a = ""
    texto = ""
    indf=0
    contp=[]
    conts=idiags
    for i in range(len(idiagp)):
        if idiagp[i]< columns:
            contp.append(idiagp[i])
    
    notf=False
    for k in range(n):
        for i in range(rows):
            for j in range(columns):

                if(fijado != "" and indf<len(fijado)):
                    if((j+1 >= int(iniciof)) and (str(i) not in lineanofijada)) and (((j in contp) or (j in conts)) or not args.diagonales): 
                        if (fijado[indf] != "^"):
                            a+=fijado[indf]
                            notf=True
                        else:
                            notf=False
                        
                        if not args.diagonales:
                            indf+=1    
                if not notf:
                    if((j+1 >= int(inicioint) and j+1 <= int(finalint)) or args.t == False):  
                        a += Utiles.randomnumber(ncar, 0, 9)
                    else:
                        a += Utiles.randomword(ncar)

                if j != columns - 1:
                    a += char
                notf=False

            if i != rows - 1:
                a += "\n"
                if args.diagonales:
                    for l in range(len(contp)):
                        contp[l]+=1
                    for l in range(len(conts)):
                        conts[l]-=1
                    indf+=1
                else:
                    indf=0

            if (i+columns+1 in idiagp):
                contp.append(0)
        texto+=a
        if k < n-1:
            texto+="\n"
        a = ""
            
    return texto
        
parser = argparse.ArgumentParser()
parser.add_argument("-M", type=str, nargs=3, dest="matrix", help="Genera matriz nxn")
parser.add_argument("--t", help='Cambia numeros por caracteres',action="store_true")
parser.add_argument("-f", type=str, nargs=1, dest="ejecuta", help='Crea un subproceso del ejecutable con el que se quieren probar los casos')
parser.add_argument("-fno", type=str, nargs=2, dest="ejecuta_casos_externos", help='Crea un subproceso del ejecutable ,pero se alimenta con casos externos')
parser.add_argument("-fij", type=str, nargs="*", dest="fijado", help='Fijado de caracteres en algunas posiciones')
parser.add_argument("-diag", type=str, nargs='*', dest="diagonales",help='Fijado de caracteres en diagonales')
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
    rows = Utiles.check_argument_list(args.matrix[0])
    columns = Utiles.check_argument_list(args.matrix[1])
    char = args.matrix[2]
    nchar = 1
    inicioint="0"
    finint="0"
    fijado=""
    iniciofijado="1"
    lineanofijada=""
    idiagp=[]
    idiags=[]
    idiagss=[]
    repeticiones=[1]

    if args.nchar:
        nchar = args.nchar[0]

    if args.intercalado: 
        inicioint = args.intercalado[0]
        finint = inicioint
        if(len(args.intercalado) == 2):
            finint = args.intercalado[1]    

    if args.fijado:
        fijado = args.fijado[0]
        if(len(args.fijado) == 2):
            iniciofijado = args.fijado[1]      
            if(args.nfijado):
                a = args.nfijado[0]

    if args.diagonales:
        idiagp=args.diagonales[0]
        idiagp=Utiles.check_argument_list(idiagp)
        if idiagp != [0]:
            for i in range(len(idiagp)):
                idiagp[i]-=1
        else:
            idiagp=[]
        if(len(args.diagonales) == 2):
            idiags=args.diagonales[1]
            idiags=Utiles.check_argument_list(idiags)
            if idiags != [0]:
                for i in range(len(idiags)):
                    idiags[i]-=1
            else:
                idiags=[]

    if args.size:
        repeticiones = args.size[0]
        repeticiones=Utiles.check_argument_list(repeticiones)

    cuentar=0
    cuentac=0
    inv=False
    cuenta=min(len(rows)-1,len(columns)-1)
    texto_a_ejecutar=""
    contp=0
    for i in repeticiones:

        if args.invn == True:
            texto_a_ejecutar+=str(columns[cuentar])+"\n"
            texto_a_ejecutar+=str(i)+"\n"
            inv=True

        if args.nonl == False and not inv:
            texto_a_ejecutar+=str(i)+"\n"
        if args.nonc == False and not inv:
            texto_a_ejecutar+=str(columns[cuentar])+"\n"

        texto_a_ejecutar+=imp_ristra(rows[cuentar], columns[cuentac], char, nchar, inicioint, finint, fijado, iniciofijado, lineanofijada, idiagp, idiags, int(i))

        if(contp<len(repeticiones)-1):
            texto_a_ejecutar+="\n"
        if(cuentar<cuenta):
            cuentar+=1
        if(cuentac<cuenta):
            cuentac+=1
        contp+=1

    print(texto_a_ejecutar)
    #print("\n")
    if args.ejecuta:
        ruta=args.ejecuta[0]
        p = subprocess.run([os.getcwd()+"\\"+ ruta],text=True, input=texto_a_ejecutar)