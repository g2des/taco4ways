import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class DequeCheck {
   public static void main(String[] args) {
       Scanner sc =  new Scanner(System.in);
       int n = sc.nextInt();
       int m = sc.nextInt();
       Deque<Integer> q = new ArrayDeque<>();
       Map<Integer, Integer> counter = new HashMap<>();
       int max = 0;
       for(int i=0;i<n;i++){
           updateQ(q, m, counter, sc.nextInt());
           
           if(max < counter.size()){
               max = counter.size();
           }
       }
       sc.close();
       System.out.println(max);
   }

   private static void updateQ(Deque<Integer> q, int m, Map<Integer, Integer> counter, int nextInt) {
       if(q.size() == m){
           decrementCounter(counter, q.pop());
       }
       q.add(nextInt);
       incrementCounter(counter, nextInt);
   }

   private static void incrementCounter(Map<Integer, Integer> counter, int nextInt) {
       int count = 1;
       if(counter.containsKey(nextInt)){
           count = counter.get(nextInt)+1;
       }
       counter.put(nextInt, count);
   }

   private static void decrementCounter(Map<Integer, Integer> counter, int pop) {
    //    Should never be called for key not in the counter, hence skipping condition check
    counter.put(pop, counter.get(pop)-1);
    if(counter.get(pop) == 0){
        counter.remove(pop);
    }
   }

}
