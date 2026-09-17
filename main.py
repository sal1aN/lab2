def calculate_deposit(deposit, annual_percentage, term=24):
    #Депозит у складних відсотках
    month_percantage = annual_percentage / 12 / 100
    for i in range(term):
        deposit += month_percantage * deposit
        print(f"Month {i}: {deposit:.2f}")
    print(f"Final deposit value: {deposit:.2f}")
    return deposit

def run():
    is_running = True
    while is_running:
        try:
            deposit = int(input("Enter the deposit amount: "))
        except ValueError:
            print("Please enter a numeric value")
            print()
            continue
        try:
            annual_percentage = int(input("Enter the annual percentage: "))
        except ValueError:
            print("Please enter a numeric value")
            print()
            continue
        enter_term = input("Do yo want to enter term(y/n): ")
        if enter_term == "y":
            try:
                term = int(input("Enter the term of deposit: "))
            except ValueError:
                print("Please enter a numeric value")
                print()
                continue
            calculate_deposit(deposit, annual_percentage, term)
        else:
            calculate_deposit(deposit, annual_percentage)
        con = input("Do you wish to continue? (y/n)")
        if not con == "y":
            is_running = False
    return

if __name__ == '__main__':
    run()