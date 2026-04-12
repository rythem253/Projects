#include <iostream>
using namespace  std;

struct Node {
    int data;
    Node* next;
};

//Function prototypes, so my functions are before the main
void addNode();
void removeNode();
void displayList(Node* head);

Node* head = nullptr;

int main() {

    cout << "ToDo-List Project" << endl;
    cout << "" << endl;
    cout << "Press 1: to add a task" << endl;
    cout << "Press 2: to remove a task" << endl;
    cout << "Press 3: to view tasks" << endl;
    cout << "" << endl;
    cout << "To quit, press 'q'" << endl;

    char userInput;

    do {
        cout << "Enter your choice: ";
        cout << " ";
        cin >> userInput;

        if (userInput == '1') {
            addNode();
        }

        if (userInput == '2') {
            removeNode();
        }

        if (userInput == '3') {
            displayList(head);
        }

    } while (userInput != 'q' && userInput != 'Q');
}

//Adds nodes, aka nodes.
void addNode() {

    int task;

    cout << "Task number to add:";
    cin >> task;

    Node* taskNode = new Node{task, nullptr};

    if (head == nullptr) {
        head = taskNode;
    } else {
        taskNode->next = head;
        head = taskNode;
    }
}

//Removes nodes, aka tasks.
void removeNode() {

    int taskToDelete;

    cout << "Enter a task to delete:" << endl;
    cin >> taskToDelete;

    Node* current = head;
    Node* prev = nullptr;
    
    while (current != nullptr && current->data != taskToDelete) {
        prev = current;
        current = current->next;
    }

    prev->next = current->next;

    //Bug: If the task to delete is the head, the program gives Segmentation Fault, 
    //since we are deleting the head pointer without fixing it. Make sure u fix that.
    //if 

}

//Displays the state of the list.
void displayList(Node* head) {

    Node* current = head;

    cout << "Your tasks:" << endl;
    while (current != nullptr) {
        cout << current->data << " " << endl;
        current = current->next;
    }
}

