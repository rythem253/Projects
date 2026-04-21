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
        cout << "==========Welcome to the Task Manager!==========\n";
        cout << "          Please select an option:\n";
        cout << "------------------------------------------------\n";
        cout << "1. Create a task\n";
        cout << "2. Delete a task\n";
        cout << "3. Display tasks\n";
        cout << "4. Exit\n";
        cout << "\n";
        cout << "\n";
        cin >> choice;
    switch (choice) {
        case 1:
            cout << "Please type the task:";
            cin.ignore(); //To clear the input stream.
            getline(cin, input); //Reads the whole line including spaces
            createNode(input, listHead);
            break;
        case 2:
            cout << "Select task number to delete: ";
            cin >> t_del;
            deleteNode(listHead, t_del);
            break;
        case 3:
            cout << "Displaying tasks:\n";
            displayLL(listHead);
            break;
       case 4:
            cout << "Exiting the Task Manager. Goodbye!\n";
            exit(1);
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
    new_Node->next = nullptr;
    //Need to make new node append at the end, not at front.
    //Need to make a whole loop for that, to append at the end of the linked list.

    if (head == nullptr) {
        head = new_Node;
        return;
    }

    Node* temp = head;

    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = new_Node;
}

    //Traverse the linked list to display all the tasks
    void displayLL(Node* head) {

    int count = 1;
    
    Node* temp = head;
    while (temp != NULL) {    
        cout << count << "." <<temp->task << endl;
        temp = temp->next;
        count++;
    }
}

    void deleteNode(Node* head, int t_Num) {

        int count =1;

        Node* temp = head;
        Node* prev = nullptr;

        //Need code to delete head of the linked-list

        while (temp != NULL) {
            prev=temp;
            temp = temp->next;

            if (temp == NULL) {
                return;
            }

            if (count == t_Num) {
                prev->next = temp->next;
            }
            count++;
        }
    }
