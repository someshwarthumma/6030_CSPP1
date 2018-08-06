''' Functions - Assignment-3 - Using Bisection Search to find lowest payment Faster'''
def paying_debt_off_in_a_year(balance, annual_interest_rate):
    if balance <= 0:
        return 0
    monthly_rate = annual_interest_rate/12
    lower_bound = balance/12
    upper_bound = (balance*(1 +monthly_rate)**12)/12
    lowest_payment = (lower_bound+upper_bound)/2
    epsilon= 0.03
    while abs(balance) > epsilon:
        lowest_payment = (lower_bound+upper_bound)/2
        prev_bal = balance
        var = 0
        while var <= 11:
            monthly_balance = prev_bal - lowest_payment
            upd_bal = monthly_balance + (monthly_rate*monthly_balance)
            prev_bal = upd_bal
            var = var+1
        if monthly_balance>epsilon:
            lower_bound = lowest_payment
        elif monthly_balance<-epsilon:
            upper_bound = lowest_payment
        else:
            break
    return str(round(lowest_payment, 2))

def main():
    ''''To find the lowest monthly payment usng bisection method '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
