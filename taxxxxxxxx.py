
class person():
    def __init__(self,name,tax_file_no,ic_no):
        self.__name = name
        self.__tax_file_no = tax_file_no
        self.__ic_no = ic_no

    def getname(self):
        return self.__name
    def gettax_file_no(self):
        return self.__tax_file_no
    def getic_no(self):
        return self.__ic_no


class taxpayer(person):
    def __init__ (self,name,tax_file_no,ic_no,gross_income,bonus,commission,marital_status,child_num):
        super().__init__(name,tax_file_no,ic_no)
        self.calculate=total_tax(marital_status,child_num)
        self.gross_income = gross_income
        self.bonus = bonus
        self.commission = commission
        self.total_income = 0
        self.marital_status = marital_status
        self.child_num = child_num

    def calculate_total_income(self):
        self.total_income = self.gross_income + self.bonus + self.commission
        self.calculate.total_income = self.total_income
        print("total income : ", self.total_income)

    def display_summary(self):
        print("Name:",self.getname())
        print("Tax File No:",self.gettax_file_no())
        print("IC No:",self.getic_no())
        print("total income:",self.total_income)
        self.calculate.display_summary()

class tax_relief():
    def __init__(self, marital_status,child_num):
        self.total_tax_relief=0
        self.child_num = child_num
        self.marital_status = marital_status
    def calculate_tax_relief(self,relief_types):
        if relief_types == 1:
            sd = float(input("Enter the self and dependent relief : "))
            if sd <= 7000:
                self.total_tax_relief += sd
            else:
                self.total_tax_relief += 7000
        elif relief_types == 2:
            efs = float(input("Enter the Education Fees: "))
            if efs <= 7000:
                self.total_tax_relief += efs
            else:
                self.total_tax_relief += 7000
        elif relief_types == 3:
            li = float(input("Enter the Life Insurance(self/spouse): "))
            if li <= 3000:
                self.total_tax_relief += li
            else:
                self.total_tax_relief += 3000
        elif relief_types == 4:
            med = float(input("Enter the Medical Expenses: "))
            if med <= 8000:
                self.total_tax_relief += med
            else:
                self.total_tax_relief += 8000
        elif relief_types == 5:
            ls = float(input("enter the lifestyle expenses : "))
            if ls <= 5000:
                self.total_tax_relief += ls
            else:
                self.total_tax_relief += 5000
        elif relief_types == 6:
            se = float(input("enter the Sports Equipment expenses: "))
            if se <= 500:
                self.total_tax_relief += se
            else:
                self.total_tax_relief += 500
        elif relief_types == 7:
            dt = float(input("enter the domestic travel expenses: "))
            if dt <= 1000:
                self.total_tax_relief += dt
            else:
                self.total_tax_relief += 1000
        elif relief_types == 8:
            ev = float(input("enter the EV Charging Facilities expenses: "))
            if ev <= 2500:
                self.total_tax_relief += ev
            else:
                self.total_tax_relief += 2500
        elif relief_types == 9:
            for i in range(self.child_num):
                ocl = float(input("enter the ordinary child relief: "))
                if ocl <= 2000:
                    self.total_tax_relief += ocl
                else:
                    self.total_tax_relief += 2000
        elif relief_types == 10:
            for i in range(self.child_num):
                dcl = float(input("enter the disabled child relief: "))
                dc_age = int(input("enter the age of the child:"))
                marital_status = input("enter the marital status(married/unmarried) : ").lower()
                if dc_age > 18 and marital_status == "unmarried":
                    if dcl <= 6000:
                        self.total_tax_relief += dcl
                    else:
                        self.total_tax_relief += 6000
                else:
                    dcl = 0
        elif relief_types == 11:
            bfe = float(input("enter the Breastfeeding Equipment expenses: "))
            wor = input("are you working(yes/no) ").lower()
            bfr = input("have you claimed this last year(yes/no) : ").lower()
            if bfr == "no":
                if bfe <= 2000:
                    self.total_tax_relief += bfe
                else:
                    self.total_tax_relief += 2000
            else:
                bfe = 0
        elif relief_types == 12:
            for i in range(self.child_num):
                efc = float(input("enter the Education Fees for child: "))
                dc_age = int(input("enter the age of the child:"))
                marital_stat = input("enter the marital status(married/unmarried) : ").lower()
                if dc_age > 18 and marital_stat == "unmarried":
                    if efc <= 8000:
                        self.total_tax_relief += efc
                    else:
                        self.total_tax_relief += 8000
                else:
                    efc = 0
        elif relief_types == 13:
            din = float(input("enter the Disability relief(self/spouse) : "))
            if din <= 6000:
                self.total_tax_relief += din
            else:
                self.total_tax_relief += 6000
        elif relief_types == 14:
            pen = float(input("enter the Pension relief: "))
            if pen <= 4000:
                self.total_tax_relief += pen
            else:
                self.total_tax_relief += 4000
        elif relief_types == 15:
            ssf = float(input("enter the Social Security Fund: "))
            if ssf <= 350:
                self.total_tax_relief += ssf
            else:
                self.total_tax_relief += 350
        elif relief_types > 16:
            print("invalid input")
        print("total tax relief amount : ", self.total_tax_relief)

