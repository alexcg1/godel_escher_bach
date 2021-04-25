import sys

terms = [
    ['611', '\n'],
    ['666', 'O'],
    ['123', 'S'],
    ['111', '='],
    ['112', '+'],
    ['236', '*'], # Actually "." in the book
    ['362', '('],
    ['323', ')'],
    ['212', '<'],
    ['213', '>'],
    ['312', '['],
    ['313', ']'],
    ['262', 'a'], # Opposite to "for all - inverted A"
    ['163', '`'],
    ['161', '∧'], # and
    ['616', '∨'], # or
    ['633', '⇒'], # implies (⊃ in book)
    ['223', '~'], # not
    ['333', '∃'], # There exists
    ['626', '∀'], # for all
    ['636', ':'], # specify definition
    ['611', '😀'] # special character - doesn't specify what
]



def convert_tnt(input):
    input = input.split(",")
    output = ""
    for codon in input:
        for term in terms:
            codon = codon.replace(term[0], term[1])
        output += codon

    print(output)

def tnt_to_num(input):
    output = ""
    for char in input:
        for term in terms:
            char = char.replace(term[1], term[0]+',')
        output += char
    output = output [:-1] # rm final comma

    print(output)

def num_to_so(num):
    # Take an int, output something like SSSSSSSO
    output = ""
    for i in range(num):
        output += 'S'
    output += 'O'
    return output

simple_terms = [
    ['S*O']
]

def process_so(term):
    number = len(term[:-1])
    return number

def process_term(term):
    if term[-1] == "O" and term[0] == 'S':
        output = process_so(term)
    return output

input = "626,262,636,223,123,262,111,666"
output = convert_tnt(input)

# tnt_to_num('O=O')
# output = num_to_so(666_111)
print(output)

print(process_term("SSSO"))
