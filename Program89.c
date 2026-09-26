#include <stdio.h>
int Display(int iNo1)
{
    int iDigit = 0;
    int iSum = 0;

    if (iNo1 < 0)
    {
        iNo1 = -iNo1;
    }

    while (iNo1 > 0)
    {
        iDigit = iNo1 % 10;
        if (2 % iDigit == 0)
        {

            iSum = iSum + iDigit;
        }

        iNo1 = iNo1 / 10;
    }
    return iSum;
}
int main()
{
    int iValue1 = 0;
    int iRet = 0;
    printf("Enter The Number \n");
    scanf("%d", &iValue1);

    iRet = Display(iValue1);
    printf("Addition of Digit is : %d ", iRet);

    return 0;
}