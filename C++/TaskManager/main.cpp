#include <iostream>
#include "DOC.H"
using namespace std;

int main() {

    cout << "Welcome to the Task Manager!\n";
    cout << "Please select an option:\n";
    cout << "1. Create a task\n";
    cout << "2. Delete a task\n";
    cout << "3. Display tasks\n";
    cout << "4. Exit\n";

    std::string input; 
    int choice;
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "Creating a task...\n";
            cout << "Please type the task: ";
            getline(cin, input); //Reads the whole line including spaces
            break;
        case 2:
            cout << "Deleting a task...\n";
            // Placeholder for task deletion logic
            break;
        case 3:
            cout << "Displaying tasks...\n";
            // Placeholder for displaying tasks logic
            break;
        case 4:
            cout << "Exiting the Task Manager. Goodbye!\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
    }

	return 0;
}

    //This function adds a node into the linked-list
    void createNode(std::string usrInput, Node*& head) {
      
    }
