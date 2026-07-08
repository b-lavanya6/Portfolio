# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190,
    "NFLX": 650
}


def display_available_stocks():
    """Display available stocks and their prices."""
    print("\nAvailable Stocks:")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock:<10} : ${price}")

    print("-" * 30)


def create_portfolio():
    """Collect stock information from the user."""
    portfolio = {}

    while True:
        stock_name = input(
            "\nEnter Stock Symbol (or type 'done' to finish): "
        ).upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Invalid stock symbol. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        except ValueError:
            print("Please enter a valid numeric quantity.")

    return portfolio


def calculate_investment(portfolio):
    """Calculate and display portfolio value."""
    total_value = 0

    print("\n")
    print("=" * 60)
    print("                PORTFOLIO SUMMARY")
    print("=" * 60)

    print(f"{'Stock':<10}{'Quantity':<12}{'Price($)':<12}{'Value($)':<12}")
    print("-" * 60)

    for stock, quantity in portfolio.items():
        value = quantity * stock_prices[stock]
        total_value += value

        print(
            f"{stock:<10}{quantity:<12}{stock_prices[stock]:<12}{value:<12}"
        )

    print("-" * 60)
    print(f"Total Portfolio Value: ${total_value}")
    print("=" * 60)

    return total_value


def save_to_file(portfolio, total_value):
    """Save portfolio details to a text file."""

    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(
            f"{'Stock':<10}{'Quantity':<12}{'Price($)':<12}{'Value($)':<12}\n"
        )

        file.write("-" * 50 + "\n")

        for stock, quantity in portfolio.items():
            value = quantity * stock_prices[stock]

            file.write(
                f"{stock:<10}{quantity:<12}{stock_prices[stock]:<12}{value:<12}\n"
            )

        file.write("-" * 50 + "\n")
        file.write(f"Total Portfolio Value: ${total_value}\n")

    print("\nPortfolio report successfully saved as 'portfolio_report.txt'")


def main():
    """Main program execution."""

    print("=" * 60)
    print("          STOCK PORTFOLIO TRACKER SYSTEM")
    print("=" * 60)

    display_available_stocks()

    portfolio = create_portfolio()

    if not portfolio:
        print("\nNo stocks were added to the portfolio.")
        return

    total_value = calculate_investment(portfolio)

    choice = input(
        "\nDo you want to save the report to a file? (yes/no): "
    ).lower()

    if choice == "yes":
        save_to_file(portfolio, total_value)

    print("\nThank you for using Stock Portfolio Tracker.")


# Program Entry Point
if __name__ == "__main__":
    main()
