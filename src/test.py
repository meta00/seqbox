class Person:
    """ Class docstrings """
    def __init__(self, name, language):
        """ Paramaters
            ----------
            name: str
                Name of the person
            language: str
                The language used by the person
        """

        self.name = name
        self.language = language

    def say_hello(self, language = None): 
        """Say hello to the person in a language
            Parameters
            ----------
            language: str
                The language to be used (default is English)
            Raises
            ----------
            NotImplementedError
                If language is set or passed in as a
            parameter. 
        """

        if self.language is None and language is None:
            raise NotImplementedError("No language is set")
        say_language = self.language if language is None else language
        print(say_language)
        print(language)
        if say_language == "Vietnamese":
            print(f"Chao ban {self.name}")
        else:
            print(f"Hello {self.name}")
        return self

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

def main():
    hai = Person("Hai", "Vietnamese")
    hai.say_hello()
    print(hai.language)
    rectangle = Shape(100,45)
    print(rectangle.area())

if __name__ == "__main__":
    main()