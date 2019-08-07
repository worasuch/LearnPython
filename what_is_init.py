class Person:
    def __init__(self, fname=None, lname=None, country="Thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname, self.lname, self.country)

if __name__ == '__main__':
    p1 = Person()
    print(p1)

    p2 = Person(country="China", lname="Haomachai", fname="Worasuchad")
    print(p2.fname)
    print(p2.lname)