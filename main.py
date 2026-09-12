def calculate_deposit(deposit, annual_percentage, term=24):
    #Депозит у складних відсотках
    try:
        deposit = int(deposit)
        annual_percentage = int(annual_percentage)
        term = int(term)
    except ValueError:
        print("Please enter a numeric value")
        return False
    month_percantage = annual_percentage / 12 / 100
    for i in range(term):
        deposit += month_percantage * deposit
        print(f"Month {i}: {deposit:.2f}")
    print(f"Final deposit value: {deposit:.2f}")
    return deposit
def run():
    deposit = input("Enter the deposit amount: ")
    annual_percentage = input("Enter the annual percentage: ")
    enter_term = input("Do yo want to enter term(y/n): ")
    if enter_term == "y":
        term = int(input("Enter the term of deposit: "))
        calculate_deposit(deposit, annual_percentage, term)
    else:
        calculate_deposit(deposit, annual_percentage)
    return

if __name__ == '__main__':
    run()