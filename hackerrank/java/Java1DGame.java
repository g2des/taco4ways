import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Java1DGame {
    public static boolean canWin(int leap, int[] game) {
        Stack<List<Integer>> stack = new Stack<>();
        List<Integer> start = new ArrayList<>();
        Map<Integer, List<Integer>> knownPath = new HashMap<>();
        start.add(0);
        stack.add(start);
        knownPath.put(0, start);
        while(!stack.isEmpty()){
            List<Integer> currentPath = stack.pop();
            int lastIndex = currentPath.get(currentPath.size()-1);
            int[] nextSteps = {lastIndex -1, lastIndex+1, lastIndex + leap};
            // declare victory if crossed the limit
            if(nextSteps[1]>=game.length|| nextSteps[2] >=game.length){
                return true;
            } 
            for(int nextStep: nextSteps){
                if(shouldAddToPath(nextStep, game, knownPath)){
                    List<Integer> newPath = new ArrayList<>(currentPath);
                    newPath.add(nextStep);
                    stack.add(newPath);
                    knownPath.put(nextStep, newPath);
                }
            }
            // System.out.println(stack);
        }
        return false;
    }

    private static boolean shouldAddToPath(int index, int[] game, Map<Integer, List<Integer>> knownPath) {
        return !(index<0 || knownPath.containsKey(index) || game[index] !=0);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}