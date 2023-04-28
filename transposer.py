NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
results = []

def transpose_note(note, semitones):
    note_index = NOTES.index(note.upper())
    new_note = note_index + semitones
    while new_note > 11:
        new_note -= 12
    while new_note < 0:
        new_note += 12
    return NOTES[new_note]

def program():
    notes_str = input('\nEnter notes to be transposed seperated by spaces:\n\n')
    semitones = int(input('\nEnter transposition in semitones:\n\n'))
    result = []
    for note in notes_str.split(' '):
        result.append(transpose_note(note, semitones))
    results.append('\n%s ---> %s' % (notes_str.upper(), ' '.join(result)))
    print(''.join(results))

program()

while input('\nAgain? (Y/N)\n\n').upper() == 'Y':
    program()