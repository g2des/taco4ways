import java.util.Scanner;

class IfElse {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int myInt = sc.nextInt();
        String weird = "Weird";
        String notWeird = "Not Weird";
        if(myInt%2 !=0){
            System.out.println(weird);
        }else if((myInt >=2 && myInt <=5) || (myInt>20)){
            System.out.println(notWeird);
        }else{
            System.out.println(weird);
        }

        sc.close();
    }
    
}
