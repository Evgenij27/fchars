
import random

def main():
    test_str = 'abcde'
    test_chars = {
        0 : ['(', ')'],
        1 : ['"'],
        2 : ['*']
    }
    strings = []
    for i in range(4):
        rnd = random.sample(range(len(test_chars)), 1)
        fchar = test_chars[rnd[0]]
        strings.append(fchar[0] + test_str + fchar[-1])

    print(strings)

    f = open('ftext.txt', 'w')
    f.write(' '.join(strings))
    f.close()


if __name__ == '__main__':
    main()


