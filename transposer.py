LETTER_NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B')
INT_NOTES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def integer_to_letter(int):
    while int > 11:
        int = int - 12
    while int < 0:
        int = int + 12
    return LETTER_NOTES[int]

def letter_to_integer(letter):
    index = LETTER_NOTES.index(letter)
    return INT_NOTES[index]

def transpose_note(note, semitones):
    before_int = letter_to_integer(note)
    after_int = before_int + semitones
    after_letter = integer_to_letter(after_int)
    return after_letter

notes_str = input('Enter notes to be transposed seperated by spaces: ')
semitones = int(input('Enter transposition in semitones: '))
notes = notes_str.split(' ')
result = []

for note in notes:
    result.append(transpose_note(note, semitones))

print(' '.join(result))

