import re

def calculate(text):
    # Use regular expressions to extract numbers and operators from input text
    numbers = re.findall(r'\d+', text)
    operator = re.findall(r'[\+\-\*/]', text)

    # Convert numbers to floats and perform calculation
    result = eval(numbers[0] + operator[0] + numbers[1])

    # Return the result as a string
    return str(result)

# Example usage

text = input("enter your calculation")

input_text = text
result = calculate(input_text)
print(result)

