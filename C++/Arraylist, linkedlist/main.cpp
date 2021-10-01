#include <iostream>
#include "ArrayList.h"
#include "is_prime.h"
#include "LinkedList.h"

int main() {
    //TASK 1
    /*test.append(2);
    test.append(5);
    test.append(7);
    test.append(11);
    test.append(13);
    test.append(17);
     */
    std::vector<int> v = {7,6,5,4};
    ArrayList test1(v);
    test1.print();
    ArrayList test;

    int i = 1;
    while(test.length() < 10){
        if(is_prime(i)){
            test.append(i);
        }
        i+= 1;
    }
    test.print();
    test.pop();
    test.remove(3);
    test.set(1,1000);
    test.print();

    //TASK 2

    LinkedList Test;
    Test.append(5);
    Test.append(7);
    Test.append(11);
    Test.append(13);
    Test.append(17);
    Test.print();
    Test.insert(3,2);
    Test.print();
    Test.remove(2);
    std::cout <<Test.length()<< std::endl;
    std::cout <<Test.pop(2)<< std::endl;
    Test.print();


    std::cout <<Test[1] << std::endl;
    std::cout <<Test.length()<< std::endl;
    /*
     * All the tests looks good
     */
    return 0;
}
