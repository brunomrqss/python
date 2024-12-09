reader = open('/home/bruno/Desktop/python/think-python/chap08/nota.txt')

def special_line(line):
    return line.startswith('*** ')

for line in reader:
    if special_line(line):
        print(line.strip())

writer = open('nota2.txt', 'w')

for line in reader:
    if special_line(line):
        break
    writer.write(line)

reader.close()
writer.close()