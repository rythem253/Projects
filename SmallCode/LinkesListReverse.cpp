#include <iostream>
using namespace  std;

struct Node {
    int data;
    Node* next;
};

//Function prototypes, so my functions are before the main.
void reserveFunction();
void addNumbers();

//Main function.
int main() {

    addNumbers();

}

void addNumbers() {

    int userInput;

    cout << "Enter 5 digits, each on another line: " << endl;

    for (int i = 0; i<5; i++) {
        cin >> userInput;
    }

    // Node* addNode = new Node{userInput, nullptr};
}
//Function which takes the userInput and reverses it.
void reserveFunction() {


}