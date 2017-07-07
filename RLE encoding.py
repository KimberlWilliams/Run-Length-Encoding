#RLE encoding
S=raw_input("Enter your input string:").strip().split(' ')
alpha={'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26, 'a': 33, 'c': 35, 'b': 34, 'e': 37, 'd': 36, 'g': 39, 'f': 38, 'i': 41, 'h': 40, 'k': 43, 'j': 42, 'm': 45, 'l': 44, 'o': 47, 'n': 46, 'q': 49, 'p': 48, 's': 51, 'r': 50, 'u': 53, 't': 52, 'w': 55, 'v': 54, 'y': 57, 'x': 56, 'z': 58}
encs=""
for i in range(len(S)):
    for j in range(len(S[i])):
        if j%2==0:
            encs+="0"*alpha[S[i][j]]
        else:
            encs+="!"*alpha[S[i][j]]
            
print "Encoded String:"
for i in range(0,len(encs),57):
    print encs[i:i+57]
    
