import java.util.*;

class Display {
    public int iNo1;

    public Display(int A) {
        iNo1 = A;
    }

    public void Number() {
        int iCnt = 0;

        System.out.println("Numbers Are : ");
        for (iCnt = 1; iCnt <= iNo1; iCnt++) {
            System.out.println(iCnt);

        }
    }

}

public class Program72 {

    public static void main(String Arr[]) {

        int iValue1 = 0;

        Scanner sobj = new Scanner(System.in);

        System.err.println("Enter the Number : ");
        iValue1 = sobj.nextInt();

        Display dobj = new Display(iValue1);

        dobj.Number();
        sobj.close();

    }

}
