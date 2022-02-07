def reverse_notation(s):
  stack = []
  for i in range(len(s)):
    if not s[i] in ['+', '-', '*', '/']:
      # add operand to stack
      stack.append(s[i])
    else:
      # to execute operation get operands from the stack
      # be careful with operands order during execution
      operand_2 = stack.pop()
      operand_1 = stack.pop()
      print(str(operand_1) + s[i] + str(operand_2),"result:", eval(str(operand_1) + s[i] + str(operand_2)))
      stack.append(eval(str(operand_1) + s[i] + str(operand_2)))
      print("stack:",stack)
  return stack[-1]

if __name__ == "__main__":
  print(reverse_notation([10, 3, "-", 2, "*"]))