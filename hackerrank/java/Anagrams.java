import java.util.Scanner;

public class Anagrams {
    static boolean isAnagram(String a, String b) {
        if(a.length()!=b.length()){
            return false;
        }
        char[] arrA = a.toLowerCase().toCharArray();
        char[] arrB = b.toLowerCase().toCharArray();
        for(int i=0;i<arrA.length;i++){
            int countA = 0, countB=0;
            for(int j=0;j<arrA.length;j++){
                if(arrA[j] == arrA[i]){
                    countA++;
                }
                if(arrB[j] == arrA[i]){
                    countB++;
                }
                if(countA != countB){
                    return false;
                }
            }
        }
        return true;
        
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
    
}
