def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Inputs must be numbers"

result = function(5, '10')
print(result)

result = function(5, 10)
print(result)