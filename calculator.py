number1 = ${{ github.inputs.number1 }}
number2 = ${{ github.inputs.number2 }}
operator = ${{ github.inputs.operator }}

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    print("Invalid Operator!")
