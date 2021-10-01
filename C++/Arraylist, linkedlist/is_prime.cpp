//
// Created by admin on 10/16/2020.
//
#include "is_prime.h"
bool is_prime(int n){
    int i = 2;
    while(i <= (n / 2)){
        if(n % i == 0){
            return false;
        }
        i+= 1;
    }
    return true;
}
