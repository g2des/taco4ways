
from typing import Tuple


class Heap:
    def __init__(self,num_children = 2):
        self._list = []
        self._num_children = num_children
	
    def push(self, value):
        self._list.append(value)
        self._fixHeapBottomUp()

    def pop(self):
        value = self._list.pop(0)
        self._fixHeapTopDown()
        return value

    def is_empty(self):
        return len(self._list) > 0
    
    def __len__(self):
        return len(self._list)
    
    def _fixHeapBottomUp(self,):
        cindex  = len(self._list)-1
        while(True):
            pindex = self._get_parent(cindex)
            if self._list[pindex] >= self._list[cindex]:
                break
            self._list[pindex],self._list[cindex]=self._list[cindex],self._list[pindex]
            cindex = pindex

    def _fixHeapTopDown(self):
        self._list.insert(0, self._list.pop())
        cindex = 0
        while True:
            children = self._get_children(cindex)
            if all([self._list[cindex] >= self._list[chindex] for chindex in children]):
                break
            swap_index = cindex
            for chindex in children:
                swap_index = chindex if self._list[swap_index] < self._list[chindex] else swap_index 
            
            self._list[swap_index], self._list[cindex] = self._list[cindex], self._list[swap_index]
            cindex = swap_index

    def _get_parent(self, index):
        # if value is negative, node is root node
        # compare with self
        return max((index - 1) // self._num_children, 0) 
    

    def _get_children(self, index):
        children = []
        for num in range(self._num_children*index+1, self._num_children*index+1+self._num_children):
            if num < len(self._list):
                children.append(num)
            else:
                children.append(index)
        return tuple(children)    
    
    def __repr__(self) -> str:
        return str(self._list)




if __name__ == "__main__":
    test()
