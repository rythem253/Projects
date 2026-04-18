#ifndef DOC_H
#define DOC_H

#include <string>

/**
 * Unlike in C where u have to allocate memory for an array of input
 * in C++ it automatically takes care of you. 
 */
struct Node {
    std::string task; 
    Node* next;
};

#endif