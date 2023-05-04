import json


# Start of the program
if __name__ == '__main__':
    # Load morse code mapping into dict
    with open("morse_code.json", 'r+') as f:
        morse = json.load(f)

    while True:
        # receive input string
        str_origin = input("Please input your string(input '~' to quit the program): ")
        if '~' == str_origin:
            print("Exit code '~'detected See you next time!")
            break
        for c in str_origin:
            try:
                print(morse[c.upper()])
            except KeyError as e:
                print(f"This char '{c}' does not have morse code.")
                continue





