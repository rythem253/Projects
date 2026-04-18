#include <iostream>
#include "DOC.H"
using namespace std;

int main() {

    Node* listHead = nullptr; //Head of the linked-list
    int loop = 1;

    std::string input; 
    int choice;
    int t_del;

    while (loop) {
        cout << "Welcome to the Task Manager!\n";
        cout << "Please select an option:\n";
        cout << "1. Create a task\n";
        cout << "2. Delete a task\n";
        cout << "3. Display tasks\n";
        cout << "4. Exit\n";
        cin >> choice;
    switch (choice) {
        case 1:
            cout << "Creating a task...\n";
            cout << "Please type the task: ";
            cin.ignore(); //To clear the input stream.
            getline(cin, input); //Reads the whole line including spaces
            createNode(input, listHead);
            break;
        case 2:
            cout << "Select task number to delete: ";
            cin >> t_del;
            cout << "Deleting a task...\n";
            break;
        case 3:
            cout << "Displaying tasks...\n";
            displayLL(listHead);
            break;
       case 4:
            cout << "Exiting the Task Manager. Goodbye!\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
    }
}
	return 0;
}

    //This function adds a node into the linked-list
    void createNode(std::string usrInput, Node*& head) {
    Node* new_Node = new Node;
    new_Node->task = usrInput;
    new_Node->next = head;
    head=new_Node;
}

    //Traverse the linked list to display all the tasks
    void displayLL(Node* head) {
    Node* temp = head;
    while (temp->next != NULL) {    
        temp = temp->next;
        cout << temp->task << endl;
    }
}

/**
    void deleteNode(Node* head, int t_Num) {
        Node* temp = head;
        Node* prev = nullptr;

        while (temp->task != t_Num) {
            prev=temp;
            temp = temp->next;

            if (temp == NULL) {
                return;
            }
            prev->next = temp->next;
        }
    }
*/