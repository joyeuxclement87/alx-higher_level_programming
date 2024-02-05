#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            ans += a ** b / j
        except Exception:
            ans = b + a
            break
    return ans
