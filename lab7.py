with open ('inData.txt', 'r') as f:
    num1 = int(f.readline())
    num2 = int(f.readline())
    char = f.readline().strip()
    text = f.readline().strip()

total = num1 + num2
next_char = chr(ord(char) + 1)

with open ('outData.txt', 'w') as f:
    f.write(f'{total}\n')
    f.write(f'{next_char}\n')
    f.write(f'{text}\n')