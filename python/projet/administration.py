import psutil
import argparse

parser = argparse.ArgumentParser(description='Définissez l\'intervalle en seconde')
parser.add_argument('interval', metavar='--interval', type=int, help='Valeur en seconde')
args = parser.parse_args()
interval = args.interval

i = 0
while i < 10:
    percentage = psutil.cpu_percent(interval=1)
    print(percentage)
    i += 1