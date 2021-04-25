terms = [
    ['S*O']
]

def process_so(term):
    number = len(term[:-1])
    return number

def process_term(term):
    if term[-1] == "O" and term[0] == 'S':
        output = process_so(term)
    return output

# for term in terms:
    # if term in input:
        # # extract term
        # process_term(term)

output = process_term('SSSSSSSO')
print(output)
