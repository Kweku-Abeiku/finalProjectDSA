import random
import time

import matplotlib.pyplot as plt

#class to build hashtable.
class HashTable:
    def __init__(self):
        self.MAX = 509
        self.arr = [[] for _ in range(self.MAX)]
        self.tree_arr = [None] * 509
    #method to generate index
    def get_hash(self, key):
        hash = key
        return hash % self.MAX

    # method to insert into hashtable with simple chaining collision resolution
    def insertChaining(self, key, val):
        h = self.get_hash(key)
        if not (self.arr[h] == "[]"):
            self.arr[h].append(val)
        else:
            self.arr[h] = val
    #method to insert into hashtable with tree collision resolution
    def insertTree(self, key, val):
        h = self.get_hash(key)
        # print(self.tree_arr[h])
        if (self.tree_arr[h] == None):
            self.tree_arr[h] = Tree()
            self.tree_arr[h].insertT(val)
        else:
            self.tree_arr[h].insertT(val)

    # print out hashtable with simple linked list
    def display_hash(self):
        size = self.MAX
        for i in range(size):
            print("[", i, "]", end=" ")
            print(self.arr[i])
    #print out hashtable with binary search tree
    def display_hash_Tree(self):
        size = self.MAX
        for i in range(size):
            print("[", i, "]", end=" ")
            if self.tree_arr[i] != None:
                print("[ ", end="")
                self.tree_arr[i].inorder()
            else:
                print("[]")

#class of the Node of binary search tree
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    #this method is used to travese throught the tree to print values in the tree
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value), end=" ")
            if self.rightChild:
                self.rightChild.inorder()

#class to build binary search tree
class Tree:
    def __init__(self):
        self.root = None

    def insertT(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
            print(']\n', end="")



table1 = HashTable()
table2 = HashTable()
tree_y1, tree_y2, tree_y3, tree_y4, tree_y5, tree_y6, tree_y7, tree_y8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
chain_y1, chain_y2, chain_y3, chain_y4, chain_y5, chain_y6, chain_y7, chain_y8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
# hash with chain
print("Hash with chain time in miliseconds")
count = 0
sum_time = 0
for current in range(8192):
    count = count + 1
    start_time = time.time()
    r = int(random.uniform(16385, 65335))
    midSqSeed = r
    midSqSeed = midSqSeed * midSqSeed
    midSqSeed = midSqSeed / 100
    midSquare = int(midSqSeed % 10000)
    # print("")
    # print(r*r)
    # print(midSquare)
    table2.insertChaining(midSquare, r)

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_milliSeconds = elapsed_time * 1000
    sum_time = sum_time + elapsed_time_milliSeconds

    if (current == 1023):
        chain_y1 = round(sum_time / count, 6)
        print(chain_y1)
        sum_time = 0
    if (current == 2047):
        chain_y2 = round(sum_time / count, 6)
        print(chain_y2)
        sum_time = 0
    if (current == 3071):
        chain_y3 = round(sum_time / count, 6)
        print(chain_y3)
        sum_time = 0
    if (current == 4095):
        chain_y4 = round(sum_time / count, 6)
        print(chain_y4)
        sum_time = 0
    if (current == 5119):
        chain_y5 = round(sum_time / count, 6)
        print(chain_y5)
        sum_time = 0
    if (current == 6143):
        chain_y6 = round(sum_time / count, 6)
        print(chain_y6)
        sum_time = 0
    if (current == 7167):
        chain_y7 = round(sum_time / count, 6)
        print(chain_y7)
        sum_time = 0
    if (current == 8191):
        chain_y8 = round(sum_time / count, 6)
        print(chain_y8)
        sum_time = 0

#table2.display_hash()


print("\n")
print(
    "**************************************************************************************************************************************")
print("\n")
#hash with tree
print("Hash with Binary Tree time in miliseconds")
count = 0
sum_time = 0
for current in range(8192):
    count = count + 1
    start_time = time.time()
    r = int(random.uniform(16385, 65335))
    midSqSeed = r
    midSqSeed = midSqSeed * midSqSeed
    midSqSeed = midSqSeed / 100
    midSquare = int(midSqSeed % 10000)
    # print("")
    # print(r*r)
    # print(midSquare)
    table1.insertTree(midSquare, r)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_milliSeconds = elapsed_time * 1000
    sum_time = sum_time + elapsed_time_milliSeconds

    if (current == 1023):
        tree_y1 = round(sum_time / count, 6)
        print(tree_y1)
        sum_time = 0
    if (current == 2047):
        tree_y2 = round(sum_time / count, 6)
        print(tree_y2)
        sum_time = 0
    if (current == 3071):
        tree_y3 = round(sum_time / count, 6)
        print(tree_y3)
        sum_time = 0
    if (current == 4095):
        tree_y4 = round(sum_time / count, 6)
        print(tree_y4)
        sum_time = 0
    if (current == 5119):
        tree_y5 = round(sum_time / count, 6)
        print(tree_y5)
        sum_time = 0
    if (current == 6143):
        tree_y6 = round(sum_time / count, 6)
        print(tree_y6)
        sum_time = 0
    if (current == 7167):
        tree_y7 = round(sum_time / count, 6)
        print(tree_y7)
        sum_time = 0
    if (current == 8191):
        tree_y8 = round(sum_time / count, 6)
        print(tree_y8)
        sum_time = 0

#table1.display_hash_Tree()
# plotting the average times
x = ["1024", "2048", "3072", "4096", "5120", "6144", "7168", "8192"]
chain = [chain_y1, chain_y2, chain_y3, chain_y4, chain_y5, chain_y6, chain_y7, chain_y8]
#print(chain)
tree = [tree_y1, tree_y2, tree_y3, tree_y4, tree_y5, tree_y6, tree_y7, tree_y8]
#print(tree)
plt.plot(x, tree)
plt.plot(x, chain)
plt.xlabel("Intervals")
plt.title("Runtime Comparison in seconds")
plt.show()
