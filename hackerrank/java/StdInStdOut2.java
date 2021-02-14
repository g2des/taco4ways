import java.util.Scanner;

public class StdInStdOut2 {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int myInt = Integer.parseInt(sc.nextLine());
        double myDouble = Double.parseDouble(sc.nextLine());
        String myString = sc.nextLine();
        System.out.println("String: "+myString);
        System.out.println("Double: "+myDouble);
        System.out.println("Int: "+myInt);
        
    }
}
