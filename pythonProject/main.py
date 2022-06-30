import functions
import psutil
import logging

logging.basicConfig(filename='stat.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

for x in range(1):
    logging.info("#################################################")
    logging.info("START analyse")
    logging.info(functions.get_all_params())
    logging.info("STOP analyse")
    logging.info("#################################################")

