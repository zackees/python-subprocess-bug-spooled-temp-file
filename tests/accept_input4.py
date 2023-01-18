import sys

for _ in range(4):
    answer = input("Accept [y/n]?: ")
    if answer == "y":
        sys.stdout.write("OK\n")
        sys.stdout.flush()
        sys.exit(0)
    else:
        sys.stdout.write("Failed\n")
        sys.stdout.flush()
        sys.exit(1)