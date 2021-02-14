import java.util.Scanner;

public class JavaLoop1 {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int myInt = sc.nextInt();
        for(int i=1;i<=10;i++){
            System.out.printf("%d x %d = %d\n", myInt, i, myInt*i);
        }
    }
}
