import re
class Note_Freq:
    def __init__(self, note):
        self.__note = note


    def frequency(self):
        if len(self.__note.split(' '))>1:
            return False
        if self.__note[0].isdigit():
            return False
        if self.__note[0]=='#':
            return False
        regex = re.compile('''[@_!$%^&*()<>?/\|}{~:]''')
        if (regex.search(self.__note) != None):
            return False
        keys = ["A", "A#", "B", "C", "C#", "D",
                "D#", "E", "F", "F#", "G", "G#"]

        try:
            octave_number = int(self.__note[2:])
        except ValueError:
            try:
                octave_number = int(self.__note[1:])
            except ValueError:
                return False

        key = self.__note[:2].upper()
        jumps = octave_number - 4
        try:
            N = keys.index(key) + jumps * 12
        except ValueError:
            key = self.__note[:1].upper()
            N = keys.index(key) + jumps * 12
        return round(440 * pow(2, N/12), 2)


