from tenor.pitch import pitches

piano = {}

for i in range(88):
    note_alias = pitches[i % 12]
    octave_register = i // 12
    # Add 1 to the octave register after the 3rd key since the register starts with C
    if i > 2:
        octave_register += 1
    piano[i] = note_alias + str(octave_register)
