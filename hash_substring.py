
def read_input():
    filepath = './tests/'
    ile = input()
    folder = filepath + file
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        filename = input().rstrip()
        with open(folder) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    prime = 1000000007
    multiplier = 263
    len_p = len(pattern)
    len_t = len(text)
    # and return an iterable variable

    hash_p = 0
    hash_w = 0
    for i in range(len_p):
        hash_p = (hash_p * multiplier + ord(pattern[i])) % prime
        hash_w = (hash_w * multiplier + ord(text[i])) % prime

    roll_multiplier = pow(multiplier, len_p - 1, prime)    

    if hash_p == hash_w:
        if pattern == text[:len_p]:
            return [0]

    occurrences = []
    for i in range(1, len_t - len_p + 1):
        hash_w = ((hash_w - ord(text[i-1])*roll_multiplier) * multiplier + ord(text[i+len_p-1])) % prime
        if hash_p == hash_w:
            if pattern == text[i:i+len_p]:
                occurrences.append(i)

    return occurrences



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
