import csv

def autoquestion(worst, datastructure, action, space=False):
    return "What is the {} time complexity of {} {}?".format("worst" if worst else "average", datastructure, action) if not space else "What is the worst space complexity of {}?".format(datastructure)

def autowrite(w, ID, question, answer):
    w.writerow([ID, question, answer, "0", "0", "1"])

with open("questions.csv", "w+") as csvfile:
    w = csv.writer(csvfile, delimiter = "~", quotechar= '"')
    w.writerow(["ID", "Question", "Answer", "Correct #", "Asked #", "Average Correctness"])
    # Array questions
    autowrite(w, "1", """What are the stats of an array?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(1)
Search : O(n)
Insertion : O(n)
Deletion : O(n)
Space : O(n)""")
    autowrite(w, "2", autoquestion(False, "array", "access") , "O(1)")
    autowrite(w, "3", "What is the worst time complexity of array access?", "O(1)")
    autowrite(w, "4", "What is the average time complexity of array search?", "O(n)")
    autowrite(w, "5", "What is the worst time complexity of array access?", "O(n)")
    autowrite(w, "6", "What is the average time complexity of array insertion?", "O(n)")
    autowrite(w, "7", "What is the worst time complexity of array insertion?", "O(n)")
    autowrite(w, "8", "What is the average time complexity of array deletion?", "O(n)")
    autowrite(w, "9", "What is the worst time complexity of array deletion?", "O(n)")
    autowrite(w, "10", "What is the worst space complexity of an array?", "O(n)")
    autowrite(w, "11", "Are an array's average and worst time complexity stats different or same?", "Same")
   # Stack questions
    autowrite(w, "12", """What are the stats of a stack?
That is, what is its average and worst time complexities in
    access,
    search,
    deletion,
and its worst space complexity?""", """Access : O(n)
Search : O(n)
Insertion : O(1)
Deletion : O(1)
Space : O(n)""")
    autowrite(w, "13", "What is the average time complexity of stack access?", "O(n)")
    autowrite(w, "14", autoquestion(True, "stack", "access"), "O(n)")
    autowrite(w, "15", autoquestion(False, "stack", "search"), "O(n)")
    autowrite(w, "16", autoquestion(True, "stack", "search"), "O(n)")
    autowrite(w, "17", autoquestion(False, "stack", "insertion"), "O(1)")
    autowrite(w, "18", autoquestion(True, "stack", "insertion"), "O(1)")
    autowrite(w, "19", autoquestion(False, "stack", "deletion"), "O(1)")
    autowrite(w, "20", autoquestion(True, "stack", "deletion"), "O(1)")
    autowrite(w, "21", autoquestion(True, "stack", None, True), "O(n)")
    autowrite(w, "22", "Are a stack's average and worst time complexity stats different or same?", "Same")
    # Singly-linked list
    autowrite(w, "23", """What are the stats of a singly-linked list?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(n),
Search : O(n),
Insertion : O(1),
Deletion : O(1),
Space : O(n)""")
    autowrite(w, "24", autoquestion(False, "singly-linked list", "access"), "O(n)")
    autowrite(w, "26", autoquestion(True, "singly-linked list", "access"), "O(n)")
    autowrite(w, "27", autoquestion(False, "singly-linked list", "search"), "O(n)")
    autowrite(w, "28", autoquestion(True, "singly-linked list", "search"), "O(n)")
    autowrite(w, "29", autoquestion(False, "singly-linked list", "insertion"), "O(1)")
    autowrite(w, "30", autoquestion(True, "singly-linked list", "insertion"), "O(1)")
    autowrite(w, "31", autoquestion(False, "singly-linked list", "deletion"), "O(1)")
    autowrite(w, "32", autoquestion(True, "singly-linked list", "deletion"), "O(1)")
    autowrite(w, "33", autoquestion(True, "singly-linked list", None, True), "O(n)")
    autowrite(w, "34", "Are a singly-linked list's average and worst time complexity stats different or same?", "Same")
    # Doubly-linked list
    autowrite(w, "35", """What are the stats of a doubly-linked list?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(n),
Search : O(n),
Insertion : O(1),
Deletion : O(1),
Space : O(n)""")
    autowrite(w, "36", autoquestion(False, "doubly-linked list", "access"), "O(n)")
    autowrite(w, "37", autoquestion(True, "doubly-linked list", "access"), "O(n)")
    autowrite(w, "38", autoquestion(False, "doubly-linked list", "search"), "O(n)")
    autowrite(w, "39", autoquestion(True, "doubly-linked list", "search"), "O(n)")
    autowrite(w, "40", autoquestion(False, "doubly-linked list", "insertion"), "O(1)")
    autowrite(w, "41", autoquestion(True, "doubly-linked list", "insertion"), "O(1)")
    autowrite(w, "42", autoquestion(False, "doubly-linked list", "deletion"), "O(1)")
    autowrite(w, "43", autoquestion(True, "doubly-linked list", "deletion"), "O(1)")
    autowrite(w, "44", autoquestion(True, "doubly-linked list", None, True), "O(n)")
    autowrite(w, "45", "Are a doubly-linked list's average and worst time complexity stats different or same?", "Same")
