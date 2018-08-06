'''write a program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months.'''
def paying_debt_off_in_a_year(balance, annual_interest_rate):
    '''input balance, annual interest
    returns lowest monthly payment'''
    if balance <= 0:
        return 0
    lowest = 10
    monthly_rate = annual_interest_rate/12.0
    while 1:
        prev_bal = balance
        var = 0
        while var <= 11:
            monthly_balance = prev_bal - lowest
            upd_bal = monthly_balance + monthly_rate*monthly_balance
            prev_bal = upd_bal
            var = var +1
        if monthly_balance <= 0:
            break
        else:
            lowest = lowest + 10
    return lowest
def main():
    '''To find the lowest monthly paymnet '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
