class CalculationService:
    @staticmethod
    def calculate(operation,x,y):
        if operation == 'add':
            return x + y
        elif operation == 'substract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            if y == 0;
                raise ValueError("Cannot divide by zero")
        else:
            raise ValueError(f"Invalid Opearion : {operation}")