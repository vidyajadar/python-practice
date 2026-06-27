class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +", self.img,"j")

    def add(self, num2):
        newReal = self.real +num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,8)
num1.shownumber()

num2 = Complex(3,5)
num2.shownumber()

num3 = num1.add(num2)
num3.shownumber()