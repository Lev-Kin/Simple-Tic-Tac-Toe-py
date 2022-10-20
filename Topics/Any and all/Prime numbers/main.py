prime_numbers = [i for i in range(2, 1000) if all(i % n != 0 for n in range(2, i))]


