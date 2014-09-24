# Need Python3

import sys
import re


def main(argv):
    # argv will be the name of text file or(and) contain the path to this file
    f = open(argv, mode='r', encoding='utf-8')
    lines = [line.rstrip()  for line in f.read().split() if line.rstrip()]
    print(lines)
    f.close()
    fil = []
    nums_chars = 0.0
    pat = re.compile(r'\b[A-Z]*\b', re.IGNORECASE)
    for w in lines:
        if pat.search(w):
            fil.append(pat.search(w).group())
    print('filleterd text,maybe {0}'.format(fil))
    nums_chars = sum([len(fw) for fw in fil])
    print('Numbers of chars in text {0}'.format(nums_chars))




if __name__ == '__main__':
    main(sys.argv[1])

