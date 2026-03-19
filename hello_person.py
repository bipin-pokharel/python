import argparse

parser = argparse.ArgumentParser(description="provides personal greeting.")
parser.add_argument(
    "-n",
    "--name",
    metavar="name",
    required=True,
    help="the name of the person is greet",
)

args = parser.parse_args()
msg = f"hello{args.name}!"
print(msg)
