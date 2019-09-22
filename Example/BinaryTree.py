#coding=utf-8
'''包括二叉树的建立等操作以及前序，中序，后序，深度优先，广度优先遍历'''

class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class Binary_Tree(object):

    #   创建二叉树
    def create(self,List):
        root = Node(List[0])
        lens = len(List)
        if lens >= 2:
            root.left = self.create(List[1])
        if lens >= 3:
            root.right = self.create(List[2])
        return root

    #   二叉树的查找
    def find(self,root,data):
        if root == None:
            print('The Tree is empty!')
            return False
        if root.value == data:
            print(str(data) + ' is in the tree !')
            return True
        elif root.left:
            return self.find(root.left,data)
        elif root.right:
            return self.find(root.right,data)

    #   先序遍历,中左右
    def preOder(self,root):
        if root == None:
            return
        print(root.value,end=' ')
        self.preOder(root.left)
        self.preOder(root.right)

    #   中序遍历，左中右
    def inOder(self,root):
        if root == None:
            return
        self.inOder(root.left)
        print(root.value,end=' ')
        self.inOder(root.right)

    #   后序遍历，左右中
    def bacOrder(self,root):
        if root == None:
            return
        self.bacOrder(root.left)
        self.bacOrder(root.right)
        print(root.value,end=' ')

    #   广度优先遍历
    def BFS(self,root):
        if root == None:
            return
        #   使用队列保存节点
        queue = [root]
        while queue:
            #   每次取出队首的节点，并打印该节点的值，若其左子树右子树存在，则将存在的子节点加入队尾
            thisNode = queue.pop(0)
            print(thisNode.value,end=' ')
            if thisNode.left:
                queue.append(thisNode.left)
            if thisNode.right:
                queue.append(thisNode.right)

    #   深度优先遍历
    def DFS(self,root):
        if root == None:
            return
        #   使用栈保存节点
        stack = [root]
        while stack:
            #   每次弹出栈顶节点，打印该节点的值，若其左子树右子树存在，则将存在的子节点入栈
            thisNode = stack.pop()
            print(thisNode.value,end=' ')
            if thisNode.right:
                stack.append(thisNode.right)
            if thisNode.left:
                stack.append(thisNode.left)

    #   获取节点的最大深度
    def height(self,root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1

    #   判断是否为平衡二叉树
    def is_balanced(self,root):
        #   如果树为空，肯定是平衡二叉树
        if root == None:
            return True
        #   满足平衡二叉树的条件：左右子树都是平衡二叉树且左右子树深度相差不大于1
        return self.is_balanced(root.left) and self.is_balanced(root.right) and abs(self.height(root.left)-self.height(root.right))<=1

if __name__ == '__main__':
    '''
                    1
                  /   \
                 2     3
                / \   / \
               4  5   6  7
              / \
             8   9
    '''
    List1 = [1, [2, [4, [8], [9]], [5]], [3, [6], [7]]]
    tree = Binary_Tree()
    root = tree.create(List1)
    tree.find(root,1)
    print('PreOrder: ')
    tree.preOder(root)
    print('\nInOrder: ')
    tree.inOder(root)
    print('\nBacOrder: ')
    tree.bacOrder(root)
    print('\nBFS: ')
    tree.BFS(root)
    print('\nDFS: ')
    tree.DFS(root)
    print('\nIs balanced: '+str(tree.is_balanced(root)))
