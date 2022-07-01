import connectionDB
import getParams
import connectionDB
import psutil
import logging

# Configure loging tool
logging.basicConfig(filename='stat.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Get all params of your machine
for x in range(1):
    logging.info("#################################################")
    logging.info("START analyse")
    logging.info(getParams.get_all())
    logging.info("STOP analyse")
    logging.info("#################################################")

# Connection to InfluxDB and write params of your machine
getParams.

