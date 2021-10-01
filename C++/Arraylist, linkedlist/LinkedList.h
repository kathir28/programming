//
// Created by admin on 10/24/2020.
//

#ifndef PROJECT2_IN1910_LINKEDLIST_H
#define PROJECT2_IN1910_LINKEDLIST_H
struct Node{
    int value;
    Node*  next;
    Node(int v);
    Node (int n, Node* p);
};

class LinkedList {
private:
    Node* head;
    Node* tail;
    Node* get_node(int index);

public:
    LinkedList();
    LinkedList::LinkedList(const std::vector<int>& v);
    void append(int add);
    void print();
    ~LinkedList();
    void remove(int index);
    int length();
    void insert(int v, int index);
    int pop(int index);
    int pop();
    int& operator[](int index);
};


#endif //PROJECT2_IN1910_LINKEDLIST_H
