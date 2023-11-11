import argparse

# import sys
# print(sys.argv)
# nums = sys.argv[1:]
# print(sum(map(int, nums)))

__version__ = "1.1.0"

parser = argparse.ArgumentParser(
    prog="main program",
    description="This is a argparse project",
    epilog="Please buy me coffee if you find it useful!",
)

parser.version = __version__

parser.add_argument("x", type=int, help="first input", choices=(100, 200))
parser.add_argument("y", type=int, help="second input")
parser.add_argument("-z", help="third input", required=True)
parser.add_argument("-c", help="It is a constant", action="store_const", const=20)
parser.add_argument("-a", "--all", help="Show all args", action="store_true")
parser.add_argument("-v", "--version", action="version")
parser.add_argument("--train", dest="train")


args = parser.parse_args()
print(args.x)
print(args.y)

if args.all:
    print(vars(args))
