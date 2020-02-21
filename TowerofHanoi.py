
def funcounter():				#To count the number of times the function has been called recursively
    funcounter.counter += 1

# Recursive Python function to solve tower of hanoi
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
	funcounter()
	if n == 1: 
		print ("Move disk 1 from rod",from_rod,"to rod",to_rod) 
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
	print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 	

# Driver code 
n=int(input("Enter the number of discs : "))
funcounter.counter=0
TowerOfHanoi(n, 'A', 'C', 'B')
print("\nTotal Number of Steps : ",funcounter.counter)
# n is the number of discs
# A, C, B are the name of rods A is the source and C is the final Destnation
# Counter is used to find the number of iterations 
