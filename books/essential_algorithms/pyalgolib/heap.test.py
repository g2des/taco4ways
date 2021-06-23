from hashlib import new
from math import acosh
import unittest
from heap import Heap
from random import randint

class TestHeap(unittest.TestCase):
	
    
    def get_heap(self, count=10):
        aheap = Heap()
        for _ in range(count):
            aheap.push(randint(1, 200))
        return aheap
    
    def test_index_of_child(self):
        aheap = self.get_heap()
        assert aheap._get_children(0) == (1,2)
        assert aheap._get_children(1) == (3,4)
        assert aheap._get_children(2) == (5,6)
        assert aheap._get_children(3) == (7,8)
        assert aheap._get_children(4) == (9,4)
        assert aheap._get_children(5) == (5,5)
        assert aheap._get_children(6) == (6,6)
    
    def test_index_of_parent(self):
        aheap = self.get_heap()
        assert aheap._get_parent(0) == 0
        assert aheap._get_parent(1) == 0
        assert aheap._get_parent(2) == 0
        assert aheap._get_parent(3) == 1
        assert aheap._get_parent(4) == 1
        assert aheap._get_parent(5) == 2
        assert aheap._get_parent(6) == 2

    def test_after_every_push_largest_val_moves_up(self):
        
        aheap = self.get_heap(count=200000)
        for pindex in range(20):
            chindex1, chindex2 = aheap._get_children(pindex)
            assert aheap._list[pindex] >= aheap._list[chindex1]
            assert aheap._list[pindex] >= aheap._list[chindex2]

    def test_after_every_pop_largest_value_moves_up(self):
        aheap = self.get_heap(count=200000)
        while not aheap.is_empty():
            aheap.pop()
            for pindex in range(len(aheap)):
                chindex1, chindex2 = aheap._get_children(pindex)
                print(chindex1, chindex2, pindex)
                assert aheap._list[pindex] >= aheap._list[chindex1]
                assert aheap._list[pindex] >= aheap._list[chindex2]
        
    def test_sorted(self):
        aheap = self.get_heap(count=200000)
        sorted_list = sorted(aheap._list)
        while not aheap.is_empty():
            assert aheap.pop() == sorted_list.pop()
        assert len(sorted_list) == len(aheap)

if __name__ == '__main__':
    unittest.main() 