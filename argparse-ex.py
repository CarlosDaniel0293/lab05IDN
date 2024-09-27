import argparse

parser = argparse.ArgumentParser(description="Ejemlo con argparse")
parser.add_argument('--name', required-True, help='Tu nombre')
args = parser.parse_args()

print(f"Hola, {arg.name}!")