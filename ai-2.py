import re
import math

def calculate(text):
    # Use regular expressions to extract numbers and operators from input text
    numbers = re.findall(r'\d+', text)
    operator = re.findall(r'[\+\-\*/]', text)

    # Check if input text contains any math functions like sqrt or sin
    func = re.findall(r'(sqrt|sin|cos|tan)', text)
    
    # Convert numbers to floats and perform calculation based on operator and function
    if len(func) > 0:
        if func[0] == "sqrt":
            result = math.sqrt(float(numbers[0]))
        elif func[0] == "sin":
            result = math.sin(float(numbers[0]))
        elif func[0] == "cos":
            result = math.cos(float(numbers[0]))
        elif func[0] == "tan":
            result = math.tan(float(numbers[0]))
    else:
        result = eval(numbers[0] + operator[0] + numbers[1])

    # Return the result as a string
    return str(result)

# Example usage
while True:
    input_text = input("What would you like to calculate? ")
    result = calculate(input_text)
    print(result)

