''' Functions | Assignment-1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year
#if a person only pays the minimum monthly payment required by the
# credit card company each month.'''
def paying_debt_off_in_a_year(balance, annual_interest_rate, monthly_payment_rate):
    ''' Input = balance , annual_interest_rate, monthly_payment_rate
        returns:remaning balance at the end of one year''' 
    var = 1
    while var <= 12:
        monthly_interest_rate = (annual_interest_rate)/12.0
        minimum_monthly_payment = (monthly_payment_rate) * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate*monthly_unpaid_balance
        balance = updated_balance_each_month
        var += 1
    return round(updated_balance_each_month,2)


def main():
    '''to find the remaining balance at the end of a year.'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:",paying_debt_off_in_a_year(data[0],data[1],data[2]))

if __name__ == "__main__":
    main()

