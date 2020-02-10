import argparse
from generators import Generator_test


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
