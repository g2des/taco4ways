import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ArrayListTensor {
    private static Scanner sc = new Scanner(System.in);
    private static void parseQueries(List<int[]> arr, int[][] queries){
        for(int[] query : queries){
            try{
                System.out.println(arr.get(query[0])[query[1]]);
            }catch(ArrayIndexOutOfBoundsException e){
                System.out.println("ERROR!");
            }
        }
    }
    public static void main(String[] args) {
        int n = sc.nextInt();
        List<int[]> arr = new ArrayList<>();
        for(int i=0;i<n;i++){
            int d = sc.nextInt();
            int[] subarr = new int[d];
            for(int j=0;j<d;j++){
                subarr[j] = sc.nextInt();
            }
            arr.add(subarr);
        }
        int q = sc.nextInt();
        int[][] queries = new int[q][2];
        for(int i=0;i<q;i++){
            queries[i][0]=sc.nextInt()-1;
            queries[i][1]=sc.nextInt()-1;
        }
        parseQueries(arr, queries);
    }
}
