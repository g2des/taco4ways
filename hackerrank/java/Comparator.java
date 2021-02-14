import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Checker implements Comparator<Player>{
    public int compare(Player one, Player two){
        if(one.score == two.score){
            return one.name.compareTo(two.name);
        }else{
            return two.score-one.score;
        }
    }
}
class Player{
    String name;
    int score;
    Player(String name, int score){
        this.name = name;
        this.score = score;
    }
}
public class Comparator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Player[] players = new Player[n];
        Checker checker = new Checker();
        for(int i=0;i<n;i++){
            players[i] = new Player(sc.next(), sc.nextInt());
        }
        sc.close();
        Arrays.sort(players, checker);
        for(Player player: players){
            System.out.printf("%s %d\n",player.name, player.score);
        }

    } 

}
