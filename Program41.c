#include <stdio.h>

int Addition()
{
    int iNo1 = 21;
    int iNo2 = 20;
    int iResult = 0;

    iResult = iNo1 + iNo2;

    return iResult;
}
int Substraction(int iNo1, int iNo2)
{

    int iResult = 0;

    iResult = iNo1 - iNo2;

    return iResult;
}

int main()
{
    int iRet = 0;

    iRet = Addition();

    printf("Addition is : %d\n", iRet);

    iRet = Substraction(16, 29);

    printf(" Substraction is : %d ", iRet);

    return 0;
}