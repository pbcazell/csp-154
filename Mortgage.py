class Mortgage:
    def __init__(self):
        self.Principle=100000
        self.Rate=4.5
        self.Term=30

    def GetPayment(self):
        L = self.Principle
        c = (self.Rate / 12 ) / 100
        n = self.Term * 12
        
        #http://www.mtgprofessor.com/formulas.htm
        #P = L[c(1 + c)n]/[(1 + c)n - 1]      
        return (L*(c*((1+c)**n))) / (((1+c)**n)-1) 