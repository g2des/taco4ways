import java.util.Scanner;

public class JavaEOF {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int i = 1;
        while(sc.hasNextLine()){
            System.out.println(i + " "+sc.nextLine());
            ++i;
        }
    }

}
