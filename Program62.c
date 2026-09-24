#include <stdio.h>

void Display()
{
    int iCnt = 0;

    printf("Numbers Are : ");

    for (iCnt = 1; iCnt <= 10; iCnt++)
    {
        printf("%d\n", iCnt);
    }
}

int main()
{

    Display();

    return 0;
}