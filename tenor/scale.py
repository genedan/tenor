from tenor.pitch import raw_pitches

circle_of_fifths = {
    '0': 'C',
    '1#': 'G',
    '2#': 'D',
    '3#': 'A',
    '4#': 'E',
    '5#': 'B',
    '6#': 'F#',
    '7#': 'C#',
    '1b': 'F',
    '2b': 'Bb',
    '3b': 'Eb',
    '4b': 'Ab',
    '5b': 'Db',
    '6b': 'Gb',
    '7b': 'Cb'
}

major_sharps = ['F', 'C', 'G', 'D', 'A', 'E', 'B']

major_flats = ['B', 'E', 'A', 'D', 'G', 'C', 'F']

pitch_modifiers = {
    'Sharp': '#',
    'Flat': 'b'
}


class Scale:
    def __init__(self, key, scale_type):
        self.key = key
        self.scale_type = scale_type

        self.circle_position = next(k for k, v in circle_of_fifths.items() if v == key)

        if len(self.circle_position) == 0:
            self.accidental_type = 'Neutral'
        elif self.circle_position[1] == '#':
            self.accidental_type = "Sharp"
        elif self.circle_position[1] == 'b':
            self.accidental_type = 'Flat'

        self.num_accidentals = int(self.circle_position[0])

        self.degrees = {}
        if self.scale_type == 'major':
            # generate degrees

            if self.accidental_type == "Sharp":
                self.accidentals = major_sharps[0:self.num_accidentals]
            elif self.accidental_type == 'Flat':
                self.accidentals = major_flats[0:self.num_accidentals]
            else:
                self.accidentals = []

            raw_position = raw_pitches.index(self.key[0])
            for i in range(7):
                raw_pitch = raw_pitches[raw_position % 7]
                if raw_pitch in self.accidentals:
                    accidental = pitch_modifiers[self.accidental_type]
                else:
                    accidental = ''
                self.degrees[i + 1] = raw_pitch + accidental
                raw_position += 1