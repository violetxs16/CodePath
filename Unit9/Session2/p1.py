from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
def is_balanced(display):
	#base case: We have a null root
    if not display:
        return True
    if not display.left and not display.right: #both subtrees are null
        return True
    #check case where 
    height_left = helper(display.left)
    height_right = helper(display.right)
    diff = height_left - height_right
    if diff == 1 or diff == 0 or diff == -1:
        return True
    return False
def helper(root):
    if not root:
        return 0
    #we need to take max height of left or right subtree
    return 1 + max(helper(root.right), helper(root.left))
#umpire
#understanding: we are given the root node and we want to see if the tree is balanced
#match: binary trree problem
#plan: use recursion to get height. root, 1 + left == 1 + right

"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁


# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)


          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  