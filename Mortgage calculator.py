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


    
        

    def fx_inst(self):
        self.p = self.payment
    #    choose = input("What variant you choose?[M/W/D] ").upper()
        #fix per month
    #    if choose == "M":
        self.r = self.rate / self.PERCENT / self.MONTH_IN_YEARS
        self.n = self.loan * self.MONTH_IN_YEARS
        #fix per week
        # elif choose == "W":
        #     self.r = self.rate / self.PERCENT / self.WEEK_IN_YEARS
        #     self.n = self.loan * self.WEEK_IN_YEARS
        #fix per day
        # elif choose == "D":
        #     self.r = self.rate / self.PERCENT / self.DAY_IN_YEARS
        #     self.n = self.loan * self.DAY_IN_YEARS
        #calculations
        self.part = ((1 + self.r)** self.n)
        self.t = (self.p * self.r * self.part)/(self.part - 1)
        return self.t
        
    def remaining_balance(self):
        balance = []
        self.p = self.payment
        #we need a vlue from previous def
        install = self.fx_inst()
        while  self.p > 0: 
            self.p = self.p + (self.p * (self.rate / self.PERCENT / self.MONTH_IN_YEARS))            
            self.p -= install
            #print("%.2f" % self.p)
            balance.append(self.p)
        return balance
            

            

            



    def __str__(self) -> str:
        print("Remaining balance is: \n_______________\n")
        balance = []
        for month,rem in enumerate(self.remaining_balance(), 1):
            print(month,"        ", f"{rem:.2f}")
        return "Done"
            

    def decrease_inst(self):
        pass


    
        

    


if __name__ == "__main__":
   m_calc = MortgageCalculator()
   
   print(str(m_calc))

