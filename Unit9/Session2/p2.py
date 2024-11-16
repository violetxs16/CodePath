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
def sum_each_days_orders(orders):
    line = deque()
    line.append(orders)
    sum_cookies = []

    while line:
        lvl_sum = 0
        #run for loop to be length of queue
        lvl_len = len(line)
        for i in range(lvl_len):
            element = line.popleft()
            lvl_sum += element.val
            if element.right:
                line.append(element.right)
            if element.left:
                line.append(element.left)

        sum_cookies.append(lvl_sum)
    return sum_cookies


    #append and popleft, queue data structure
#match: breath first search approach? Binary tree
#plan: take root , that first entry to queue, take children
#breath first search approach

#Example Usage:



# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)
print(sum_each_days_orders(orders))