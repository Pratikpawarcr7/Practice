#include <iostream>
using namespace std;

class Addition
{

public:
	int iValue1;
	int iValue2;

	Addition(int A, int B)
	{
		iValue1 = A;
		iValue2 = B;
	}

	int AdditionX()
	{
		int iResult = 0;
		iResult = iValue1 + iValue2;
		return iResult;
	}
};
int main()
{

	int iNo1 = 0;
	int iNo2 = 0;
	int iRet = 0;

	cout << "Enter the First Number" << endl;
	cin >> iNo1;

	cout << "Enter the Second Number" << endl;
	cin >> iNo2;

	Addition aobj1(iNo1, iNo2);

	iRet = aobj1.AdditionX();

	printf("Addition : %d ", iRet);

	return 0;
}