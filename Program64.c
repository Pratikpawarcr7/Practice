#include <stdio.h>
#include <stdbool.h>

bool Display(int iNo)
{
    int iResult = 0;
    iResult = iNo % 5;

    if (iResult == 0)
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
    printf("Enter the Number\n");
    scanf("%d", &iValue);
    iRet = Display(iValue);

    if (iRet == true)
    {
        printf("%d is Divisible By 5", iValue);
    }
    else
    {
        printf("%d is Not Divisible By 5", iValue);
    }

    return 0;
}