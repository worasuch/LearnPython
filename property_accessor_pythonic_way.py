class Person:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood  # Should have A, B, AB, O

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname.strip().title()

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, blood):
        if blood.upper() in ["A", "B", "AB", "O"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group.")

    def __str__(self):
        return "{!r} {}, blood group: {}".format(self.fname, self.lname, self.blood)

if __name__ == '__main__':
    p1 = Person("   peter ", "Parker", "O")
    print(p1)
    p1.blood = "AB"
    print(p1)