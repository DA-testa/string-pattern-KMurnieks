#python3  Kristaps Mūrnieks 221RDB173


def read_input():
    filepath = './tests/'
    file = '6'
    folder = filepath + file
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    def read_input():
    input_type = input("Enter 'F' to read from file, or press any other key to enter text manually: ")
    if input_type == "F":
        filename = input("Enter the file name: ")
        with open(filename) as f:
            text = f.read().rstrip()
    else:
        text = input("Enter the text: ").rstrip()
    pattern = input("Enter the pattern: ").rstrip()

    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    return pattern, text
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    result = []
    p_len, t_len = len(pattern), len(text)
    p_hash = hash(pattern)
    t_hashes = [hash(text[i:i+p_len]) for i in range(t_len - p_len + 1)]
    for i, h in enumerate(t_hashes):
        if h == p_hash and text[i:i+p_len] == pattern:
            result.append(i)
    return result



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
