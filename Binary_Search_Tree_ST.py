class BST:
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__(self, key, value, n):
            self.key = key
            self.val = value
            self.left = None
            self.right = None
            self.n = n

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x == None:
            return 0
        else:
            return x.n

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        if x == None:
            return None
        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x == None:
            return BST.Node(key, val, 1)
        if key < x.key:
            x.left = self._put (x.left, key, val)
        elif key > x.key:
            x.right = self._put (x.right, key, val)
        else:
            x.val = val
        x.n = self._size(x.left) + self._size(x.right) + 1
        return x

    def min(self):
        x = self._min(self.root)
        return x.key

    def _min(self, x):
        if x.left == None:
            return x
        return self._min(x.left)

    def max(self):
        x = self._max(self.root)
        return x.key

    def _max(self, x):
        if x.right == None:
            return x
        return self._max(x.right)


    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, x):
        if x == None:
            return 0
        if key < x.key:
            return self._rank(key, x.left)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(key, x.right)
        else:
            return self._size(x.left)

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, x):
        if x.left == None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.n = 1 + self._size(x.left) + self._size(x.right)
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x == None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        if key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right == None:
                return x.left

            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left

        x.n = self._size(x.left) + self._size(x.right) + 1
        return x

    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self, root):
        if root == None or root.n == 1:
            return True
        
        if root.left :
            isLeftBST = root.left.key < root.key and self._isBST(root.left)
        else:
            isLeftBST = True
        
        if root.right :
            isRightBST = root.right.key > root.key and self._isBST(root.right)
        else:
            isRightBST = True,

        return isLeftBST and isRightBST

    def successor(self, key):
    
        x = self.root
        while x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

      
        if x.right != None:
            return self._min(x.right).key
       
        else:
            succ = None
            y = self.root
            while y != None:
                if x.key < y.key:
                    succ = y
                    y = y.left
                elif x.key > y.key:
                    y = y.right
                    succ = y.right
                else:
                    break
        
        if succ:
            return succ.key
        else:
            return None

def main():

    class Node2:
        def __init__(self, key, value, n):
            self.key = key
            self.val = value
            self.left = None
            self.right = None
            self.n = n

    symbolTable = BST()
    symbolTable.put('X', 7)
    symbolTable.put('B', 8)
    symbolTable.put('A', 9)
    symbolTable.put('P', 10)
    symbolTable.put('L', 11)
    symbolTable.put('S', 0)
    symbolTable.put('E', 1)
    symbolTable.put('A', 2)
    symbolTable.put('R', 3)
    symbolTable.put('E', 6)
    symbolTable.put('E', 12)
    symbolTable.put('C', 4)
    symbolTable.put('H', 5)

    print (symbolTable.successor('P'))
    exit(0)
    print ("Size: ", symbolTable.size())
    root = symbolTable.root
    traverse (root)
    print()

    print ("isBST: ", symbolTable.isBST())

    n1 = Node2(10, "A", 4)
    n2 = Node2(8, "B", 1)
    n3 = Node2(20, "C", 2)
    n4 = Node2(21, "D", 1)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = None
    n2.right = None
    n3.left = None
    n3.right = n4
    n4.left = None
    n4.right = None


    print ("isBST: ", symbolTable._isBST(root))


def traverse(root): 
    print (root.key, " ", root.val)
    if root.left != None:
        traverse(root.left)
    if root.right != None:
        traverse(root.right)

if __name__ == '__main__':
    main()
