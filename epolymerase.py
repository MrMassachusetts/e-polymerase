import sys
version = '1.1.1'
print('E-Polymerase by MrMassachusetts')
print('Version: ', version)
print('')
print('Do you want to ')
print('1. Convert single DNA-String into double-helix')
print('2. Convert DNA into RNA')
print('3. Convert RNA into Amino-Acids')
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
elif choice == '3':
    print('Please input the RNA-String')
    print('Without spaces, capitalization does not matter ')
    print('If there is a wrong character in a triplett, the whole triplett will be ignored')
    print('Use: c=cytosine, g=guanine, u=uracil, t=thymine')
    rna = input('5\'> ')
    if len(rna) % 3 == 0:
        lang = len(rna)
        rna = list(rna)
        count = 0
        count2 = 3
        amac = []
        while lang >= 0:
            if rna[count:count2] == ['a', 'a', 'a'] or rna[count:count2] == ['a', 'a', 'g']:
                amac.append('Lysine')
            elif rna[count:count2] == ['a', 'u', 'g']:
                amac.append('Methionine (Start)')
            elif rna[count:count2] == ['a', 'c', 'u'] or rna[count:count2] == ['a', 'c', 'c'] or rna[count:count2] == ['a', 'c', 'a'] or rna[count:count2] == ['a', 'c', 'g']:
                amac.append('Threonine')
            elif rna[count:count2] == ['a', 'a', 'u'] or rna[count:count2] == ['a', 'a', 'c']:
                amac.append('Asparagine')
            elif rna[count:count2] == ['a', 'g', 'u'] or rna[count:count2] == ['a', 'g', 'c'] or rna[count:count2] == ['u', 'c', 'u'] or rna[count:count2] == ['u', 'c', 'c'] or rna[count:count2] == ['u', 'c', 'a'] or rna[count:count2] == ['u', 'c', 'g']:
                amac.append('Serine')
            elif rna[count:count2] == ['a', 'g', 'a'] or rna[count:count2] == ['a', 'g', 'g'] or rna[count:count2] == ['c', 'g', 'u'] or rna[count:count2] == ['c', 'g', 'c'] or rna[count:count2] == ['c', 'g', 'a'] or rna[count:count2] == ['c', 'g', 'g']:
                amac.append('Arginine')
            elif rna[count:count2] == ['g', 'u', 'u'] or rna[count:count2] == ['g', 'u', 'c'] or rna[count:count2] == ['g', 'u', 'a'] or rna[count:count2] == ['g', 'u', 'g']:
                amac.append('Valine')
            elif rna[count:count2] == ['g', 'c', 'u'] or rna[count:count2] == ['g', 'c', 'c'] or rna[count:count2] == ['g', 'c', 'a'] or rna[count:count2] == ['g', 'c', 'g']:
                amac.append('Alanine')
            elif rna[count:count2] == ['g', 'a', 'u'] or rna[count:count2] == ['g', 'a', 'c']:
                amac.append('Aspartic acid')
            elif rna[count:count2] == ['g', 'a', 'a'] or rna[count:count2] == ['g', 'a', 'g']:
                amac.append('Glutamic acid')
            elif rna[count:count2] == ['g', 'g', 'u'] or rna[count:count2] == ['g', 'g', 'c'] or rna[count:count2] == ['g', 'g', 'a'] or rna[count:count2] == ['g', 'g', 'g']:
                amac.append('Glycine')
            elif rna[count:count2] == ['u', 'u', 'u'] or rna[count:count2] == ['u', 'u', 'c']:
                amac.append('Phenylalanine')
            elif rna[count:count2] == ['u', 'u', 'a'] or rna[count:count2] == ['u', 'u', 'g'] or rna[count:count2] == ['c', 'u', 'u'] or rna[count:count2] == ['c', 'u', 'c'] or rna[count:count2] == ['c', 'u', 'a'] or rna[count:count2] == ['c', 'u', 'g']:
                amac.append('Leucine')
            elif rna[count:count2] == ['u', 'a', 'u'] or rna[count:count2] == ['u', 'a', 'c']:
                amac.append('Tyrosine')
            elif rna[count:count2] == ['u', 'a', 'a'] or rna[count:count2] == ['u', 'a', 'g'] or rna[count:count2] == ['u', 'g', 'a']:
                amac.append('Stop')
            elif rna[count:count2] == ['u', 'g', 'u'] or rna[count:count2] == ['u', 'g', 'c']:
                amac.append('Cysteine')
            elif rna[count:count2] == ['u', 'g', 'g']:
                amac.append('Tryptophan')
            elif rna[count:count2] == ['c', 'c', 'u'] or rna[count:count2] == ['c', 'c', 'c'] or rna[count:count2] == ['c', 'c', 'a'] or rna[count:count2] == ['c', 'c', 'g']:
                amac.append('Proline')
            elif rna[count:count2] == ['c', 'a', 'u'] or rna[count:count2] == ['c', 'a', 'c']:
                amac.append('Histidine')
            elif rna[count:count2] == ['c', 'a', 'a'] or rna[count:count2] == ['c', 'a', 'g']:
                amac.append('Glutamine')
            elif rna[count:count2] == ['a', 'u', 'u'] or rna[count:count2] == ['a', 'u', 'c'] or rna[count:count2] == ['a', 'a', 'a']:
                amac.append('Isoleucine')
            lang -= 3
            count += 3
            count2 += 3
        print()
        print('The amino-acids from your proteine are:')
        print(', '.join(amac))
        print('')
        print('Do you want to save it as a file? (Y|N)')
        yn2 = input('> ')
        if yn2 in ('Y', 'y'):
            f1 = open('protein.txt', 'wt')
            f1.write(', '.join(amac))
            f1.close()
            print('RNA-String saved as \'protein.txt\'')
            input('Press enter to exit')
        else:
            input('Press enter to exit')
    else:
        print('Error: Lenght of RNA-String not divisible trough 3')
        input('Press enter to exit')

else:
    print('Only Numbers from 1-3 are allowed')
    input('Press enter to exit')
