#include <iostream>
using namespace std;

const int MAX = 10;
int stack[MAX];
int top = -1;

bool empty() {
    return top == -1;
}

bool full() {
    return top == MAX - 1;
}

void push(int value) {
    if (full()) {
        cout << "Stack Overflow!" << endl;
    } else {
        stack[++top] = value;
        cout << value << " pushed to stack." << endl;
    }
}

void pop() {
    if (empty()) {
        cout << "Stack Underflow!" << endl;
    } else {
        cout << "Value popped: " << stack[top--] << endl;
    }
}

int main() {
    int choice, val;

    while (true) {
        cout << "\nChoose operation:\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            if (full()) {
                cout << "Stack Overflow! Cannot push." << endl;
                break;
            }
            cout << "Enter value to push: ";
            cin >> val;
            push(val);
        }
        else if (choice == 2) {
            if (empty()) {
                cout << "Stack Underflow! Cannot pop." << endl;
                break;
            }
            pop();
        }
        else {
            cout << "Invalid input. Enter 1 or 2 only." << endl;
        }

    }

    return 0;
}
