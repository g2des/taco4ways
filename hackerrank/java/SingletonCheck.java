import java.util.Scanner;

class Singleton{
    public String str;
    private static Singleton singleton = null;
    private Singleton(){
    }
    public static Singleton getSingleInstance(){
        if(singleton == null){
            singleton = new Singleton();
        }
        return singleton;
    }
}
public class SingletonCheck{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Singleton instance = Singleton.getSingleInstance();
        Singleton instance2 = Singleton.getSingleInstance();
        instance.str = sc.nextLine();
        System.out.printf("Hello I am a singleton! Let me say %s to you\n",instance2.str);
        sc.close();

    }
} 