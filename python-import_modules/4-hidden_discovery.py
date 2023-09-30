#!/usr/bin/python3

import hidden_4


def main():

    all_names = dir(hidden_4)

    filtered_names = sorted(
        [name for name in all_names if not name.startswith("__")])

    for name in filtered_names:
        print(name)


if __name__ == "__main__":
    main()
