#include <stdio.h>
#include <stdbool.h>

int CheckDivisible(int iNo)
{

    if (((iNo % 3) == 0) && ((iNo % 5) == 0))
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
    bool bRet = false;
    printf("Enter the number\n");
    scanf("%d", &iValue);

    bRet = CheckDivisible(iValue);
    if (bRet == true)
    {
        printf("%d is divisible by 3 and 5", iValue);
    }
    else
    {
        printf("%d is not divisible by 3 and 5", iValue);
    }

    return 0;
}