#include <stdio.h>
int Display(int iNo1)
{
    int iDigit = 0;
    int iCount = 0;

    if (iNo1 < 0)
    {
        iNo1 = -iNo1;
    }

    while (iNo1 > 0)
    {
        iDigit = iNo1 % 10;
        iCount++;
        iNo1 = iNo1 / 10;
    }
    return iCount;
}
int main()
{
    int iValue1 = 0;
    int iRet = 0;
    printf("Enter The Number \n");
    scanf("%d", &iValue1);

    iRet = Display(iValue1);
    printf("Count of Digit is : %d ", iRet);

    return 0;
}