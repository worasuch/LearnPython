import re

class Person:
    def __init__(self, fname, lname, sex):
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()
        self.sex = sex

    def __str__(self):
        return "{!r} {!r} sex: {}".format(self.fname, self.lname, self.sex)


class Student(Person):
    def __init__(self, s_id, fname, lname, sex):
        super().__init__(fname, lname,sex)
        self.s_id = self.remove_non_digit(s_id)

    def __str__(self):
        return "{} {}".format(self.s_id, super().__str__())

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)

    def email(self):
        return "{}.{}{}@cbs.chula.ac.th".format(self.fname, self.lname[:2], self.s_id[:2])

class ExchangesStudent(Student):
    def __init__(self, s_id, fname, lname, sex, partner_univ):
        super().__init__(s_id, fname, lname, sex)
        self.partner_univ = partner_univ

    def __str__(self):
        return "{} {}".format(super().__str__(), self.partner_univ)


if __name__ == '__main__':
    s1 = Student("1234", " fon", "Sairoong", "F")
    print(s1)
    print(s1.email())
    s2 = ExchangesStudent("4567", "Peter ", "Parker", "M","ABC Univ")
    print(s2)
    print(s2.email())
