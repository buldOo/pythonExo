# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import getParams
import logging
import argparse


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# argParse library command line toul to configure args
parser = argparse.ArgumentParser(description='Définissez l\'intervalle en seconde')
parser.add_argument('-i', '--interval', type=int, help='Valeur en seconde')
args = parser.parse_args()
interval = args.interval


# write all 10s analyse machine
for x in range(10):
    logging.info("#################################################")
    logging.info("START machine analyse")
    logging.info(getParams.get_all_params(interval))
    logging.info("STOP machine analyse")
    logging.info("#################################################")
