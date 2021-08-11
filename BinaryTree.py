#二叉树类
class BinaryTree(object):
    # 初始化，传入根节点的值
    def __init__(self, root_value):
        self.root = root_value
        self.leftchild = None
        self.rightchild = None
    # 插入左子树
    def insert_left(self, left_value):
        if self.leftchild == None :
            self.leftchild = BinaryTree(left_value)
        else:
            left_subtree = BinaryTree(left_value)
            left_subtree.leftchild = self.leftchild
            self.leftchild = left_subtree
    # 插入右子树
    def insert_right(self, right_value):
        if self.rightchild == None :
            self.rightchild = BinaryTree(right_value)
        else:
            right_subtree = BinaryTree(right_value)
            right_subtree.rightchild = self.rightchild
            self.rightchild = right_subtree
    # 设置根节点的值
    def set_root(self, root_value):
        self.root = root_value
    # 获取根节点的值
    def get_root(self):
        return self.root
    # 获取左子树
    def get_leftchild(self):
        return self.leftchild
    # 获取右子树
    def get_rightchile(self):
        return self.rightchild


# 前序遍历二叉树
def pre_traversal(tree):
    if tree != None:
        print(tree.root)
        pre_traversal(tree.leftchild)
        pre_traversal(tree.rightchild)


# 中序遍历二叉树
def in_traversal(tree):
    if tree != None:
        in_traversal(tree.leftchild)
        print(tree.root)
        in_traversal(tree.rightchild)


# 后序遍历二叉树
def post_traversal(tree):
    if tree != None:
        post_traversal(tree.leftchild)
        post_traversal(tree.rightchild)
        print(tree.root)