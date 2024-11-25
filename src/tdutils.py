import random

def generate_ID():
	alpha_num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	ID = ''.join([alpha_num[random.randint(0,35)] for _ in range(5)])
	return ID