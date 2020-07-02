import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--N", help="Lenght of the board", type=int, default=20)
parser.add_argument("--C", help="Color style", type=str, default="smooth")
parser.add_argument("--algo", help="Astar or Dijkstra", type=str, default="astar")
parser.add_argument("--nd", help="Unauthorize Diagonals", type=bool, default=False)

args = parser.parse_args()
