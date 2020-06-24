import re
class Note_Freq:
    def __init__(self, note):
        self.__note = note


    def frequency(self):
        if self.__note.index(' ') != -1:
            return False
        if self.__note[0].isnum():
            return False
        if self.__note[0]=='#':
            return False
        regex = re.compile('''[@_!$%^&*()<>?/\|}{~:]''')
        if (regex.search(self.__note) != None):
            return False
        keys = ["A", "A#", "B", "C", "C#", "D",
                "D#", "E", "F", "F#", "G", "G#"]
        octave_number = self.__note[2:]
        key = self.__note[:2].upper()
        jumps = octave_number - 4
        N = keys.index(key) + jumps * 12
        return 440 * pow(2, N/12)


