import sys
input = sys.argv[1]

terms = [
    ['3', '\n'+'M'],
    ['1', 'I'],
    ['0', 'U']
]


def convert_mui(input):
    output = ""
    for char in input:
        for term in terms:
            char = char.replace(term[0], term[1])
        output += char

    print(output)

if __name__ == "__main__":
    convert_mui(input)
