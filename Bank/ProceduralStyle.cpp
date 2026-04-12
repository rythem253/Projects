#include <iostream>
using namespace std;

int CURR_BALANCE = 100;


int deposit() {

    int depositAmount;

    cout << "How much to deposit: ";
    cin >> depositAmount;

    if (depositAmount <= 0) {
        cout<<"Error"<< endl;
    } else {
        CURR_BALANCE +=  depositAmount;
    }
    return CURR_BALANCE;
}

int withdraw(){

    int withdrawAmount;

    cout << "Enter withdraw money: ";
    cin >> withdrawAmount;

    if (withdrawAmount > CURR_BALANCE) {
        cout << "Unsufficient balance!" << endl;
    } else {
        CURR_BALANCE -= withdrawAmount;
    }
    return CURR_BALANCE;
}

int main() {

    deposit();
    withdraw();

    cout << "Current balance: " << CURR_BALANCE;

}
