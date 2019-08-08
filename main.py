# -*- coding: utf-8 -*-

log = []

def repl():
    line = input()
    if line == "view":
        for l in log:
            print(l)
    elif line == "exit":
        exit();
    else:
        print(">",line)
        log.append(line)

def main():
    while True:
        repl()

if __name__ == '__main__':
    main()
