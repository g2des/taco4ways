import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;

public class StackParser {
    public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input=sc.next();
            Stack<Character> stack = new Stack<>();
            boolean shouldContinue = true;
            for(char c: input.toCharArray()){
                switch(c){
                    case '{':
                    case '(':
                    case '[': stack.add(c);break;
                    case '}': 
                    if(!stack.isEmpty() && stack.peek() == '{'){
                        stack.pop();
                    }else{
                        shouldContinue = false;
                    }
                    break;
                    case ')': 
                    if(!stack.isEmpty() && stack.peek() == '('){
                        stack.pop();
                    }else{
                        shouldContinue = false;
                    }
                    break;
                    case ']': 
                    if(!stack.isEmpty() && stack.peek() == '['){
                        stack.pop();
                    }else{
                        shouldContinue = false;
                    }
                    break;
                }
                if(!shouldContinue){
                    break;
                }
            }
            System.out.println(stack.isEmpty() && shouldContinue);
            //Complete the code
		}
        sc.close();
	}
}