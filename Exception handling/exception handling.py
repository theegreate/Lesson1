class Calculator:
    def _init_(self):
        pass
    
    def calculate_sum(self, x, y):
        return x + y
    
    def calculate_difference(self, x, y):
        return x - y
    
    def calculate_product(self, x, y):
        return x * y
    
    def calculate_quotient(self, x, y):
        try:
            if y == 0:
                raise ValueError("Division by zero is not allowed.")
            return x / y
        except ValueError as e:
            return str(e)

if _name_ == "_main_":
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        calc = Calculator()
        
        result_sum = calc.calculate_sum(number1, number2)
        result_difference = calc.calculate_difference(number1, number2)
        result_product = calc.calculate_product(number1, number2)
        result_quotient = calc.calculate_quotient(number1, number2)
        
        print("Sum:", result_sum)
        print("Difference:", result_difference)
        print("Product:", result_product)
        print("Quotient:", result_quotient)
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")