import getParams
import logging
import argparse

# argParse library command line toul to configure args
parser = argparse.ArgumentParser(description='Définissez l\'intervalle en seconde')
parser.add_argument('-i', '--interval', type=int, help='Valeur en seconde')
args = parser.parse_args()
interval = args.interval



for x in range(10):
    logging.info("#################################################")
    logging.info("START CPU analyse")
    logging.info(getParams.get_all_params(interval))
    logging.info("STOP CPU analyse")
    logging.info("#################################################")
