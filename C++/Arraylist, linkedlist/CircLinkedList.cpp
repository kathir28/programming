//
// Created by admin on 10/25/2020.
//

#include "CircLinkedList.h"
/*

Node::Node(int n)
        : value(n){
    next = nullptr;
}
Node::Node(int n, Node *p):value(n), next(p) {
}
CircLinkedList::CircLinkedList(){
    head = nullptr;
    int size = 0;
}

void CircLinkedList::append(int add) {
    if (head == nullptr){
        head = new Node(add);
        head -> next = head;
        size +=1;
    }
    else{
        Node* current;
        Node* temp;
        current = get_node(add);
        temp = new Node(add);
        current ->next = temp;
        temp -> next = head;
    }

}

Node *CircLinkedList::get_node(int index) {
    Node* current;
    current = head;
    int i = 0;
    while(i < index && current != nullptr){
        current = current -> next;
    }
    return current;
}
*/
