#python3  Kristaps Mūrnieks 221RDB173


def read_input():
    filepath = './tests/'
    file = '06'
    folder = filepath + file
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()

    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open(folder, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    return pattern, text

    
    
    # after input type choice
    # read two lines 
    # first line is pattern 

    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    positions = []
    pattern_len = len(pattern)
    text_len = len(text)
 
    p = 31
    m = 10**9 + 9
    p_pow = [1]
    h = [0] * (text_len + 1)
    for i in range(1, text_len + 1):
        p_pow.append((p_pow[-1] * p) % m)
        h[i] = (h[i - 1] * p + ord(text[i - 1])) % m

    pattern_hash = 0
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
    for i in range(text_len - pattern_len + 1):
        if pattern_hash != (h[i + pattern_len] - h[i] * p_pow[pattern_len]) % m:
            continue
        if text[i:i+pattern_len] == pattern:
            positions.append(i)

    return positions


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
