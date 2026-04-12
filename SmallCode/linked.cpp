#include <iostream>
#include <sstream>
#include <string>

using namespace std;

struct Node {
    int data;
    Node* next;
};

int main() {

    //I made all the nodes, from 1 to 4.
    Node* head = new Node{1, nullptr};
    Node* first = new Node{2, nullptr};
    Node* second = new Node{3, nullptr};
    Node* third = new Node{4, nullptr};

    //Now I will link the nodes, all togheter in order.
    head->next = first;
    first->next = second;
    second->next = third;

    //Make a new node, temp which will be pointing to head, and 
    //then iterate untill null.
    Node* current = head;

    while (current != nullptr) {
        cout << current->data << "->";
        current = current->next;
    }

    cout << "" << endl;
    cout << "" << endl;
    


    //                                     **This is where insertion begins**                
                                            
    
    //Add Item at a random space
    cout << "Adding a 10 after node 2" << endl;
    

    Node* newNode = new Node{10, nullptr};

    first->next = newNode;
    newNode->next = second;

    current = head;

    while (current != nullptr) {
    cout << current->data << "->";
    current = current->next;
    
    }


    //Add Item at front
    //Add Item at end
    //Made a circular linked list


    cout << " null" << endl;
    cout << " " << endl;

    cout << "Deleting 3" << endl;

    first->next= second->next;
    delete second;

    //print list after deleting
    current = head;
    while (current != nullptr) {
        cout << current->data << "->";
        current = current->next;
    }

    cout << " null" << endl;

    //Delete head node
    cout << " " << endl;
    cout << "Deleting head" << endl;

    Node* temp = head;
    head = head->next;
    delete temp;

    current = head;
    while (current != nullptr) {
        cout << current->data << "->";
        current = current->next;
    }

    cout << "x" << endl;
    cout << "" << endl;

    cout << "Delete 4" << endl;

    //Delete middle node aka, 4
    head->next = third->next;
    delete third;

    current = head;
    while (current != nullptr) {
        cout << current->data << "->";
        current = current->next;
    }

    cout << "x" << endl;
    cout << "" << endl;

    cout << "Delete head" << endl;

    //Delete head
    Node* tempN = head;
    head = head->next;
    delete tempN;

    current = head;
    
    while (current != nullptr) {
        cout << current->data << "->";
        current = current->next;
    }

    cout << "x" << endl; 

}


