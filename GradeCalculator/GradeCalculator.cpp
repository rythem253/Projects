#include <iostream>
using namespace std;

int main() {

    int userInput;
    int gradeInput;
    int displayGrade;
    int sum = 0;

        cout << "How many students? :";
        cin >> userInput;

        for (int i = 0; i < userInput; i++){
            cout << "Enter grade for student #" << i+1 << ": ";
            cin >> gradeInput;
            sum += gradeInput;
        }

        displayGrade = sum/userInput;

        cout << "Average grade is: " << displayGrade << endl;

}

