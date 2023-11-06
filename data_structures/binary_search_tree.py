class LeafNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.left: 'LeafNode' = None
        self.right: 'LeafNode' = None

class PrintBST:
    def height(self, root: LeafNode):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def recursive_append(self, node: LeafNode, cur_height, lo, hi, output):
        if not node:
            return 
        
        mid = (lo + hi) // 2
        output[cur_height][mid] = str(node.val)
        self.recursive_append(node.left, cur_height + 1, lo, mid - 1, output)
        self.recursive_append(node.right, cur_height + 1, mid + 1, hi, output)

    def print_tree(self, root: LeafNode):
        tree_height = self.height(root)
        length = 2 ** tree_height
        output = [[' ' for _ in range(length)] for _ in range(tree_height)]
        self.recursive_append(root, 0, 0, length - 1, output)
        
        str_out = ''
        for row in output:
            for col in row:
                str_out += col
            
            str_out += '\n'

        return str_out

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def __repr__(self) -> str:
        return PrintBST().print_tree(self.root)
    
    def put(self, key, value):
        self.root = self._put(key, value, self.root)

    def _put(self, key, value, node: LeafNode):
        if not node:
            return LeafNode(key, value)
        
        if node.key == key:
            node.val = value
        elif node.key > key:
            node.left = self._put(key, value, node.left)
        else:
            node.right = self._put(key, value, node.right)

        return node
    
    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, node: LeafNode):
        if not node:
            return 
        
        if node.key == key:
            return node.val
        
        if node.key > key:
            return self._get(key, node.left)
        
        return self._get(key, node.right)

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node: LeafNode):
        if not node:
            return 
        if node.key > key:
            node.left = self._delete(key, node.left)
        elif node.key < key:
            node.right = self._delete(key, node.right)
        else:
            if not node.left and not node.right:
                return
            elif node.left and node.right:
                temp = node
                cur = node.right
                while cur.left:
                    cur = cur.left

                self._delete(cur.key, temp.right)
                cur.left = temp.left
                cur.right = temp.right
                return cur
            else:
                if node.right:
                    return node.right
                else:
                    return node.left
                
        return node

def inorder(root: LeafNode) -> list:
    def _inorder(r: LeafNode, arr: list):
        if not r:
            return
        
        inorder(r.left, arr)
        arr.append(r.val)
        inorder(r.right, arr)
        return arr

    node_list = []
    return _inorder(root, node_list)

def reverse_inorder(root: LeafNode) -> list:
    def _inorder(r: LeafNode, arr: list):
        if not r:
            return
        
        inorder(r.right, arr)
        arr.append(r.val)
        inorder(r.left, arr)
        return arr

    node_list = []
    return _inorder(root, node_list)

def preorder(root: LeafNode) -> list:
    def _pre(r: LeafNode, arr: list):
        if not r:
            return
        arr.append(r.val)
        preorder(r.left, arr)
        preorder(r.right, arr)
        return arr
    
    nodes_list = []
    return _pre(root, nodes_list)

def postorder(root: LeafNode) -> list:
    def _post(r: LeafNode, arr: list):
        if not r:
            return
        
        postorder(r.left, arr)
        postorder(r.right, arr)
        arr.append(r.val)
        return arr

    nodes_list = []
    return _post(root, nodes_list)

def levelorder_iterative(root: LeafNode) -> list:
    queue: list[LeafNode] = []
    arr = []
    queue.append(root)
    while queue:
        current = queue.pop(0)
        if current:
            arr.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
    return arr

def height(root: LeafNode) -> int:
    def _height(r: LeafNode):
        if not r:
            return 0
        
        return 1 + max(_height(r.left), _height(r.right))

    return max(_height(root.left), _height(root.right))

def is_symetric(root: LeafNode) -> bool:
    def _symetric(this: LeafNode, other: LeafNode):
        if not this or not other:
            return True
        
        if this.val != other.val:
            return False
        
        return _symetric(this.left, other.right) and _symetric(this.right, other.left)
    
    return _symetric(root.left, root.right)

class Height:
    def __init__(self) -> None:
        self.height = 0

def diameter(root: LeafNode):

    def _diameter(r: LeafNode, h: Height):
        lh = Height()
        rh = Height()

        if not root:
            h.height = 0
            return 0
        
        l_diameter = _diameter(r.left, lh) if r.left else 0
        r_diameter = _diameter(r.right, rh) if r.right else 0

        h.height = max(lh.height, rh.height) + 1
        return max(lh.height + rh.height, max(l_diameter, r_diameter))
    
    height = Height()
    return _diameter(root, height)

def leafs(root: LeafNode):
    def _leafs(r: LeafNode):
        if not r:
            return 0
        
        if not r.left and not r.right:
            return 1

        return _leafs(r.left) + _leafs(r.right)
    
    return _leafs(root)

