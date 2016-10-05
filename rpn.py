#!/usr/bin/env python3

def calculate(string):
	stack = list()
	for token in myarg.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		else if token == '-':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 - arg2
			stack.append(result)
		else if token == '*':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 * arg2
			stack.append(result)
		else if token == '/':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 / arg2
			stack.append(result)
		else
			stack.append(int(token))
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)

if __name__ == '__main__': # Note that's "underscore underscore n a m e ..."
	main()
