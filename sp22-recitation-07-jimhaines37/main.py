import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):

    p = queue.PriorityQueue()

    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        
        l = p.get() 
        r = p.get()

        z = TreeNode(l, r, ((l.data[0] + r.data[0]), " "))

        p.put(z)         
        
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}): 

    if node.left == None and node.right == None:
        code[node.data[1]] = prefix 

    if node.left != None:
        get_code(node.left, prefix + "0", code)

    if node.right != None:
        get_code(node.right, prefix + "1", code)

    return code 
    

# given an alphabet and frequencies, compute the cost of a fixed length encoding, each character has same coding length instead of variable lengths
def fixed_length_cost(f):
    
    numBits = math.ceil(math.log2(len(f)))
    total = 0
    
    for i in f.keys():
        total += f[i]  
    return total*numBits



# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):

    overall = 0

    for i in f.keys():
        overall += len(C[i]) * f[i]

    return overall


f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))