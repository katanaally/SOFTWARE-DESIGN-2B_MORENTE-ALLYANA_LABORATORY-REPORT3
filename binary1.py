class Node:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None

def PostPreInOrderInOneFlowRecursive(root, pre, post, In):

	if (root == None):
		return

	pre.append(root.data)

	PostPreInOrderInOneFlowRecursive(root.left, pre, post, In)

	In.append(root.data)

	PostPreInOrderInOneFlowRecursive(root.right, pre, post, In)

	post.append(root.data)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.left.right= Node(99)
root.left.right.left = Node(85)
root.right.right.left = Node(90)
root.right.right.right = Node(95)
pre,post,In = [],[],[]
PostPreInOrderInOneFlowRecursive(root, pre, post, In)
print("Pre Order : ",end = "")
for i in pre:
	print(i,end = " ")

print()
print("Post Order : ",end = "")
for i in post:
	print(i,end = " ")
print()
print("In Order : ",end = "")
for i in In:
	print(i,end = " ")


