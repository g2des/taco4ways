
/**
 * A node is defined as an object holding the actual data T
 * and link to the next object. Ideally typename T should have
 * operator== and operator<< functions
 */
template<typename T>
class Node{
    private:
        T data;
    public:
        Node * next;
        Node(T);
        const T& get_data();
};

/**
 * LinkedList is a collection of nodes chained by a single forward looking pointer.
 * This list uses sentinel to avoid special purpose coding
 */
template<typename T, class Node>
class LinkedList{
    private:
        Node* _top;
        int _size;
    public:
        LinkedList() : _top{Node(0)}, _size{0}{};
        const Node* findCellBefore(const T& t);
        void addToTop(const T& t);
        void addToBotton(const T& t);
        void insertAfter(const Node& afterme, const T& t);
        void deleteAfter(const Node& afterme);
        bool isEmpty();
        bool size();
        void printList();
        void destroyList();
};