#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cnt = len(sys.argv) - 1
    if cnt == 0:
        print("0 arguments.")
    elif cnt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cnt))
    for a in range(cnt):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
