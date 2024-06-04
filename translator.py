text_to_nato = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
    'Y': 'Yankee', 'Z': 'Zulu', '0': 'Zero', '1': 'One',
    '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
    '-': 'Dash', ' ': ' '
}

def encode():
    message = input("Enter your message: ")
    ls = []
    for i in message:
        if i.upper() in text_to_nato:
            ls.append(text_to_nato[i.upper()])
        else:
            ls.append(i)
    print(' '.join(ls))

nato_to_text = {value: key for key, value in text_to_nato.items()}

def decode():
    message = input("Enter your encrypted message: ")
    words = message.split(' ')
    decoded_message = []
    for word in words:
        if word in nato_to_text:
            decoded_message.append(nato_to_text[word])
        else:
            decoded_message.append(word)
    print(''.join(decoded_message))

choice = int(input("Enter 1 for Encode and 2 for Decode: "))
if choice == 1:
    encode()
elif choice == 2:
    decode()
else:
    print('Wrong input!!')
