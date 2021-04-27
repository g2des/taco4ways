# Essential Algorithms


## Linked List

- A linked list is built of objects that are often called cells. The cell’s class contains whatever data the list must store plus a link to another cell.
- In addition to the list itself, a program needs a variable `top` that points to the list so that the code can find it.
- **Sentinel: A brilliant concept to code list more elegantly.**

### Singly Linked List

- Each cell is connected to the next cell with a single link.
- Interface: print, insert_at_start, insert_at_end, insert_after, find_before, delete_after, destroy_list