# Skip List
    autowrite(w, "46", """What are the stats of a skip list?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : Average O(log n), Worst O(n)
Search : Average O(log n), Worst O(n)
Insertion : Average O(log n), Worst O(n)
Deletion : Average O(log n), Worst O(n)
Space: O(n log n)""")
    autowrite(w, "47", autoquestion(False, "skip list", "access"), "O(log n)")
    autowrite(w, "48", autoquestion(False, "skip list", "search"), "O(log n)")
    autowrite(w, "49", autoquestion(False, "skip list", "insertion"), "O(log n)")
    autowrite(w, "50", autoquestion(False, "skip list", "deletion"), "O(log n)")
    autowrite(w, "51", autoquestion(True, "skip list", "access"), "O(log n)")
    autowrite(w, "52", autoquestion(True, "skip list", "search"), "O(log n)")
    autowrite(w, "52", autoquestion(True, "skip list", "insertion"), "O(log n)")
    autowrite(w, "53", autoquestion(True, "skip list", "deletion"), "O(log n)")
    autowrite(w, "54", "Are a skip list's average and worst time complexity stats different or same?", "Different")
    autowrite(w, "55", autoquestion(True, "skip list", None, True), "O(n log n)")
# Binary Search Tree
    autowrite(w, "46", """What are the stats of a binary search tree?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : Average O(log n), Worst O(n)
Search : Average O(log n), Worst O(n)
Insertion : Average O(log n), Worst O(n)
Deletion : Average O(log n), Worst O(n)
Space: O(n)""")
    autowrite(w, "47", autoquestion(False, "binary search tree", "access"), "O(log n)")
    autowrite(w, "48", autoquestion(False, "binary search tree", "search"), "O(log n)")
    autowrite(w, "49", autoquestion(False, "binary search tree", "insertion"), "O(log n)")
    autowrite(w, "50", autoquestion(False, "binary search tree", "deletion"), "O(log n)")
    autowrite(w, "51", autoquestion(True, "binary search tree", "access"), "O(n)")
    autowrite(w, "52", autoquestion(True, "binary search tree", "search"), "O(n)")
    autowrite(w, "52", autoquestion(True, "binary search tree", "insertion"), "O(n)")
    autowrite(w, "53", autoquestion(True, "binary search tree", "deletion"), "O(n)")
    autowrite(w, "54", "Are a binary search tree's average and worst time complexity stats different or same?", "Different")
    autowrite(w, "55", autoquestion(True, "binary search tree", None, True), "O(n)")
# Cartesian Tree
    autowrite(w, "56", """What are the stats of a cartesian tree?
That is, what is its average and worst time complexities in
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Search : Average O(log n), Worst O(n)
Insertion : Average O(log n), Worst O(n)
Deletion : Average O(log n), Worst O(n)
Space: O(n)""")
    autowrite(w, "57", autoquestion(False, "cartesian tree", "search"), "O(log n)")
    autowrite(w, "58", autoquestion(False, "cartesian tree", "insertion"), "O(log n)")
    autowrite(w, "59", autoquestion(False, "cartesian tree", "deletion"), "O(log n)")
    autowrite(w, "61", autoquestion(True, "cartesian tree", "search"), "O(n)")
    autowrite(w, "62", autoquestion(True, "cartesian tree", "insertion"), "O(n)")
    autowrite(w, "63", autoquestion(True, "cartesian tree", "deletion"), "O(n)")
    autowrite(w, "64", "Are a cartesian tree's average and worst time complexity stats different or same?", "Different")
    autowrite(w, "65", autoquestion(True, "cartesian tree", None, True), "O(n)")
# Splay Tree
    autowrite(w, "66", """What are the stats of a splay tree?
That is, what is its average and worst time complexities in
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Search : Average O(log n), Worst O(log n)
Insertion : Average O(log n), Worst O(log n)
Deletion : Average O(log n), Worst O(log n)
Space: O(n)""")
    autowrite(w, "67", autoquestion(False, "splay tree", "search"), "O(log n)")
    autowrite(w, "68", autoquestion(False, "splay tree", "insertion"), "O(log n)")
    autowrite(w, "69", autoquestion(False, "splay tree", "deletion"), "O(log n)")
    autowrite(w, "70", autoquestion(True, "splay tree", "search"), "O(log n)")
    autowrite(w, "71", autoquestion(True, "splay tree", "insertion"), "O(log n)")
    autowrite(w, "72", autoquestion(True, "splay tree", "deletion"), "O(log n)")
    autowrite(w, "73", "Are a splay tree's average and worst time complexity stats different or same?", "Same")
    autowrite(w, "74", autoquestion(True, "splay tree", None, True), "O(n)")
