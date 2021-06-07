/**
Singly linked list with sentinel
*/
#include<iostream>
using namespace std;
struct Node
{
    Node* next;
    int value;

    Node(int);
    bool operator== (int);
};

Node::Node(int value) : value{value}, next{nullptr}{}
// create new node
Node* create_node(int num=-1){
    Node* cell = new Node {num};
    cout << "New node witl value : " << cell->value<< endl;
    return cell;
}

bool Node::operator== (int value){
    if(this->value == value){
        return true;
    }
    return false;
}

// add node to the list : adds node to the top of the list
void add_node_at_head(Node* top, Node* cell){
    cell->next =top->next;
    top->next = cell;
}

// get node before
Node* get_node_before_value(Node*top, int value){
    Node* start = top;
    while(start->next != nullptr){
        if(*(start->next) == value){
            return start;
        }
        start = start->next;
    }
    return nullptr;
}

void add_node_after(Node*top, Node* cell, int value){
    Node* pos = get_node_before_value(top, value);
    pos = pos->next;
    cell->next = pos->next;
    pos->next = cell;
}

void add_node_before(Node*top, Node* cell, int value){
    Node* pos = get_node_before_value(top, value);
    cell->next = pos->next;
    pos->next = cell;
}
// remove node
void delete_node(Node* top, int value){
    Node *start = top;
    while(start->next->value != value){
        start = start->next;
    }
    // assumes node is always present
    Node* temp = start->next;
    cout << "Deleting value : " << temp->value << endl;
    start->next = start->next->next;
    delete temp;
}
// print list
void print_list(Node *top){
    Node* start = top;
    while(start->next != nullptr){
        cout << start->next->value << ", ";
        start = start->next;
    }
    cout << endl;
}
void destroy_list(Node* top) {
    Node* start = top;
    while(start->next != nullptr){
        int value = start->next->value;
        delete_node(top, value);
        print_list(top);
    }
    // cout << "HERE" <<top->next << top->value << endl;
    delete top;
}


int main(){
    Node* top;
    top = create_node();
    for(int i=1;i<6;i++){
        add_node_at_head(top, create_node(i));
    }
    print_list(top);
    add_node_before(top, create_node(12), 2);
    add_node_before(top, create_node(33),5);
    add_node_before(top, create_node(34),1);
    print_list(top);
    add_node_after(top, create_node(55), 33);
    add_node_after(top, create_node(56), 1);
    add_node_after(top, create_node(57), 12);
    print_list(top);
    delete_node(top, 33);
    delete_node(top, 55);
    delete_node(top, 56);
    delete_node(top, 1);
    delete_node(top, 3);
    print_list(top);
    destroy_list(top);
}