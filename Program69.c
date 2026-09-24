#include <stdio.h>
#include <stdbool.h>
int Display(int iNo)
{
    int iCnt = 0;
    int iSum = 0;
    for (iCnt = 1; iCnt < iNo; iCnt++)
    {
        if (iNo % iCnt == 0)
        {
            iSum = iSum + iCnt;
        }
    }

    if (iSum == iNo)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{

    int iValue = 0;
    bool iRet = false;
    printf("Enter the Number : \n");
    scanf("%d", &iValue);

    iRet = Display(iValue);
    if (iRet == true)
    {
        printf("%d is Perfect Number", iValue);
    }
    else
    {
        printf("%d is Not a Perfect Number", iValue);
    }
}