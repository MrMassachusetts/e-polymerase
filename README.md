# e-polymerase
A python script, which converts DNA strings into Helixes and RNA
Download: git clone https://github.com/MrMassachusetts/e-polymerase
Run: 

How to use:
If you open the program, you have two choices:
1. Generate a DNA Helix out of a single DNA-String
2. Generate a RNA-String out of a DNA-String
3. Generate Amino-Acids (Proteines) out of RNA-String

Generate a DNA Helix out of a single DNA-String
You'll need to enter a single strained DNA-String with the direction 5' - 3' - without spaces. The program will generate the complementary 3' - 5' string, and it will display both. If you want to you can safe a file with both strings to the folder, where the script is. If the sequence is shorter than 10000 nucleotides it will generate instantly, if its longer or your cpu is bad, it could take longer.

Generate a RNA-String out of a DNA-String
You'll need to enter a single-strained DNA-String with the direction 3' - 5' - without spaces. The program will genenerate a 5' - 3' RNA. It wont splice the m-RNA into a RNA. You can safe the RNA-String to the folder, where the script is. If the sequence is shorter than 10000 nucleotides it will generate instantly, if its longer or your cpu is bad, it could take longer.

Generate Amino-Acids (Proteines) out of RNA-String
You'll need to enter a single-strained RNA-String with the direction 5' - 3' - without spaces. The program will generate the Amino-Acids for the base-tripletts. If you have forgotten a nucleotide, the program wont start (number of nucleotides must be divisible by 3). You can safe the amino-acids in a text file to your computer.
