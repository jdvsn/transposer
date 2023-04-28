LETTER_NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B')
INT_NOTES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def integer_to_letter(int):
    return LETTER_NOTES[int]

def letter_to_integer(letter):
    index = LETTER_NOTES.index(letter)
    return INT_NOTES[index]

before_letter = input("Enter note to be transposed:")
before_int = letter_to_integer(before_letter)

semitones = int(input("Enter degree of transposition:"))

after_int = before_int + semitones
after_letter = integer_to_letter(after_int)

print(after_letter)

