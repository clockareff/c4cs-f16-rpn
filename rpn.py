#!/usr/bin/env python3

#python3 does not work on CAEN so I couldnt test the code
#I tried python2 but it was throwing errors every time I used if else

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
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
