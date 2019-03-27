import sys
print('Do you want to ')
print('1. Convert single DNA-String into double-helix')
print('2. Convert DNA into RNA')
choice = input('> ')

if choice == '1':
    print('Input your single-strained DNA-String:')
    print('Without spaces, capitalization does not matter')
    print('Use: C=cytosine, G=guanine, A=adenine, T=thymine')
    dnastring = input('5\'> ')
    dnastring = dnastring.lower()
    leng = len(dnastring)
    dnastring = list(dnastring)
    compstring = []
    leng-=1
    while leng >= 0:
        if dnastring[leng] == 'c':
            compstring.extend('G')
        elif dnastring[leng] == 'g':
            compstring.extend('C')
        elif dnastring[leng] == 'a':
            compstring.extend('T')
        elif dnastring[leng] == 't':
            compstring.extend('A')
        else:
            print('Only the characters a, t, c and g are allowed')
            input('Press enter to exit')
            sys.exit()
        leng -= 1
    compstring = compstring[::-1]
    strang = ' '.join(dnastring)
    strang = str(strang)
    strang = strang.upper()
    print('\n')
    print("5\'", strang)
    print("3\'", ' '.join(compstring))
    print('\n')
    print('Do you want to save it in a text-file? (Y|N)')
    yn = input('> ')
    if yn in ('Y', 'y'):
        f1 = open('dnastring.txt', 'wt')
        line1 = "5\'", strang, "\n"
        #line1 = str(line1)
        line2 = "3\'", ' '.join(compstring)
        #line2 = str(line2)
        f1.write(''.join(line1))
        f1.write(''.join(line2))
        f1.close()
        print('DNA-String saved as \'dnastring.txt\'')
        input('Press enter to exit')
    else:
        input('Press enter to exit')
elif choice == '2':
    print('Input your single-strained DNA-String:')
    print('Without spaces, capitalization does not matter')
    print('Use: C=cytosine, G=guanine, A=adenine, T=thymine')
    dna2 = input('3\'> ')
    dna2 = dna2.lower()
    leng = len(dna2)
    dna2 = list(dna2)
    compstring = []
    leng -= 1
    while leng >= 0:
        if dna2[leng] == 'c':
            compstring.extend('G')
        elif dna2[leng] == 'g':
            compstring.extend('C')
        elif dna2[leng] == 'a':
            compstring.extend('U')
        elif dna2[leng] == 't':
            compstring.extend('A')
        else:
            print('Only the characters a, t, c and g are allowed')
            input('Press enter to exit')
            sys.exit()
        leng -= 1
    compstring = compstring[::-1]
    strang = ' '.join(dna2)
    strang = str(strang)
    strang = strang.upper()
    print('\n')
    print("5\'", strang)
    print("3\'", ' '.join(compstring))
    print('\n')
    print('Do you want to save it in a text-file? (Y|N)')
    yn = input('> ')
    if yn in ('Y', 'y'):
        f1 = open('rnastring.txt', 'wt')
        line1 = "3\'", strang, "\n"
        line2 = "5\'", ' '.join(compstring)
        f1.write(''.join(line2))
        f1.close()
        print('RNA-String saved as \'rnastring.txt\'')
        input('Press enter to exit')
    else:
        input('Press enter to exit')
else:
    print('Only Numbers from 1-3 are allowed')
    input('Press enter to exit')