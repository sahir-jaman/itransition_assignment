def max_multiplication(given_string):
    if not isinstance(given_string, str):
        return "nil"

    max_product = 0
    max_combination = None

    for i in range(len(given_string) - 3):
        string_portion = given_string[i:i+4]

        if string_portion.isdigit():
            product = 1
            for digit in string_portion:
                product *= int(digit)

            if product > max_product:
                max_product = product
                max_combination = string_portion

    return max_product if max_combination is not None else "nil"

# Test cases
result1 = max_multiplication('abc12345def')
result2 = max_multiplication('a1b2c3d4e')

print(result1)  # Output: 120
print(result2)  # Output: nil
