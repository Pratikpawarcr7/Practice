#include <stdio.h>
void Display(int iNo1)
{
    int iDigit = 0;

    while (iNo1 > 0)
    {
        iDigit = iNo1 % 10;
        printf("%d", iDigit);
        iNo1 = iNo1 / 10;
    }
}
int main()
{
    int iValue1 = 0;
    printf("Enter The Number \n");
    scanf("%d", &iValue1);

    Display(iValue1);

    return 0;
}