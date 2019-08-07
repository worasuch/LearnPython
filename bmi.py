class Bmi:
    def __init__(self, w_kg, h_cm):
        self.w_kg = w_kg
        self.h_cm = h_cm

    def bmi(self):
        return self.w_kg / (self.h_cm / 100) ** 2

    def category(self):
        diag = ""
        if self.bmi() < 18.5:
            diag = "Below standard"
        elif 18.5 <= self.bmi() <= 25:
            diag = "Standard"
        elif 25 < self.bmi() <= 30:
            diag = "Above standard"
        elif self.bmi() > 30:
            diag = "Fat"
        return diag

    def __str__(self):
        return "BMI = {:.2f} ({})".format(self.bmi(), self.category())

if __name__ == '__main__':
    a = Bmi(47, 168)
    print(a)