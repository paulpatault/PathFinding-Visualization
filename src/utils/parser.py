import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--N", help="Lenght of the board", type=int, default=20)
parser.add_argument("--C", help="Lenght of the board", type=str, default=None)

args = parser.parse_args()
