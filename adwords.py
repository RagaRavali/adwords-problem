import sys
import math
import csv
import random
from random import shuffle
from math import exp



if len(sys.argv) != 2:
	sys.exit()

alg = sys.argv[1] ##inspired from previous projects template given

def greedy(add_list):
	for i in add_list:
		if i[2] == max(j[2] for j in add_list):
			#print i
			return i
def msvv(advertiser, temp, budget):
	func = []
	val = 0.0
	for i in advertiser:
		formula = 1 - math.exp((temp[i[0]]-budget[i[0]])/temp[i[0]]-1)
		if(float(i[2])*formula) > val:
			val = float(i[2])*formula
			func = i
	return func

def balance(advertiser,budget):
	final = []	
	value = 0.0
	for i in advertiser:
		if budget[i[0]] > value:
			value = budget[i[0]]
			final = i
	#print final	
	return final

def main():
	query_data = open('queries.txt')
	query = []
	for i in query_data:
		query.append(i.replace("\n",""))
	
	
	bidder_data = csv.reader(open('bidder_dataset.csv'))
	bidder =[]
	for i in bidder_data:
		bidder.append(i)
	budget = {}
	for i in bidder[1:]:
		if(i[3]):
			budget[i[0]] = float(i[3])
	temp = budget.copy()
	total = sum(budget.values())	
	#print total

        advertiser = []
	ratio = 0.0
	for q in query:
	        advertiser = find_add(budget,[x for x in bidder if x[1] == q])
		if len(advertiser)>=1:
			if alg == "greedy":
				select = greedy(advertiser)
			elif alg == "msvv":
				select = msvv(advertiser,temp,budget)
			elif alg == "balance":
				select = balance(advertiser,budget)

			temp1 = float(select[2])
			ratio = temp1+ratio
			budget[select[0]] -= temp1
	print "revenue:" 
	print ratio		
	#print advertiser

	advertiser_random = []

	for i in range(1,101):
		ratio = 0.0
		random.seed(0)
		shuffle(query)
		bud = temp.copy()
		for q in query:
	        	advertiser = find_add(bud,[i for i in bidder if i[1] == q])
			if len(advertiser)>=1:
				if alg == "greedy":
					select = greedy(advertiser)
				elif alg == "msvv":
					select = msvv(advertiser,temp,bud)
				elif alg == "balance":
					select = balance(advertiser,bud)
				temp1 = float(select[2])
				ratio = temp1+ratio
				bud[select[0]] -= temp1
		advertiser_random.append(ratio)
	num = min(advertiser_random)
	#print str(num/ratio)
	print  "competitive ratio:"
	print num/total
		
def find_add(budget,bidder): ##for each bidding, we will find which is suitable
	temp = []
	for i in bidder:
		if budget[i[0]] >= float(i[2]):
			temp.append(i)
	return temp

if __name__ == "__main__":
	main()




