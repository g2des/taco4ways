

class Cell:

    def __init__(self, value):
        self.value = value
        self.next = None
    

class SinglyLinkedList:

    def __init__(self):
        self.top = Cell(-1)
    
    def add_at_beginning(self, value:int):
        cell = Cell(value)
        cell.next = self.top.next
        self.top.next = cell

    def add_at_end(self, value: int):
        cell = Cell(value)
        ptr = self.top
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = cell
    
    def find_cell_before(self,target: int):
        ptr = self.top
        while ptr.next != None:
            if ptr.next.value == target:
                return ptr
            ptr = ptr.next
        return None
    
    def delete_cell(self, target:int):
        before_target = self.find_cell_before(target)
        if before_target != None:
            cell = before_target.next
            before_target.next = before_target.next.next
            del cell
    
    
    def print_list(self):
        start = self.top
        output_string = ""
        while(start.next != None):
            output_string+= f"{start.next.value} -> "
            start = start.next
        print(output_string)
    
def main():
    list = SinglyLinkedList()
    list.add_at_beginning(2)
    list.add_at_beginning(1)
    list.add_at_end(3)
    list.add_at_end(4)
    list.print_list()
    print(list.find_cell_before(1).value)
    print(list.find_cell_before(5))
    list.delete_cell(2)
    list.print_list()
    

if __name__ == '__main__':
    main()