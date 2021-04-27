
class Cell:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.top = Cell("top")
        self.bottom = Cell("bottom")
        self.top.next, self.bottom.prev = self.bottom, self.top
        self.top.prev, self.bottom.next = None, None
    
    def add_at_start(self, value):
        self.insert(self.top, Cell(value))
    
    def add_at_end(self, value):
        self.insert(self.bottom.prev, Cell(value))

    def insert(self, afterme:Cell, cell:Cell):
        # cell = Cell(value)
        cell.next = afterme.next
        afterme.next = cell

        cell.prev = afterme
        cell.next.prev = cell
    
    def find_cell_before(self, value):
        ptr = self.top
        while ptr.next != None:
            if ptr.next.value == value:
                return ptr
            ptr = ptr.next
        return None

    def delete_cell(self, value):
        find_before = self.find_cell_before(value)
        if find_before != None:
            cell = find_before.next
            cell.prev.next = cell.next
            cell.next.prev = cell.prev
            del cell


    def to_string(self, reverse=False):
        output = ""
        if reverse:
            ptr = self.bottom
            while ptr.prev != None:
                output += f"{ptr.prev.value}-> "
                ptr = ptr.prev
        else:
            ptr = self.top
            while ptr.next !=None:
                output+= f"{ptr.next.value}-> "
                ptr = ptr.next
        return output

def main():
    list = DoublyLinkedList()
    from random import randint
    nums = [randint(0,100) for _ in range(10)]
    ordered = []
    method = []
    for num in nums:
        index = randint(0,1)
        if index == 0:
            list.add_at_start(num)
            ordered.insert(0, num)
            method.append((num, 'start'))
        else:
            list.add_at_end(num)
            ordered.append(num)
            method.append((num,'end'))
    print(method)
    print(list.to_string())
    print(ordered)
    print(list.to_string(reverse=True))
    print([*reversed(ordered)])
    delete_index = [0,-1]+ [randint(1,6)]
    for num in delete_index:
        print(f"Deleting {ordered[num]}")
        list.delete_cell(ordered[num])
        print(list.to_string())


if __name__ == "__main__":
    main()