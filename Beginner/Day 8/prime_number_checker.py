def prime_checker(number):
	is_prime = True
	for i in range(2, number - 1):
		if number % i == 0:
			is_prime = False
	if is_prime:
		return f"{number} is a prime number"
	else:
		return f"{number} is not a prime number"
