def add_binary(a, b):
	return '{0:08b}'.format(a + b)


print(add_binary(51, 12))


def decimalToBinary(a, b):
	return bin(a + b).replace("0b", "")


print(decimalToBinary(1, 3))


def get_average(marks):
	return sum(marks) // len(marks)


print(get_average([1, 3, 5, 10]))


def square_digits(num):
	digits = [int(x) for x in str(num)]
	pow_digits = [i ** 2 for i in digits]
	final_number = "".join(str(e) for e in pow_digits)
	return int(final_number)


def square_digits(num):
	ret = ""
	for x in str(num):
		ret += str(int(x) ** 2)
	return int(ret)


print((square_digits(9999999)))

from collections import Counter


def find_uniq(arr):
	uniques = Counter(arr)
	for key, value in uniques.items():
		if value == 1:
			return key


def find_uniq(arr):
	a, b = set(arr)
	return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 1, 5, 1, 1]))
