"""
Custom implementation of stack
"""


class Stack:

    def __init__(self, elements=[]):
        
        if type(elements) == list:
            self.elements = elements
        else:
            raise TypeError("A list with values must be provided as the argument instead")
    

    def pop(self):
        try:
            value = self.elements[-1]
            self.elements = self.elements[:-1]
            return value
        except:
            raise RuntimeError


    def push(self, value):
        self.elements.append(value)

    
    def is_empty(self):
        return self.elements != []


    def peek(self):
        try:
            return self.elements[-1]
        except:
            raise RuntimeError

    def __repr__(self):
        return '\n'.join(map(str, self.elements[::-1]))


if __name__ == "__main__":
    lst = list(range(10))
    stack = Stack(lst)
    print("New Stack")
    print(stack)
    print("Popped")
    print(stack.pop)
    print("Pushed 11")
    print(stack.push(11))
    print("Popped")
    print(stack.pop())
    for _ in range(5):
        print("Popped")
        print(stack.pop())
    print("Stack")
    print(stack)

            
