class Human:
    """Example class"""

    def __init__(self, gender, name):
        """Make a virtual human.

        :param sex: gender of human.
        :param name: name of human.
        """
        self.gender = gender
        self.name = name

    def speak(self, words):
        """speak some words.

        :param words: words to speak.
        :return: None
        """
        print(words)

    def get_intro(self):
        """get man's introduction.

        :return: self introduction string.
        """
        return f"Name: {self.name};Gender: {self.gender}"

    def test_google_docstring_style(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
        return True

    def test_numpy_docstring_style(arg1, arg2):
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value

        """
        return True


def main(name):
    print(f"Hi, {name}")


# Put code with side effect below
if __name__ == "__main__":
    main("World")
