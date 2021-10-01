//
// Created by admin on 10/24/2020.
//
#include <iostream>
#include <vector>
#include <stdexcept>
#include "LinkedList.h"
Node::Node(int n)
        : value(n){
    /*
     * Node pointer
     */
    next = nullptr;
}
Node::Node(int n, Node *p):value(n), next(p) {
    /*
     * Node pointer
     */
}

LinkedList::LinkedList(){
    /*
     * Default constructor
     */
    head = nullptr;
    tail = nullptr;
}
LinkedList::LinkedList(const std::vector<int>& v) {
/*
 * Overloaded constructor for vector/array input
 * Using call by reference to make more efficient code regarding to space
 */
    head = nullptr;
    tail = nullptr;
    for (int n:v){
        append(n);
    }
}


void LinkedList::append(int add) {
    /*
     * Append methoed
     */
    if (head == nullptr){
        head = new Node(add);
    }
    else if (tail == nullptr){
        tail = new Node(add);
        head->next = tail;
    }
    else{
        Node* current;
        current = tail;
        tail = new Node(add);
        current ->next = tail;
    }
}
void LinkedList::print() {
    /*
     *
     * Prints all the elements in the array using a while loop
     *
     */
    if (head == nullptr){
        std::cout <<"[]" << std::endl;
    }
    else{
        Node* current;
        current = head;
        std::cout <<"[";
        while (current->next != nullptr){
            std::cout << current-> value <<",";
            current = current -> next;
        }
        std::cout << current -> value << "]" << std::endl;
    }
}
LinkedList::~LinkedList() {
    /*
     * Destructor
     */
    Node* current;
    Node* next;
    current = head;
    while (current != nullptr){
        next = current ->next;
        delete current;
        current = next;
    }
}
Node *LinkedList::get_node(int index) {
    /*
     * Gets the element on a given index
     */
    Node* current;
    current = head;
    int i = 0;

    while(i < index && current != nullptr){
        current = current -> next;
        i+= 1;
    }
    return current;
}

void LinkedList::insert(int v, int index) {
    /*
     * Inserts an element on a given index
     */
    if (index == 0){
        head = new Node(v, head);
    }
    else {
        Node* temp;
        Node* next;
        temp = get_node(index-1);
        next = temp -> next;
        temp -> next = new Node(v, next);
    }
}
void LinkedList::remove(int index) {
    /*
     * Removes an element on a given index
     */
    Node* del = get_node(index);
    if (index == 0){
        head = del -> next;
        delete del;
    }
    else{
        Node* prev = get_node((index - 1));
        if (del -> next == nullptr){
            delete del;
            prev->next = nullptr;
        }
        else{
            prev -> next = del -> next;
            delete del;
        }
    }
}
int LinkedList::length() {
    /*
     * Returns length of array
     */
    int i = 0;
    Node* current = head;
    while(current != nullptr){
        i+= 1;
        current = current ->next;
    }
    return i;
}

int LinkedList::pop(int index) {
    /*
     * Returns the value on a given index and deletes it
     */
    Node* pop = get_node(index);
    int elem = pop -> value;
    remove(index);
    return elem;
}

int LinkedList::pop() {
    /*
     * Returns the last value and deletes it
     */
    int elem = tail -> value;
    remove((length() - 1));
    return elem;
}

int &LinkedList::operator[](int index) {
    /*
     * Operator methoed, throws error if exception
     */
    Node* elem = get_node(index);
    return elem-> value;
}










