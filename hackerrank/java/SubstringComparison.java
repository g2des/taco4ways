import java.util.Scanner;

public class SubstringComparison {
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = null;
        String largest = null;
        for(int i=0;i<s.length()-k+1;i++){
            String subs = s.substring(i, i+k);
            if(smallest == null){
                smallest = subs;
                largest = subs;
            }else if(smallest.compareTo(subs)>0){
                smallest = subs;
            }else if(largest.compareTo(subs)<0){
                largest = subs;
            }
        }
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
