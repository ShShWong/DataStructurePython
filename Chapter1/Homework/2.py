def SalaryCal(SalaryPerHour,OrdinaryWork,ExtraWork):
    return SalaryPerHour*OrdinaryWork + 1.5*SalaryPerHour*ExtraWork


print(SalaryCal(10,40,5))