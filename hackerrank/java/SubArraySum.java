import java.util.Scanner;

public class SubArraySum {
    private static Scanner sc = new Scanner(System.in);

    private static int sum(int arr[], int start, int end){
        int sum=0;
        for(int i=start;i<end;i++){
            sum +=arr[i];
        }
        return sum;
    }
    private static int getSubArraySum(int[] arr){
        int count = 0;
        for(int subLen = 1;subLen<=arr.length;subLen++){
            for(int start=0;start<=arr.length -subLen;start++){
                // System.out.println(start+" "+ (start+subLen));
                if(sum(arr, start, start+subLen) < 0){
                    count++;
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(getSubArraySum(arr));
    }
}
