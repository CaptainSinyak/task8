import math


def factorization(n):  # функция для разложения числа на простые множители
	if n < 0:
		result = "error, try again"
	else:
		result = str(math.factorial(n))
	return result
