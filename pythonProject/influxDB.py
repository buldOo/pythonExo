from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
import logging
import influxdb_client

bucket = "influxDB"
org = "PKMM"
token = "KtpO_uTOFJZDeqKlmHQkKFHJwYhC5RFZmTXvdrCSn8VL-EjY9N0LLNiQ4SJXX_p5J-oKpKoW-RwWagOgpe-jvg=="
# Store the URL of your InfluxDB instance
url = "http://10.57.29.248:8086/"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

logging.basicConfig(filename='stat.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def send_networks(network):
    """
    send network to influxdb
    :param network:
    :return:
    """
    record = (
        Point("measurement")
        .tag("tag", "network")
        .field("bytes_sent", network.bytes_sent)
        .field("bytes_recv", network.bytes_recv)
        .field("packets_sent", network.packets_sent)
        .field("packets_recv", network.packets_recv)
    )
    write_api.write(bucket=bucket, org=org, record=record)


def send_cpu(cpu):
    """
    send cpu to influxdb
    :param cpu:
    :return:
    """
    record = (
        Point("measurement")
        .tag("tag", "cpu")
        .field("user", cpu.user)
        .field("nice", cpu.nice)
        .field("system", cpu.system)
        .field("idle", cpu.idle)
    )
    write_api.write(bucket=bucket, org=org, record=record)


def send_virtual_memory(memory):
    """
    send memory to influxdb
    :param virtual_memory:
    :return:
    """
    record = (
        Point("measurement")
        .tag("tag", "memory")
        .field("total memory", memory.total)
        .field("available", memory.available)
        .field("used", memory.used)
        .field("percent", memory.percent)
    )
    write_api.write(bucket=bucket, org=org, record=record)


def send_disk(disk):
    """
    send disk to influxdb
    :param disk:
    :return:
    """
    record = (
        Point("measurement")
        .tag("tag", "disk")
        .field("read_count", disk.read_count)
        .field("write_count", disk.write_count)
        .field("read_bytes", disk.read_bytes)
        .field("write_bytes", disk.write_bytes)
    )
    write_api.write(bucket=bucket, org=org, record=record)
