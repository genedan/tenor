from tenor.pitch import pitches


class OctaveRegister:
    def __init__(self, register: int):
        self.register = register
        self.pitches = [pitch + str(register) for pitch in pitches]