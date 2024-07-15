def char_counter(path_to_DNA_string):
    raw_file = open(path_to_DNA_string, "r")
    DNA_string = raw_file.read()

    A_count, C_count, G_count, T_count = 0, 0, 0, 0

    for char in range(len(DNA_string)):
        if DNA_string[char].upper() == 'A':
            A_count += 1
        elif DNA_string[char].upper() == 'C':
            C_count += 1
        elif DNA_string[char].upper() == 'G':
            G_count += 1
        elif DNA_string[char].upper() == 'T':
            T_count += 1
    
    raw_file.close()
    
    return f'{A_count} {C_count} {G_count} {T_count}'


print(char_counter("./../data/rosalind_dna.txt"))