def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 20, 'Ally')
insert(HashTable, 2, 'Katana')
insert(HashTable, 20, 'Snowball')
insert(HashTable, 9, 'Krypton')
insert(HashTable, 18, 'Febe')
insert(HashTable, 16, 'Sq')
display_hash(HashTable)
