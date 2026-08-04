def isBalanced(exp):

    stack = []

    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for i in exp:

        if i in "({[":
            stack.append(i)

        elif i in ")}]":

            if not stack:
                return False

            if stack.pop() != pairs[i]:
                return False

    return len(stack) == 0


expression = input("Enter Expression: ")

if isBalanced(expression):
    print("Balanced")
else:
    print("Not Balanced")