# Mortgage Calculator

class MortgageCalculator:

    def __init__(self):
        self.payment = int(input("What amount of payment you need?: "))
        self.rate = float(input("What's the interest rate?: "))
        self.loan = int(input("What is the duration of the mortgage?: "))
        self.item = int(input("What is the cost of the home? "))
        self.PERCENT = 100
        self.MONTH_IN_YEARS = 12
        self.WEEK_IN_YEARS =  52
        self.DAY_IN_YEARS = 365


    def __str__(self) -> str:
        return """
        
        MORTGAGE CALCULATOR MENU
              
            P x r (1+r)^n
        m = --------------
            (1 + r)^n - 1
"""
        

    def mortgage_calc(self):
        choose = input("What variant you choose?[M/W/D] ").upper()
        if choose == "M":
            self.p = self.payment
            self.r = self.rate / self.PERCENT / self.MONTH_IN_YEARS
            self.n = self.loan * self.MONTH_IN_YEARS
            #part of code to short
            self.part = ((1 + self.r)** self.n)
            self.t = (self.p * self.r * self.part)/(self.part - 1)
            return self.t


    def decrease_inst(self):
        pass


    
        

    


if __name__ == "__main__":
   m_calc = MortgageCalculator()
   print(m_calc.mortgage_calc())

