
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)



r = Node(50)
r = insert(r, 130)
r = insert(r, 210)
r = insert(r, 410)
r = insert(r, 470)
r = insert(r, 650)
r = insert(r, 890)


inorder(r)
