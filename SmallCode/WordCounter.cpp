#include <iostream>
using namespace std;


int main() {

    string userInput;
    char letterToCount;
    int count = 0;
        
    cout << "Enter a word: ";
    cin >> userInput;

    cout << "Which letter to count?: ";
    cin >> letterToCount;

    for (int i = 0; i < userInput.length(); i++) {
        if (userInput[i] == letterToCount) {
            count++;
        }
    }
            cout << letterToCount << ": was in the word: " << count << " times" << endl; 

}