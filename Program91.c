#include <stdio.h>
int Display(int iNo1)
{
    int iDigit = 0;
    int iRev = 0;

    if (iNo1 < 0)
    {
        iNo1 = -iNo1;
    }

    while (iNo1 > 0)
    {
        iDigit = iNo1 % 10;
        iRev = iRev * 10 + iDigit;
        iNo1 = iNo1 / 10;
    }

    return iRev;
}
int main()
{
    int iValue1 = 0;
    int iRet = 0;
    printf("Enter The Number \n");
    scanf("%d", &iValue1);

    iRet = Display(iValue1);

    printf("Reverse Number : %d ", iRet);

    return 0;
}