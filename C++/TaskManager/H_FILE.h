#ifndef H_FILE_H
#define H_FILE_H

#include <string>

typedef struct ht_items
{
    char* data;
    char* value; 
} ht_items;

//Hash table 
typedef struct hashTable
{
    /* data */
    ht_items** items;
    int size;
    int count;
} hashtable;

//Linked list
struct Node {
    int val;
    Node* next;
};


#endif // H_FILE_H
