import morse
import sys


morse_codes = morse.morse_equiv


def converter(text):
    print("Converting....")
    converted_text = ""
    for letter in text:
        for (key,value) in morse_codes.items():
            if letter == key:
                converted_text += value
        if letter == " ":
            converted_text += "| "

    return converted_text


print("#####\tTEXT TO MORSE CODE\t#####")
user_input = input("Text: ").upper()
print(converter(text = user_input))



sys.exit(0)