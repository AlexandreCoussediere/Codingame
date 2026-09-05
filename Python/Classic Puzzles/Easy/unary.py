import sys
import math

message = input()

bits = "".join(format(ord(c), '07b') for c in message)

result = []
i = 0
n = len(bits)
while i < n:
    current_bit = bits[i]
    run_length = 0
    while i < n and bits[i] == current_bit:
        run_length += 1
        i += 1
    first_block = "0" if current_bit == "1" else "00"
    second_block = "0" * run_length
    result.append(first_block)
    result.append(second_block)

print(" ".join(result))
