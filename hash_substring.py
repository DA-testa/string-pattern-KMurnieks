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

    for i in range(text_len - pattern_len + 1):
        if text[i:i+pattern_len] == pattern:
            positions.append(i)
            
    return positions


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
