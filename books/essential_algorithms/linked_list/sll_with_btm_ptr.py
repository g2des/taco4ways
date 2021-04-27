

class Cell:

    def __init__(self, value):
        self.value = value
        self.next = None
    

class SinglyLinkedList:

    def __init__(self):
        self.top = Cell("Top")
        self.bottom = self.top
    
    def add_at_beginning(self, value:int):
        cell = Cell(value)
        cell.next = self.top.next
        self.top.next = cell
        if cell.next == None:
            self.bottom = cell
        
    def add_at_end(self, value: int):
        cell = Cell(value)
        self.bottom.next = cell
        self.bottom = cell
        # ptr = self.top
        # while ptr.next != None:
        #     ptr = ptr.next
        # ptr.next = cell
    
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
            if before_target.next == None:
                self.bottom = before_target
            del cell
    
    def get_max(self):
        ptr = self.top
        max_val = None
        while ptr.next != None:
            if max_val == None:
                max_val = ptr.next.value
            elif max_val < ptr.next.value:
                max_val = ptr.next.value
            ptr = ptr.next
            # max_val = ptr.next.value if max_val != None or max_val < ptr.next.value else max_val
        return max_val
            

    def print_list(self):
        start = self.top
        output_string = ""
        while(start.next != None):
            output_string+= f"{start.next.value} -> "
            start = start.next
        print(f"Top : {self.top.next.value} Bottom: {self.bottom.value}\n"+output_string)



def main():
    list = SinglyLinkedList()
    list.add_at_beginning(2)
    list.print_list()
    list.add_at_beginning(1)
    list.print_list()
    list.add_at_end(3)
    list.print_list()
    list.add_at_end(4)
    list.print_list()
    print(list.find_cell_before(1).value)
    print(list.find_cell_before(5))
    list.delete_cell(2)
    list.print_list()
    list.delete_cell(4)
    list.print_list()
    list.delete_cell(3)
    list.print_list()
    from random import randint
    for _ in range(10):
        list.add_at_beginning(randint(0,100))
    list.print_list()
    print(list.get_max())

if __name__ == '__main__':
    main()