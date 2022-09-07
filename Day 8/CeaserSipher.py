from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(ceaser_text, shift_amount, cipher_direction):
    message = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in ceaser_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_position = position + shift_amount
            message += alphabet[new_position]
        else:
            message += letter
    print(f"The {cipher_direction}d text is {message}")

print(logo)

while input("Would you like to go again? answer yes or no.") == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if shift > 26:
    shift = shift % 26
ceasar(ceaser_text=text, shift_amount=shift, cipher_direction=direction)
