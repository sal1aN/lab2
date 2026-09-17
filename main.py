def calculate_deposit(deposit, annual_percentage, term=24):
    #Депозит у складних відсотках
    month_percantage = annual_percentage / 12 / 100
    for i in range(term):
        deposit += month_percantage * deposit
        print(f"Month {i}: {deposit:.2f}")
    print(f"Final deposit value: {deposit:.2f}")
    return deposit

def verify(value, prompt):
    verified = True
    while verified:
        try:
            verified = False
            value = int(input(prompt))
        except ValueError:
            verified = True
            print("Please enter a numeric value")
            print()
    return value

def run():
    is_running = True
    deposit, annual_percentage, term = 0, 0, 0
    while is_running:
        deposit = verify(deposit, "Enter the deposit amount: ")
        annual_percentage = verify(annual_percentage, "Enter the annual percentage: ")
        enter_term = input("Do yo want to enter term(y/n): ")
        if enter_term == "y":
            term = verify(term, "Enter the term of deposit: ")
            calculate_deposit(deposit, annual_percentage, term)
        else:
            calculate_deposit(deposit, annual_percentage)
        con = input("Do you wish to continue? (y/n)")
        if not con == "y":
            is_running = False
    return

if __name__ == '__main__':
    run()