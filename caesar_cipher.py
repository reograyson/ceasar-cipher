from art import logo

def caesar(text,shift,direction):
    encoded_text = ""
    for char in text:
        if char not in alphabet:
            encoded_text += char
            continue
        char_index = alphabet.index(char)
        if direction == "encode":
            encode_index = char_index + shift
            encoded_text += alphabet[encode_index]
        if direction == "decode":
            encode_index = char_index - shift
            encoded_text += alphabet[encode_index]
    print(f">>{encoded_text}<<")


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%25
    caesar(text,shift,direction)
    pop = input("\nWant to start again?(yes or no)\n").lower()
    if pop == "yes":
        continue
    else:
        break
