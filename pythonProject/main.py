import functions
import psutil
import logging
import argparse

parser = argparse.ArgumentParser(description='Définissez l\'intervalle en seconde')
parser.add_argument('-i', '--interval', type=int, help='Valeur en seconde')
args = parser.parse_args()
interval = args.interval


if __name__ == '__main__':
    for x in range(10):
        logging.info("#################################################")
        logging.info("START CPU analyse")
        logging.info(functions.get_all_params(interval))
        logging.info("STOP CPU analyse")
        logging.info("#################################################")
