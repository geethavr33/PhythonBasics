class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words


reverser = StringReverser("the sky is blue ")
reverser1 = StringReverser("the sky is blue in color ")
reversed_string = reverser.reverse_words()
reversed_string1 = reverser1.reverse_words()
print(reversed_string)
print(reversed_string1)
