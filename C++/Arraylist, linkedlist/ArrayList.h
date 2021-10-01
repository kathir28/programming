//
// Created by admin on 10/9/2020.
//

#ifndef PROJECT2_IN1910_ARRAYLIST_H
#define PROJECT2_IN1910_ARRAYLIST_H
#include <vector>
class ArrayList{
private:
    int * data;
    int capacity;
    void resize();

public:
    int size;
    int growthfactor;
    ArrayList();
    ArrayList(const std::vector<int>& v);
    ~ArrayList();
    void append(int n);
    int length() const;
    int& operator[](int i);
    void insert(int index, int n);
    void remove(int index);
    int get(int index);
    void set(int index, int value);
    void shrink_to_fit();
    void print();
    int pop(int n);
    int pop();

};
#endif //PROJECT2_IN1910_ARRAYLIST_H
