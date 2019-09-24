from test_framework import generic_test


def justify_text(words, L):
    ret  = []
    i=0
    while i < len(words):
        line = []
        counter = 0
        while i < len(words) and counter <= L:
            tmp = words[i]
            if counter+len(tmp) > L:
                break
            line.append(tmp)
            counter += 1 + len(tmp)
            i += 1
        counter -= len(line)
        # find space multiplier
        if i == len(words):
            tmp = ''
            for word in line:
                tmp += word + ' '
            tmp += ' '*(L-counter)
        else:
            if len(line) != 1:
                rem = (L-counter)%(len(line)-1)
                mult = (L-counter)//(len(line)-1)
            else:
                mult = L - counter
                rem = 0
            
            tmp = ''
            for word in line:
                tmp += word
                extra = 0
                if rem > 0:
                    extra = 1
                    rem = max(0, rem-1)
                tmp += ' '*(mult+extra)
        ret.append(tmp[:L])
    
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
