import matplotlib.pyplot as plt

def find_primes_in_range(start, stop):
	primes = []
	# print("checking range " + str(start) + " " + str(stop))
	for num in range(start, stop):
		if(is_prime(num)):
			primes.append(num)
	# print("found these primes = " + str(primes))
	return primes

def is_prime(x):
	if x == 2 or x == 3:
		return True
	if x%2 == 0 or x < 2:
		return False
	for div in range(3, int(x**.5)+1, 2):
		if x%div == 0:
			return False
	return True

def range_calc(num, divisions):
	ranges = []
	for x in range(int(num/divisions), num+1, int(num/divisions)):
		ranges.append(str(x-int(num/divisions)) + "-" + str(x))
	return ranges
	
def prime_count(num, divisions):
	count = []
	for x in range(int(num/divisions), num+1, int(num/divisions)):
		count.append(len(find_primes_in_range(x-int(num/divisions), x)))
		# print(count)
	return count


def main():
	# primes = []
	# primes = find_primes_in_range(10000)
	number = int(input("What is the max number across which you want to look for primes? "))
	divisions = 10
	ranges = range_calc(number, divisions)
	primes_dist = prime_count(number, divisions)
	print(ranges)
	print(primes_dist)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.bar(ranges, primes_dist)
	
	plt.show()

if __name__ == "__main__":
	main()