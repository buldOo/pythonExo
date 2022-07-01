from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
import logging
import influxdb_client
import psutil
import logging
import time

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


def get_networks():
    """
    function to get all network on your machine
    :return:networks_stat, networks_system, networks_adrss, networks_stat_adrss
    """
    networks_stat = psutil.net_io_counters(pernic=False, nowrap=True)
    networks_adress = psutil.net_if_addrs()
    networks_stat_adress = psutil.net_if_stats()

    logging.basicConfig(filename='stat_networks.log', encoding='utf-8', level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    send_networks(networks_stat)

    return logging.info("networks stat :"), \
           logging.info(networks_stat), \
           logging.info("networks adress :"), \
           logging.info(networks_adress), \
           logging.info("networks stat adress :"), \
           logging.info(networks_stat_adress)


def get_cpu(interval):
    """
    function get cpu on your machine
    :param: interval
    :return: cpu_time, cpu_percent, cpu_percent_time, cpu_count, cpu_stats, cpu_freq
    """
    cpu_time = psutil.cpu_times(percpu=False)
    cpu_percent = psutil.cpu_percent(interval, percpu=False)
    cpu_percent_time = psutil.cpu_times_percent(interval, percpu=False)
    cpu_count = psutil.cpu_count(logical=True)
    cpu_stats = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq(percpu=False)

    logging.basicConfig(filename='stat_cpu.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    return logging.info("CPU TIME :"), \
           logging.info(cpu_time), \
           logging.info("CPU PERCENTAGE :"), \
           logging.info(cpu_percent), \
           logging.info("CPU PERCENT TIME :"), \
           logging.info(cpu_percent_time), \
           logging.info("CPU COUNT :"), \
           logging.info(cpu_count), \
           logging.info("CPU STAT :"), \
           logging.info(cpu_stats), \
           logging.info("CPU FREQ :"), \
           logging.info(cpu_freq)


def get_networks():
    """
    function to get all network on your machine
    :return:networks_stat, networks_system, networks_adrss, networks_stat_adrss
    """
    networks_stat = psutil.net_io_counters(pernic=False, nowrap=True)
    networks_system = psutil.net_connections()
    networks_adrss = psutil.net_if_addrs()
    networks_stat_adrss = psutil.net_if_stats()

    logging.basicConfig(filename='stat_networks.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    return logging.info("networks stat :"),\
           logging.info(networks_stat),\
           logging.info("networks system:"),\
           logging.info(networks_system),\
           logging.info("networks adress :"),\
           logging.info(networks_adrss), \
           logging.info("networks stat adress :"), \
           logging.info(networks_stat_adrss)


def get_virtual_memory():
    """
    functuion to get memory on your machine
    :return: virtual_memory, swap_memory
    """
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    return logging.info("VIRTUAL MEMORY :"), \
           logging.info(virtual_memory), \
           logging.info("SWAP MEMORY"), \
           logging.info(swap_memory)


def get_sensors():
    """
    function to get sensors of your machine
    :return: sensors_temperature, sensors_fans, sensors_battery
    """
    sensors_temperature = psutil.sensors_temperatures()
    sensors_fans = psutil.sensors_fans()
    sensors_battery = psutil.sensors_battery()

    return logging.info("SENSORS TEMPERATURE :"), \
           logging.info(sensors_temperature), \
           logging.info("SENSORS FANS :"), \
           logging.info(sensors_fans), \
           logging.info("SENSORS BATTERY :"), \
           logging.info(sensors_battery)


def get_disk():
    """
    function to get disk opf your machine
    :return:
    """
    disk_stats = psutil.disk_io_counters(perdisk=False, nowrap=True)

    return logging.info("DISK STATS :"), \
           logging.info(disk_stats)


def get_all_params(interval):
    while True:
        get_cpu(interval)
        get_networks()
        get_virtual_memory()
        #get_sensors()
        print('loop')
        print(interval)
        time.sleep(int(interval))
