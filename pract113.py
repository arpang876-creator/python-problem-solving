with open("poem.txt", "r") as f:
    data = f.readlines()

longest_line = data[0]
longest = len(data[0])

for line in data:
    if len(line) > longest:
        longest = len(line)
        longest_line = line

print("Longest Line:", longest_line)
print("Characters in the longest line:", longest)