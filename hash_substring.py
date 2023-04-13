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
        with open('folder', 'r') as f:
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
    # this function should find the occurances using Rabin Karp alghoritm 
    prime = 1000000007
    multiplier = 263
    pattern_hash = 0
    text_hash = 0
    multiplier_pow = 1
    positions = []

    for i in range(len(pattern)):
        pattern_hash = (pattern_hash + ord(pattern[i]) * multiplier_pow) % prime
        text_hash = (text_hash + ord(text[i]) * multiplier_pow) % prime
        multiplier_pow = (multiplier_pow * multiplier) % prime

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)
        if i == len(text) - len(pattern):
            break
        text_hash = (text_hash - ord(text[i]) + ord(text[i+len(pattern)]) * multiplier_pow) % prime
    return positions



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
