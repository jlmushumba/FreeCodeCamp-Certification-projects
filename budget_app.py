class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
      

    def deposit(self, amount, description = ""):

        self.ledger.append({'amount'  : amount, 'description' : description})
    

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount'  : - amount, 'description' : description})

        return True
       

    def get_balance(self):
        balance = sum(item.get("amount") for item in self.ledger)
        return balance
        

    def transfer(self, amount, other):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, description=f"Transfer to {other.name}")
        other.deposit(amount, description = f"Transfer from {self.name}")

        return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        result = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            result += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"

        result += f"Total: {self.get_balance():.2f}"

        return result
        

def create_spend_chart(categories):
    # Calculate how much was spent in each category
    spent_amounts = []

    for category in categories:
        spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])

        spent_amounts.append(spent)

    # Total amount spent across all categories
    total_spent = sum(spent_amounts)

    # Calculate percentages rounded down to nearest 10
    percentages = []

    for spent in spent_amounts:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((spent / total_spent) * 100) // 10 * 10

        percentages.append(percentage)

    # Start the chart
    result = "Percentage spent by category\n"

    # Y-axis and bars
    for level in range(100, -1, -10):
        result += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                result += "o"
            else:
                result += " "

            result += "  "

        result += "\n"

    # Horizontal line
    result += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Vertical category names
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        result += "     "

        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "

        result += "\n"

    return result.rstrip("\n")
