from math import inf
class Cell:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Sorted_Doubly_LinkedList:

    def __init__(self):
        self.top = Cell(-inf)
        self.bottom = Cell(inf)

        self.top.next = self.bottom
        self.bottom.prev = self.top
    
    def sorted_add(self, value):
        cell = Cell(value)
        ptr = self.top
        while ptr.next.value < value:
            ptr = ptr.next
        self.insert(ptr, cell)
    
    def insert(self, after_me:Cell, target:Cell):
        target.prev = after_me
        after_me.next.prev = target

        target.next = after_me.next
        after_me.next = target
    
    def is_sorted(self):
        ptr = self.top
        while ptr.next!=None:
            if ptr.next.value >= ptr.value:
                ptr = ptr.next
            else:
                return False
        return True
    
    def __str__(self):
        output = ""
        ptr = self.top
        while ptr != None:
            output += f"{ptr.value} ->"
            ptr = ptr.next
        return output

def main():
    from random import randint
    list = Sorted_Doubly_LinkedList()
    for _ in range(10):
        list.sorted_add(randint(-100,100))
    print(list, f"\nSorted : {list.is_sorted()}")

if __name__ == "__main__":
    main()