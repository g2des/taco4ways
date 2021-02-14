import java.util.Scanner;

public class JavaLoop2 {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int q = sc.nextInt();
        for(int i=0;i<q;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            int num = -1;
            for(int j=0;j<n;j++){
                num =  num == -1? a + (int) Math.pow(2, j) * b : num + (int) Math.pow(2, j) * b;
                System.out.printf("%d ", num);
            }
            System.out.println();
        }
    }
}
