#include <iostream>
using namespace std;

class Test
{
private:
    
int x = 50;

public:

    void setX(int setX) {


        if (setX > 1000) {
            cout<<"Error"<<endl;        //Does not set setX to X unless less than 1000.
        } else {
            cout<<"Fine"<<endl;         //Sets setX to X only if less than X.
            x = setX;
        }
    }

    int getX() {
        return x;
    }

};

int main() {

    Test t;

    cout << "Default Value: " << t.getX() << endl;

    t.setX(2000);
    cout << "Changed Valued: " << t.getX() << endl;
}




