#include <iostream>
using namespace std;

class Demo
{
public:
    Demo()
    {
        int A = 21;
        int &B = A;

        cout << "Value of A : " << A << "\n";
        cout << "Value of B : " << B << "\n";
    }
};

int main()
{
    Demo dObj;
}