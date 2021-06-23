# Data Structures

## Linked Lists

### Concept
- consists of cells linked together
- need a variable to point to top (and bottom) of the list
- sentinel is a node at top (and bottom) of the list to remove special purpose coding

### Interface
- FindCellBefore(top, target_value) throws value not found exception, value is none
- AddAtTop(top, new_cell) throws no memory allocated exception
- AddAtBottom(top, new_cell) throws no memory allocated exception
- InsertAfter(after_me, new_cell) throws null pointer exception
- DeleteAfter(after_me) throws null pointer exception
- DestroyList(top)
- PrintList(top)
    
### Types

#### Singly linked list

#### Doubly linked list

#### Sorted linked list
- singly linked list with two sentinels
- Top sentinel having smallest possible value
- Bottom sentinel having largest possible value

#### Multi Threaded linked list
- a list with links providing different kinds of movement
- planet list, one by position from sun, other by size of the planted

#### Circular linked list
- start and end at the sentinel
  
### Algorithms

#### Copying list

#### Sorting *add details*
- Insertion sort
- Selection sort

#### Finding and breaking loops *add details*
- Marking Cell
- Using Hash Tables
- List Reversal
- List Retracing
- Tortoise and hare algorithm

## Arrays : TODO

## Stacks

### Concept
- stacks are LIFO data structures

### Interface
- push(top, value): throws stack is full exception
- pop(top): throws stack empty exception and returns value on top
- peek(top): returns value on top

### Types
#### Linked List Stack
#### Array Stack
#### Double Stack

### Algorithms

#### Tower of Hanoi Problem
- move circular disk from one pole to another
- constraint is there are only three poles and larger disk cannot be on top of smaller disk

#### Train Sorting
- group carriages for same destination together

#### Reversing an Array
#### Stack Insertion Sort
#### Stack Selection Sort

## Queues
### Concept
- queues follow last in first out mechanism
### Interface
- enqueue(bottom, value) throws queue full exception
- dequeue(top) throws queue empty exception

### Types

#### Linked List Queues
#### Array Queues
- values move forward in the queue as values are enqueued and dequeued
- this can be solved by using circular queues and wrapping next to start
- creates ambiguity as `next==top` means either queue is empty of full
- simple solution is to make `next + 1 == top` as full and `next==top` as empty

#### Priority Queue
- elements are removed in the order of priority
- heap based implmenetation provides best solution

#### Deques
- double ended queue
- useful where you have partial information about priority of items






## Heap
### Concept
- a heap is a complete binary tree
- complete binary tree is one where all levels except the leaf nodes are full
- every parent node is greater than all of it's children
- complexity to build heap $O(NlogN)$
- easy to save in array
  - $child\_nodes(i) = \{node_{2*i+1}, node_{2*i+2}\}$
  - $parent\_node(i) = {\lfloor \frac{i-1}{2} \rfloor}$
- how to reset after a pop?
  - move the last element to the top
  - swap with the largest child
  - repeat till no more swaps possible
- how to reset after a push?
  - swap the last element with parent if larger than parent
  - continue till no more swaps possible

### Interface
- push(T):void
- _fixHeapBottomUp():void
- _fixHeapTopDown():void
- pop():T
- _get_parent(index_t):index_t
- _get_child(index_t):(index_t, index_t)

# Algorithms

## Randomization : TODO

## Sorting

### $O(N^2)$

#### InsertionSort

- Add an item in the list in sorted position in another list
- For inplace, index i defines the boundary of sorted and unsorted array
- return another list
- **WORKING**
  - for an item located at index i
  - it takes j steps to find the new location
  - i-j steps to move elements one step right(except in linkedlist)
  - so i steps for item located at index i
  - i.e $1+2+3+4+...+N = {(N^2 + N)}/{2} \implies O(N^2)$
  
  #### Selectionsort

  - Find largest number and swap it with the position we are trying to sort for
  - Alernatively, find smallest number in remaining part of the list and swap with position we are looking at
  - **WORKING**:
    - For finding an element at index i in array of N elements
    - $N-i$ steps for finding the right element
    - 1 for swapping the elements
    - i.e $N-1 + N-2 + ... + 3+2+1 = (N^2 - N)/2 \implies O(N^2)$

#### Bubblesort

- swap two numbers if they are out of order
- **WORKING**:
  - swap two numbers until no more swapping is possible
  - at every step at least one element reaches its final position
  - so at most we will have to make N passes over the dataset
  - i.e. $N*N= N^2$
- **IMPROVEMENTS**:
  - `swap in alternating direction` will move smaller elements to start and larger elements to bottom more quickly
  - some elements require multiple swaps so it is better to store them in temp variable and `directly insert them at their final position` while moving other elements one index.
  - you `don't need to scan beyond last swapped index` as all elements beyond that swap are already sorted.


### $O(NlogN)$

#### Heapsort

- build a heap; remove root node and move it to end of the array; for the remaining N-1 elements estabish heap properties
- While asymptotically heapsort has complexity of $NlogN$, usually, quicksort runs faster than heapsort 
- can be easily parallalized
- **WORKING**:
  - for every element added it at index i, it may take at most $log_2(i)$ step to move it to correct position, base 2 coz it is binary tree
  - i.e. $ \sum_i log(i) \implies \because \sum_i log(i) \leq Nlog(N) \implies O(NlogN)$

#### Quicksort
- determine a dividing point and move elements less than divider to left and greater than or equal to, to the right
- recursively do so for the left and the right partition
- in best case complexity of $O(NlogN)$ and $O(N^2)$ in worst case
- **WORKING**:
  - at each step we select a divider and move elements left or right
  - in best case, the divider creates partitions of equal sizes in each step
  - so $logN$ levels are required
  - at each step we scan through the entire list with
  - i.e. $O(NlogN)$
  - in worst case the partition will one less element than previous step 
  - so $N-1 \rightarrow N-2 \rightarrow N-3 \rightarrow ... \rightarrow 1 \implies (N^2 - N)/2 $
  - and since we still can N elements in each iteration $\implies O(N^2)$
- What is necessary is good strategy to select the divider

#### Mergesort
- divide array recursively into two eqaul halves
- linearly sort two equal halves to build the array
- is a stable sorting algorithm as it maintains relative order of elements in the array
- possible to parallalize
- needs additional constraints to complete both recursions before linearly sorting elements
- **WORKING**:
  - since we divide array into two equal halves, the tree will be $logN$ long.
  - linearly sorting the two halves mean that we scan N elements in each iteration
  - $\implies O(NlogN)$

### $Sub(O(NlogN))$

#### Countingsort
- for elements in a limited range
- count instance of each element
- build an array based on the count
- **WORKING**:
  - for an array of N elements in range M
  - it takes M iterations to initialize an array
  - N iterations to count the elements
  - N iterations to build sorte array
  - M steps to move over elements
  - $\implies O(2(M+N)) \implies O(N+M)$ if N and M are comparable

#### Bucketsort
- bin all the elements in buckets
- sort elements in the buckets
- merge buckets to build sorted array
- **WORKING**:
  - for N elements and M buckets
  - if it is based on a uniform distribution with each bucket having N/M items
  - N steps to put elements in buckets using $\lfloor Val \div M \rfloor$
  - $M*F(N/M)$ to sort bucket with sorting algo complexity of $F$
  - M to go over all buckets and N to build array
  - if $M \lt M \implies O(N) + O(M* F(N/M)) + O(N) => O(N+M) \because F(N\div M) = c$



