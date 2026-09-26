#include <stdio.h>
int main()
{
    int iNo1 = 122344;

    int iDigit = 0;

    while (iNo1 > 0)
    {
        iDigit = iNo1 % 10;
        printf("%d", iDigit);
        iNo1 = iNo1 / 10;
    }

    return 0;
}