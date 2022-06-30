import functions
import psutil
import logging

logging.basicConfig(filename='stat.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

for x in range(10):
    logging.info("#################################################")
    logging.info("START CPU analyse")
    logging.info(functions.get_networks())
    logging.info("STOP CPU analyse")
    logging.info("#################################################")

