#include <iostream>
using namespace std;
class Marvellous
{
public:
    int iNo1;
    int iNo2;

    Marvellous(int A, int B)
    {

        iNo1 = A;
        iNo2 = B;
    }

    int Addition()
    {

        int iResult = 0;
        iResult = iNo1 + iNo2;
        return iResult;
    }

    int Substraction()
    {

        int iResult = 0;
        iResult = iNo1 - iNo2;
        return iResult;
    }
};
int main()
{

    int iValue1 = 0;
    int iValue2 = 0;
    int iRet = 0;

    cout << "Enter the First Number : " << "\n";
    cin >> iValue1;

    cout << "Enter the Second Number : " << "\n";
    cin >> iValue2;

    Marvellous mobj(iValue1, iValue2);

    cout << "Addition : " << mobj.Addition() << "\n";
    cout << "Substraction : " << mobj.Substraction() << "\n";

    return 0;
}
