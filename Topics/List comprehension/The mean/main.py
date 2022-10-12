strings = input()
floats = [float(num) for num in strings]
result = sum(floats) / len(floats)
print(result)
