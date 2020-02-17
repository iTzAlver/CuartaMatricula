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
        self, rows, columns, char=" ", ncar=1, tipo=0, iniciot="0" , finalt="0" , fijado="" , inicionf="0" , finalnf="0" , n=1
    ):
        a = ""
        b=0
        ind=0
        contc = 1

        for k in range(n):
            for i in range(rows):
                for j in range(columns):
                    if (contc >= int(iniciot) and contc <= int(finalt)) or tipo == 0:  
                        a += Utiles.randomnumber(ncar, 0, 9)
                    else:
                        a += Utiles.randomword(ncar)
 
                    if j != columns - 1:
                        a += char
                     
                    if len(fijado)>0 and ind<len(fijado): 
                        if (contc >= int(inicionf) and contc <=int(finalnf)):
                            if fijado != "" and fijado[ind] != "^":
                                a=a[:b]+fijado[ind]+a[(b+1):]
                            ind+=1

                    b+=(1+len(char))
                    contc += 1

                if i != rows - 1:
                    a += "\n"
                    b = len(a)
                    
                contc=1
                ind = 0

            print(a)
            a = ""
            b=0

gen = Generator_test()

parser = argparse.ArgumentParser()

parser.add_argument("-M", type=str, nargs=5, dest="matrix", help="Genera matriz nxn")

parser.add_argument('-i', type=str, nargs="*", dest="intercalado", help='intercalado')

parser.add_argument('-f', type=str, nargs="*", dest="fijado", help='fijado')

parser.add_argument('-n', type=str, nargs=1, dest="size", help='n lineas')


args = parser.parse_args()


if args.matrix:
    a1 = str(args.matrix[0])
    a2 = str(args.matrix[1])
    a3 = str(args.matrix[2])
    a4 = int(args.matrix[3])
    a5 = int(args.matrix[4])
    a6="0"
    a7="0"
    a8=""
    a9=""
    a10=""
    a11=[1]

if args.intercalado: 
    a6 = str(args.intercalado[0])
    a7 = a6
    if(len(args.intercalado) == 2):
        a7 = str(args.intercalado[1])    

if args.fijado:
    a8 = str(args.fijado[0])
    if(len(args.fijado) == 2):
        a9 = str(args.fijado[1])
        a10 = a9
    if(len(args.fijado) == 3):
        a9 = str(args.fijado[1])
        a10 = str(args.fijado[2])

if args.size:
    a11 = str(args.size[0]) 
    a11=Utiles.check_argument_list(a11)

cuentar=0
cuentac=0
a1=Utiles.check_argument_list(a1)
a2=Utiles.check_argument_list(a2)
for i in a11:
    print(i)
    gen.imp_ristra(a1[cuentar], a2[cuentac], a3, a4, a5, a6, a7 , a8 , a9 , a10 , int(i))
    if(cuentar<len(a1)-1):
        cuentar+=1
    if(cuentac<len(a2)-1):
        cuentac+=1