def top_ordered(root: LeafNode):
    if not root:
        return True
        
    if root.left and root.left.val < root.val or root.right and root.right.val < root.val:
        return False
    
    return top_ordered(root.left) and top_ordered(root.right)
     
def sum_only_child_parents(root: LeafNode):
    def _sum_only_child_parents(r: LeafNode, total = 0):

        if not root: 
            return 0
        
        if bool(root.left) ^ bool(root.right):
            total += root.val

        total += sum_only_child_parents(root.left)
        total += sum_only_child_parents(root.right)
        return total
    
    return _sum_only_child_parents(root)

def sum_only_child(root: LeafNode):
    def _sum_only_child(r: LeafNode, total: int = 0):
        if not r:
            return 0
        
        left = r.left
        right = r.right

        if left and not right:
            total += left.val

        if right and not left:
            total += right.val

        total += _sum_only_child(left)
        total += _sum_only_child(right)
        return total
    
    return root.val + _sum_only_child(root) 

def same(this: LeafNode, other: LeafNode):
    if not this or not other:
        return True

    if this.val != other.val:
        return False
    
    return same(this.left, other.left) and same(this.right, other.right)

def full(root: LeafNode):
    if not root:
        return True
    
    if bool(root.left) != bool(root.right):
        return False
    
    return full(root.left) and full(root.right)

def find_height(root: LeafNode, height: int):
    def _find(r: LeafNode, cur_lvl, desired_lvl):
        if not r:
            return 0
        
        if cur_lvl == desired_lvl:
            return 1
        
        return _find(r.left, cur_lvl + 1, desired_lvl) + _find(r.right, cur_lvl + 1, desired_lvl)
    
    return _find(root, 0, height)

def level_min(root: LeafNode, level: int):
    def _lvl_min(r: LeafNode, des_lvl: int, cur_lvl: int) -> int:
        if not r:
            return float('inf')
        
        if cur_lvl == des_lvl:
            return r.val
        
        return min(_lvl_min(r.left, des_lvl, cur_lvl + 1), _lvl_min(r.right, des_lvl, cur_lvl + 1))
    return _lvl_min(root, level, 0)

def almost_same(this_root: LeafNode, other_root: LeafNode, level: int) -> bool:
    def _almost(this: LeafNode, other: LeafNode, cur_lvl: int, lvl: int) -> bool:
        if not this and not other:
            return True
        
        if this.val != other.val and cur_lvl != lvl:
            return False
        
        return _almost(this.left, other.left, cur_lvl + 1, lvl) and _almost(this.right, other.right, cur_lvl + 1, lvl)
    
    return _almost(this_root, other_root, 0, level)

if __name__ == '__main__':
    bstA = BinarySearchTree()
    bstA.put(8, 8)
    bstA.put(3, 3)
    bstA.put(10, 10)
    bstA.put(1, 1)
    bstA.put(6, 6)
    bstA.put(14, 14)
    bstA.put(4, 4)
    bstA.put(7, 7)
    bstA.put(12, 12)
    print(bstA)

    bstB = BinarySearchTree()
    bstB.put(1, 1)
    bstB.put(2, 2)
    bstB.put(3, 3)
    bstB.put(4, 4)
    bstB.put(5, 5)
    print(bstB)

    rootC = LeafNode(1, 1)
    rootC.left = LeafNode(2, 2)
    rootC.right = LeafNode(3, 3)
    rootC.left.left = LeafNode(4, 4)
    rootC.left.right = LeafNode(5, 5)
    rootC.right.left = LeafNode(6,6)
    rootC.right.right = LeafNode(7,7)
    rootC.left.left.left = LeafNode(8,8)
    rootC.left.left.right = LeafNode(9,9)
    rootC.left.right.left = LeafNode(10,10)
    rootC.left.right.right = LeafNode(11,11)
    print(PrintBST().print_tree(rootC))

    rootD = LeafNode(1, 1)
    rootD.left = LeafNode(2,2)
    rootD.right = LeafNode(2,2)
    rootD.left.left = LeafNode(4,4)
    rootD.left.right = LeafNode(5,5)
    rootD.right.left = LeafNode(5,5)
    rootD.right.right = LeafNode(4,4)
    print(PrintBST().print_tree(rootD))

    rootE = LeafNode(1,1)
    rootE.left = LeafNode(2,2)
    rootE.right = LeafNode(3,3)
    rootE.left.left = LeafNode(4,4)
    rootE.left.right = LeafNode(5,5)
    rootE.left.left.left = LeafNode(10,10)
    rootE.right.right = LeafNode(6,6)
    rootE.right.right.right = LeafNode(8,8)
    rootE.right.right.right.right = LeafNode(9,9)
    print(PrintBST().print_tree(rootE))

    print('Tree A: ', height(bstA.root))
    print('Tree B: ', height(bstB.root))
    print('Tree C: ', height(rootC))
    print('Tree D: ', height(rootD))
    print('Tree E: ', height(rootE))