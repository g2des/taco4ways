import java.util.Scanner;

public class StdInStdOut{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<3;i++){
            int myInt = sc.nextInt();
            System.out.println(myInt);
        }
        sc.close();
        
    }

}