class total_tax(tax_relief):
    def __init__(self, marital_status,child_num):
        super().__init__(marital_status,child_num)
        self.total_income = 0
        self.taxable_income = 0
        self.tax = 0
    def calculate_taxable_income(self):
        self.taxable_income = self.total_income - self.total_tax_relief
        if self.taxable_income <= 0:
            self.taxable_income = 0
        print("total taxable income : ", self.taxable_income)
    def calculate_tax(self):
        if self.taxable_income <= 5000:
            self.tax = 0
            print("no tax")
        elif 5000 < self.taxable_income <= 20000:
            self.tax = (self.taxable_income - 5000) * 0.01
            print("the total tax is : ", self.tax)
        elif 20000 < self.taxable_income <= 35000:
            self.tax = 150 + (self.taxable_income - 20000) * 0.03
            print("the total tax is : ", self.tax)
        elif self.taxable_income > 35000:
            self.tax = 600 + (self.taxable_income - 35000) * 0.08
            print("the total tax is : ", self.tax)

    def display_summary(self):
        print("total tax relief amount : ", self.total_tax_relief)
        print("total taxable income : ", self.taxable_income)
        print("total tax : ", self.tax)

list1=[]
while True:
    taxpayer_name=input("Enter the name: ")
    taxpayer_tax_file_no=input("Enter tax file number: ")
    taxpayer_ic_no=input("Enter IC NO: ")
    gross_income= float(input("enter the gross income: "))
    bonus= float(input("enter the bonus: "))
    commission= float(input("enter the commission: "))
    marital_status = input("enter the marital status (married/unmarried): ").lower()
    if marital_status == 'married':
        child_num = int(input("enter the number of children: "))
    else:
        child_num = 0
    a = taxpayer(taxpayer_name, taxpayer_tax_file_no, taxpayer_ic_no, gross_income, bonus, commission, marital_status,child_num)

    while True:
        print('''1.Self and Dependent \n
                2.Education Fees (Self) \n
                3.Life Insurance (Self & Spouse) \n
                4.Medical Expenses \n
                5.Lifestyle (For each category: non-technology and technology) \n
                6.Sports Equipment \n
                7.Domestic Trave \n
                8.EV Charging Facilities \n
                9.Ordinary Child Relief \n
                10.Disabled Child Relief (Unmarried child, age over 18) \n
                11.Breastfeeding Equipment (Working_women, once over 2 years) \n
                12.Education Fee for Child (Unmarried child, ago over 18 \n
                13.Disability (or each category disabled individual, basic supporting equipment disabled spouse) \n 
                14.Pension(EPf) \n
                15.Social Security Fund (608CO/EIS) \n
                16.exit \n''')
        relief_types = int(input("Enter the tax reliefs: "))
        a.calculate.calculate_tax_relief(relief_types)
        if relief_types == 16:
            break
    a.calculate_total_income()
    a.calculate.calculate_taxable_income()
    a.calculate.calculate_tax()
    #a.display_summary()
    list1.append(a)
    ans = input("Do you wish to continue (yes/no): ")
    if ans == "no":
        break

for i in list1:
    i.display_summary()
    print()



