# your code goes here!

class Anagram:
    def __init__(self, name):
        self.name = name

    def match(self,value):
        new_list = []
        for elem in value:
            if sorted(list(self.name))==sorted(list(elem)):
                new_list.append(elem)
        return new_list