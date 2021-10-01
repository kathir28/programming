//
// Created by admin on 10/9/2020.
//
#include <stdexcept>
#include <iostream>
#include <vector>
#include "ArrayList.h"

ArrayList::ArrayList() {
    /*
     * Default constructor, makes new array with a fixed capacity
     */
        size = 0;
        capacity = 1;
        data = new int[capacity];
        growthfactor = 2;
}
ArrayList::ArrayList(const std::vector<int>& v)
    /*
     * Using call by reference to make more efficient code regarding to space
     * Overloaded constructor thas takes vector as input
     */
    {
        size = 0;
        capacity = 1;
        data = new int[capacity];
        growthfactor = 2;
        for (int i : v){
            append(i);
        }
    }
ArrayList::~ArrayList() {
    /*
     * Delete methoed
     */
    delete[] data;
}

void ArrayList::append(int n) {
    /*
     * Append methoed, resizes and shrinks if necassary, sets the last value
     */
    if (size >= capacity){
        resize();
    }
    data[size] = n;
    size += 1;
    if (size < capacity*0.25){
        shrink_to_fit();
    }
}
void ArrayList::resize() {
    /*
     * Resizes the array with a fixed growthfactor
     */
    if (size >= capacity) {
        int * temp = new int[capacity * growthfactor];
        for (int n = 0; n < capacity; n++)
            temp[n] = data[n];
        delete[] data;
        data = temp;
        capacity = capacity * growthfactor;
    } else{
        //dette skal aldri skje
        std::cout <<"ERROR WITH RESIZE" << std::endl ;
    }
}
int ArrayList::length() const {
    /*
     * Returns size
     */
    return size;
}
int& ArrayList::operator[](int i){
    /*
     * Operator methoed, throws error if exception
     */
    if(0 <= i && i <= size){
        return data[i];
    }else{
        throw std::range_error("Indeks ikke gyldig");
    }
}
void ArrayList::insert(int index, int n) {
    /*
     * Inserts an element on a given index, iterates over the array and changes the index
     */
    if (capacity == size) {
        resize();
    }
    if(index == size){
        append(n);
    }
    else{
        for (int i = size; i >= index; i--) {
            data[i + 1] = data[i];
        }
        data[index] = n;
        size += 1;
    }
}
void ArrayList::remove(int index) {
    /*
     * Delets an element on a given index, iterates over the array and changes the index
     */
    if (index >= 0) {
        for (int i = index; i < size; i++)
            data[i] = data[i + 1];
        size -= 1;
        if (size < capacity*0.25){
            shrink_to_fit();
        }
    } else {
        throw std::range_error("Indeks ugyldig");
    }
}
int ArrayList::get(int index) {
    /*
     * Gets the element on a given index, throws error if exception
     */
    if (index > 0 && index <= size) {
        return data[index];
    } else {
        throw std::range_error("Indeks ugyldig");
    }
}
void ArrayList::set(int index, int value) {
    /*
     * Overwrites the value on a given index
     */
    if (index <= size)
        data[index] = value;
    else
        throw std::range_error("Indeks ugyldig");
}
void ArrayList::shrink_to_fit(){
    /*
     * Shrinks the array to the 2^n power
     */
    for (int i = 0; i < 50; i++){
        if (size <= pow(2,i)){
            int * temp = new int[pow(2,i)];
            for (int n = 0; n < capacity; n++)
                temp[n] = data[n];
            delete[] data;
            data = temp;
            capacity = pow(2,i);
            break;
        }else{
            continue;
        }
    }
}
void ArrayList::print(){
    /*
     * Prints all the elements in the array
     */
    for (int i = 0; i < size; i++)
        std::cout << data[i] << " ";
    std::cout <<" " << std::endl;
}
int ArrayList::pop(int n){
    /*
     * Returns the value on a given index and deletes it
     */
    int elem = get(n);
    remove(n);
    return elem;
}
int ArrayList::pop(){
    /*
     * Returns the last value and deletes it
     */
    int elem = pop((size-1));
    return elem;
}
