lines = []

while True:
    if 'EOI' in lines:
        break
    lines.append(input())

for i in range(len(lines)-1):
    lines[i] = lines[i].upper()
    if 'NEMO' in lines[i]:
        print('Found')
    else:
        print('Missing')