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
        #choose = input("What variant you choose?[M/W/D] ").upper()
        self.p = self.payment
        #fix per month
        #if choose == "M":
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
            self.p = self.p + (self.p * (self.r))
            self.p -= install
            #print("%.2f" % self.p)
            balance.append(self.p)
        return balance
            
    def amount_paid(self):
        install = self.fx_inst()
        self.p = self.payment
        paids = []
        while self.p > 0:
            self.p -= install
            install = install + self.fx_inst()
            paids.append(install)
        return paids

            

            



    def __str__(self) -> str:
        print("\n")
        print(f"Fixed installment is: {self.fx_inst():.2f}")
        print("Remaining balance is: \n_______________\n")
        print("Month".ljust(10), "Remaining Bal.".ljust(15), "Amount Paid".ljust(5))
        for month, rem in enumerate(self.remaining_balance(), 1): #, self.amount_paid()   remember to zip values
            amount = self.fx_inst() * month
            print(str(month).ljust(10), f"{rem:.2f} PLN","    ", str("%.2f" % amount).ljust(5)) #,str(tow).ljust(4) 
        return "Done"
            

    


    
        

    


if __name__ == "__main__":
   m_calc = MortgageCalculator()
   
   print(str(m_calc))

