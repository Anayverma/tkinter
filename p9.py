# python program in which a class is defined, then create object 
# call simple ‘print function’ defined in class.

class A:# created class A
    sentence="" # class variables
    def __init__(self,sen) :
        self.sentence=sen
    def print(self): #  defining main function 
        print(self.sentence)
    def main(sen):
        a = A(sen)
        a.print() #calling print function
A.main(input("Enter messaged to be printed -->\n"))
# calling main function 

