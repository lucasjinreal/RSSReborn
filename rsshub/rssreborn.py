"""



"""

import os
from rsshub import create_app
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--ip", type=str, default="127.0.0.1")
parser.add_argument("--port", type=str, default=5000)
parser.add_argument("--https", action="store_true")
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()


def main():
    app = create_app("production")
    app.run(host=args.ip, port=args.port, debug=args.debug)
