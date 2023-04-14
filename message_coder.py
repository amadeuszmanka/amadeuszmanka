alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(input_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_char = alphabet[new_position]
            cipher_text += new_char
        else:
            cipher_text += char

    print(f"The {cipher_direction}d text is: {cipher_text}")


print("Welcome to the program where you can encrypt or decrypt a secret message")
end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceasar(input_text=text, shift_amount=shift, cipher_direction=direction)

    ending = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()

    if ending != 'yes':
        end = True
        print("Thanks for using the program!\nGoodbye.")


