#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            else:
                output += a ** b / n
        except Exception:
            output = a + b
            break
        return (output)
