def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
    num = int(input("enter a nuber:"))
    if num < 0:
      print("factorial is not defined for negative numbers.")
    elif num == 0:
      print("the factorial of 0 is 1")
    else:
      result = factorial(num)
      print(f"the factorial of {num}is{result}")
