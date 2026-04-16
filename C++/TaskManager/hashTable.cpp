#include <iostream>
using namespace std;   

#define CAPACITY 500
#include "H_FILE.h"

unsigned long hash_function(char* str) {
    
    unsigned long i = 0;

    for (int j = 0; str[j]; j++)
        i += str[j];

    return i % CAPACITY;
}

//Initialize the hashtable, and set all entries to 0
hashTable* createHashTable(int size) {
    // Placeholder for hash table creation logic
    // Creates a new HashTable.
    cout << "Creating hash table...\n";
    hashTable* table = (hashTable*) malloc(sizeof(hashTable));
    table->size = size;
    table->count = 0;
    table->items = (ht_items**) calloc(table->size,sizeof(ht_items*));
    
    //Check if table is allocated properly
    if (table == NULL) {
        cout << "Err";
        return 0;
    }

    return 0; // Return a dummy value for now
}

int insertIntoHashTable(int key, int value) {
    // Placeholder for hash table insertion logic
    cout << "Inserting key: " << key << ", value: " << value << " into hash table...\n";
    return 0; // Return a dummy value for now
}

int deleteFromHashTable(int key) {
    // Placeholder for hash table deletion logic
    cout << "Deleting key: " << key << " from hash table...\n";
    return 0; // Return a dummy value for now
}

int searchHashTable(int key) {
    // Placeholder for hash table search logic
    cout << "Searching for key: " << key << " in hash table...\n";
    return -1; // Return a dummy value indicating not found
}

int displayHashTable() {
    // Placeholder for hash table display logic
    cout << "Displaying hash table contents...\n";
    return 0; // Return a dummy value for now
}