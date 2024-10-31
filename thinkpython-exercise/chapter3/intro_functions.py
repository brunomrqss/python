def print_lyrics():
    print("printando primeira linha")
    print("printando segunda linha")

print_lyrics()

def print_twice(string):
    print(string)
    print(string)

print_twice('Calling the function')
another = 'Another way to call a function'
print_twice(another)

def repeat(word, n):
    print(word*n)

mom = 'mamae, '
repeat(mom, 4)

def first_two_lines():
    repeat(mom, 4)
    repeat(mom, 4)

first_two_lines()

def last_three_lines():
    repeat(mom, 2)
    print("My wife is the mom of my child")
    repeat(mom, 2)

last_three_lines()

def print_text():
    first_two_lines()
    last_three_lines()

print_text()

for i in range(2):
    print("Verso", i)
    print_text()
    print()

# we can put this loop inside a function which 
# makes the same thing but in worth words

def repeat_verse(n):
    for i in range(n):
        print_text()
        print()

repeat_verse(2)

def cat_twice(part1,part2):
    cat = part1 + part2 
    print_twice(cat)

line1='bruno marques da silva'
line2='adhely monik lira de oliveira'
cat_twice(line1, line2)


# interface de uma função: local onde é adiciona o seu nome, parametro e ações 