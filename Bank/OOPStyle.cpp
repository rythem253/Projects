#include <iostream>
using namespace std;

class Withdraw {
private:
    int withdrawMoney;
    int startingAmount;

public:
    // Constructor
    Withdraw(int amount) {
        startingAmount = amount;
        withdrawMoney = 0;
    }

    void setWithdraw(int drawX) {
        if (drawX > startingAmount) {
            cout << "Error, can't withdraw more than you have!" << endl;
        } else {
            withdrawMoney = drawX;
            startingAmount -= withdrawMoney;
        }
    }

    int getWithdraw() {
        return withdrawMoney;
    }

    int afterWithdrawal() {
        return startingAmount;
    }

    int& getStartingAmountRef() {
        return startingAmount;
    }
};

class Deposit {
private:
    int depositMoney;

public:
    // Constructor
    Deposit(int toDeposit) {
        depositMoney = toDeposit;
    }

    void setDeposit(int depositX, int& startingAmount) {
        if (depositX <= 0) {
            cout << "Can't deposit 0 or less!" << endl;
        } else {
            depositMoney = depositX;
            startingAmount += depositMoney;
        }
    }

    int getDeposit() {
        return depositMoney;
    }
};

int main() {
    int startingAmount = 500;

    Withdraw w(startingAmount);
    w.setWithdraw(12);
    cout << "Withdrawn Amount: " << w.getWithdraw() << endl;
    cout << "Remaining after withdrawal: " << w.afterWithdrawal() << endl;

    // Sync updated balance from Withdraw
    startingAmount = w.afterWithdrawal();

    Deposit d(0);  // Provide dummy value for constructor
    d.setDeposit(500, startingAmount);
    cout << "Deposited: " << d.getDeposit() << endl;
    cout << "Current Balance: " << startingAmount << endl;

    return 0;
}
