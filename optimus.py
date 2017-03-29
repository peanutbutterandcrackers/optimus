#!/usr/bin/python3

import pickle

def save_to_hint_file():
	f = open('primes_hint', 'wb')
	pickle.dump(primes, f)
	f.close()

def load_hint():
	file_exists = True
	try:
		f = open('primes_hint', 'rb')
	except IOError:
		primes = []
		file_exists = False
	if file_exists:
		try:
			primes = pickle.load(f)
		except EOFError:
			primes = []
		f.close()
	return primes

def find_index(element, List):
	index = 0
	while True:
		if List[index] == element:
			return index
		else:
			index += 1

def find_greatest_prime_upto(num):
	index = 0
	while True:
		if primes[index] >= num:
			break
		index += 1
	return primes[index-1]
	
primes = [2, 3]

if len(primes) < len(load_hint()):
	primes = load_hint()

def genprimesupto(num):
	"""Generates primes up to num"""
	if num < 2:
		raise ValueError("Those values do not result in any primes.")
	if num in primes:
		return primes[:(find_index(num, primes) + 1)]
	if num not in primes and num < primes[-1]:
		return primes[:(find_index(find_greatest_prime_upto(num), primes) + 1)]
	else:
		n = (primes[-1] + 2)
		while n <= num:
			for prime in primes:
				rem = n % prime
				if rem == 0:
					break
				elif rem != 0 and prime == primes[-1]:
					primes.append(n)
				else:
					pass
			n += 2
		save_to_hint_file()
		return primes

def primefactorsof(num):
	"""Returns a list of prime factors of num"""
	primefactors = []
	while num not in primes:
		for prime in primes:
			if num % prime == 0:
				primefactors.append(prime)
				num /= prime
				break
			else:
				pass
	primefactors.append(int(num))
	return primefactors
