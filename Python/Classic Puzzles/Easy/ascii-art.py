l = int(input())
h = int(input())
t = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet_rows = [input() for _ in range(h)]

letter = {}
for i, char in enumerate(alphabet):
    letter[char] = [alphabet_rows[row][i*l : i*l+l] for row in range(h)]

for row in range(h):
    line = ""
    for c in t:
        c = c.upper()
        if c not in alphabet:
            c = "?"
        line += letter[c][row]
    print(line)
