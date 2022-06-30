import functions
import psutil
import logging
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "influxdb"
org = "PKMM"
token = "KtpO_uTOFJZDeqKlmHQkKFHJwYhC5RFZmTXvdrCSn8VL-EjY9N0LLNiQ4SJXX_p5J-oKpKoW-RwWagOgpe-jvg=="
# Store the URL of your InfluxDB instance
url="http://10.57.29.248:8086"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("Measurment Paul").tag("location", "Paris").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)

logging.basicConfig(filename='stat.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

for x in range(1):
    logging.info("#################################################")
    logging.info("START analyse")
    logging.info(functions.get_all_params())
    logging.info("STOP analyse")
    logging.info("#################################################")

