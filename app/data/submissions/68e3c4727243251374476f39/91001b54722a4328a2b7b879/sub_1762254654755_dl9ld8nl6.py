import ast
nums_str = input()
nums = ast.literal_eval(nums_str)
squared = [num ** 2 for num in nums]
print('[' + ','.join(str(x) for x in squared) + ']')
