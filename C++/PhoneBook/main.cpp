#include <iostream>
#include <limits>

using namespace std;

struct Node {

    int data;
    Node* next;

};

void addNumber();
void deleteNumber();
void displayList(Node* head);

Node* head = nullptr;

int main() {

cout << "--------Phone Book--------" << endl;
cout << "To ADD a contact, Press 1" << endl;
cout << "To DELETE a contact, Press 2" << endl;
cout << "To VIEW contacts, Press 3" << endl;

char userInput;

do {

    cout << "Enter your choice:";
    cin >> userInput;

        if (userInput == '1') {
            addNumber();
        }

        if (userInput == '2') {
            deleteNumber();
        }

        if (userInput == '3') {
            displayList(head);
        }

    } while (userInput != 'q' && userInput != 'Q');
}

void addNumber() {

    int phoneNumber;
    cin >> phoneNumber;

    Node* newNode = new Node{phoneNumber, nullptr};

    // Add node to the front
    if (head == nullptr) {
        head = newNode;
    } else {
        newNode->next = head;
        head = newNode;
    }
}


void deleteNumber() {

    //delete the selected;
    int numberToDelete;
    
    cout << "Enter a task to delete";
    cin >> numberToDelete;

   

    Node* prev = nullptr;
    Node* current = head;

    while (current != nullptr && current->data != numberToDelete) {
        prev = current;
        current = current->next;
    }

    prev->next = current->next;
   
}

void displayList(Node* head) {

    //use for while-loop to display the list;

    Node* current = head;

    while (current != nullptr) {
        cout << current->data << " " << endl;
        current = current->next;
        }
    }