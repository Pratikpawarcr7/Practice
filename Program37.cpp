#include <iostream>
using namespace std;
class Demo
{

public:
    int A;
    int B;

    void Fun()
    {

        cout << "Inside Fun" << "\n";
        cout << A << "\n";
        cout << B << "\n";
    }

    void Gun()
    {
        cout << "Inside Gun";
    }
};
int main()
{
    Demo obj;
    obj.A = 16;
    obj.B = 29;

    cout << obj.A << "\n";
    cout << obj.B << "\n";

    obj.Fun();
    obj.Gun();
}