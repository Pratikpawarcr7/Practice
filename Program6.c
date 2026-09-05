#include <stdio.h>

int Addition(int iVal_1, int iVal_2)
{

	int iResult = 0;
	iResult = iVal_1 + iVal_2;
	return iResult;
}
int main()
{

	int iNo1 = 0;
	int iNo2 = 0;
	int iRet = 0;

	printf("Enter the First Number : ", "\n");
	scanf("%d", &iNo1);

	printf("Enter the Second Number : ", "\n");
	scanf("%d", &iNo2);

	iRet = Addition(iNo1, iNo2);

	printf("Addition : %d ", iRet);

	return 0;
}