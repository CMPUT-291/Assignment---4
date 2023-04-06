import argparse
import pymongo

parser = argparse.ArgumentParser()

parser.add_argument('port', type=int, nargs='?', default=27017, help='the port number to run the application on')

args = parser.parse_args()

port_number = args.port

print(type(str(port_number)))
print(pymongo.version)