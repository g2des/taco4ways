#include "dsa.h"

template<typename T>
Node<T>::Node(T t) : data{t}, next{nullptr}{}

template<typename T>
const T& Node<T>::get_data(){
    return &(this->data);
}

template<typename T, class Node>
const Node* LinkedList<T, Node>::findCellBefore(const T& t){
    Node * node = this->_top;
    while(node->next != nullptr){
        if(node->get_data() == t){
            return node;
        }
        node = node.next;
    }
    return nullptr;
}
