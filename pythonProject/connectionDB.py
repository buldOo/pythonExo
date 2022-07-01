import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import logging


def writeDataDB():
    """
   connection influDB in VM and write all params
   :return: null
   """
    bucket = "influxdb"
    org = "PKMM"
    token = "KtpO_uTOFJZDeqKlmHQkKFHJwYhC5RFZmTXvdrCSn8VL-EjY9N0LLNiQ4SJXX_p5J-oKpKoW-RwWagOgpe-jvg=="
    # Store the URL of your InfluxDB instance
    url = "http://10.57.29.248:8086"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("Measurment Paul").tag("location", "Paris").field("temperature", 25.3)

    return logging.info("CONNECT TO DB"),\
           logging.info("WRITE DATA PARAMS:"),\
           logging.info(write_api.write(bucket=bucket, org=org, record=p)),\
           write_api.write(bucket=bucket, org=org, record=p)