# B Tree
    autowrite(w, "75", """What are the stats of a b-tree?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(log n)
Search : O(log n)
Insertion : O(log n)
Deletion : O(log n)
Space : O(n)""")
    autowrite(w, "76", autoquestion(False, "b-tree", "access"), "O(log n)")
    autowrite(w, "77", autoquestion(False, "b-tree", "search"), "O(log n)")
    autowrite(w, "78", autoquestion(False, "b-tree", "insertion"), "O(log n)")
    autowrite(w, "79", autoquestion(False, "b-tree", "deletion"), "O(log n)")
    autowrite(w, "80", autoquestion(True, "b-tree", "access"), "O(log n)")
    autowrite(w, "81", autoquestion(True, "b-tree", "search"), "O(log n)")
    autowrite(w, "82", autoquestion(True, "b-tree", "insertion"), "O(log n)")
    autowrite(w, "83", autoquestion(True, "b-tree", "deletion"), "O(log n)")
    autowrite(w, "84", autoquestion(True, "b-tree", None, True), "O(n)")
    autowrite(w, "85", "Are a b-tree's average and worst time complexity stats different or same?", "Same")
# Red-Black Tree
    autowrite(w, "86", """What are the stats of a red-black tree?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(log n)
Search : O(log n)
Insertion : O(log n)
Deletion : O(log n)
Space : O(n)""")
    autowrite(w, "87", autoquestion(False, "red-black tree", "access"), "O(log n)")
    autowrite(w, "88", autoquestion(False, "red-black tree", "search"), "O(log n)")
    autowrite(w, "89", autoquestion(False, "red-black tree", "insertion"), "O(log n)")
    autowrite(w, "90", autoquestion(False, "red-black tree", "deletion"), "O(log n)")
    autowrite(w, "91", autoquestion(True, "red-black tree", "access"), "O(log n)")
    autowrite(w, "92", autoquestion(True, "red-black tree", "search"), "O(log n)")
    autowrite(w, "93", autoquestion(True, "red-black tree", "insertion"), "O(log n)")
    autowrite(w, "94", autoquestion(True, "red-black tree", "deletion"), "O(log n)")
    autowrite(w, "95", autoquestion(True, "red-black tree", None, True), "O(n)")
    autowrite(w, "96", "Are a red-black tree's average and worst time complexity stats different or same?", "Same")
# AVL Tree
    autowrite(w, "97", """What are the stats of a avl tree?
That is, what is its average and worst time complexities in
    access,
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Access : O(log n)
Search : O(log n)
Insertion : O(log n)
Deletion : O(log n)
Space : O(n)""")
    autowrite(w, "98", autoquestion(False, "avl tree", "access"), "O(log n)")
    autowrite(w, "99", autoquestion(False, "avl tree", "search"), "O(log n)")
    autowrite(w, "100", autoquestion(False, "avl tree", "insertion"), "O(log n)")
    autowrite(w, "101", autoquestion(False, "avl tree", "deletion"), "O(log n)")
    autowrite(w, "102", autoquestion(True, "avl tree", "access"), "O(log n)")
    autowrite(w, "103", autoquestion(True, "avl tree", "search"), "O(log n)")
    autowrite(w, "104", autoquestion(True, "avl tree", "insertion"), "O(log n)")
    autowrite(w, "105", autoquestion(True, "avl tree", "deletion"), "O(log n)")
    autowrite(w, "106", autoquestion(True, "avl tree", None, True), "O(n)")
    autowrite(w, "107", "Are a avl tree's average and worst time complexity stats different or same?", "Same")
# Hash Table
    autowrite(w, "108", """What are the stats of a hash table?
That is, what is its average and worst time complexities in
    search,
    insertion,
    deletion,
and its worst space complexity?""", """Search : Average O(1), Worst O(n)
Insertion : Average O(1), Worst O(n)
Deletion : Average O(1), Worst O(n)
Space : O(n)""")
    autowrite(w, "109", autoquestion(False, "hash table", "search"), "O(1)")
    autowrite(w, "110", autoquestion(False, "hash table", "insertion"), "O(1)")
    autowrite(w, "111", autoquestion(False, "hash table", "deletion"), "O(1)")
    autowrite(w, "112", autoquestion(True, "hash table", None, True), "O(n)")
    autowrite(w, "113", autoquestion(True, "hash table", "search"), "O(n)")
    autowrite(w, "114", autoquestion(True, "hash table", "insertion"), "O(n)")
    autowrite(w, "115", autoquestion(True, "hash table", "deletion"), "O(n)")
    autowrite(w, "116", "Are a hash table's average and worst time complexity stats different or same?", "different")
