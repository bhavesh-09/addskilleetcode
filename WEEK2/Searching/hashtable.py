def display_hash(hashTable): 
	
	for i in range(len(hashTable)): 
		print(i, end = " ") 
		
		for j in hashTable[i]: 
			print("-->", end = " ") 
			print(j, end = " ") 
			
		print() 

# Creating Hashtable as 
# a nested list. 
HashTable = [[] for _ in range(40)] 

# Hashing Function to return 
# key for every value. 
def Hashing(keyvalue): 
	return keyvalue % 40 


# Insert Function to add 
# values to the hash table 
def insert(Hashtable, keyvalue, value): 
	
	hash_key = Hashing(keyvalue) 
	Hashtable[hash_key].append(value) 

# Driver Code 
insert(HashTable, 39, 'red') 
insert(HashTable, 15, 'blue') 
insert(HashTable, 39, 'Mathura') 
insert(HashTable, 9, 'Delhi') 
insert(HashTable, 25, 'Punjab') 
insert(HashTable, 25, 'Noida')

display_hash (HashTable)




