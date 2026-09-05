
import java.util.*;

class Addition {

	public int iNo1;
	public int iNo2;

	public Addition(int A, int B) {
		iNo1 = A;
		iNo2 = B;
	}

	public int AdditionX() {

		int iResult = 0;
		iResult = iNo1 + iNo2;
		return iResult;

	}
}

public class Program8 {

	public static void main(String Arr[]) {

		int iValue1;
		int iValue2;
		int iRet;

		Scanner sobj = new Scanner(System.in);

		System.out.println("Enter the First Number");
		iValue1 = sobj.nextInt();

		System.out.println("Enter the Second Number");
		iValue2 = sobj.nextInt();

		Addition sobjX = new Addition(iValue1, iValue2);

		iRet = sobjX.AdditionX();

		System.out.println("Addition : " + iRet);

		sobj.close();

	}

}
