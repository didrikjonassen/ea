import random

class binary_genotype():
	gene = None
	mutation = None

	def __init__(this, length, mutation = mutate_bitwise):
		this.gene = [random.randint(0,1) for i in xrange(length)]
		this.mutation = mutation
	
	def generate_gene(this, length):
		this.gene = [random.randint(0,1) for i in xrange(length)]
	
	def set_gene(this, gene):
		this.gene = gene
		
	def crossover(this, that, num_points, prob):
		points = random.sample(xrange(1, len(this.gene) - 1)) + [len(this.gene)]
		points.sort()
		genomes = [this, that]
		start = 0
		result = []
		phase = 0
		for point in points:
			stop = point
			result += genomes[phase].gene[start:stop]
			start = point
			if random.random() < prob:
				phase = (phase + 1) % 2
		return result
	
	def mutate_bitwise(this, prob):
		for i in xrange(len(this.gene)):
			if random.random() < prob:
				this.gene[i] = 0 if this.gene[i] == 1 else 1
	
	def mutate_genewise(this, prob):
		if random.random() < prob:
			i = random.randint(0, len(this.gene) - 1)
			this.gene[i] = 0 if this.gene[i] == 1 else 1
		
	def develop_intlist(this, bits):
		result = []
		for i in xrange(0, len(this.gene), bits):
			substr = this.gene[i: i + bits]
			val = 1
			integer = 0
			for bit in substr[::-1]:
				integer += bit * val
				val *= 2
			result += [integer]
		return result
