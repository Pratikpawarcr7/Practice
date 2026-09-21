#include <iostream>
using namespace std;
class Demo
{
public:
    int A;
    int B;

    Demo()
    {
        cout << "Inside Demo Constructor" << "\n";
    }

    Demo(int A, int B)
    {
        cout << "Inside Parameterised Constructor" << "\n";
    }

    ~Demo()
    {
        cout << "Inside Distructor" << "\n";
    }

    void Fun()
    {
        cout << "Inside Fun" << "\n";
    }
};

int main()
{
    Demo dobj1;
    Demo dobj2(16, 29);
    dobj2.Fun();
}