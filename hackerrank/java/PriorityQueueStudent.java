import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

class Student{
    private int id;
    private String name;
    private double cgpa;
    
    Student(int id, String name, double cgpa){
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID(){
        return this.id;
    }

    public String getName(){
        return this.name;
    }

    public double getCGPA(){
        return this.cgpa;
    }
}

class CheckStudent implements Comparator<Student>{
    public int compare(Student one, Student two){
        if(two.getCGPA() != one.getCGPA()){
            return (int) Math.signum(two.getCGPA() - one.getCGPA());
        }else if(!one.getName().equals(two.getName())){
            return one.getName().compareTo(two.getName());
        }else{
            return one.getID() - two.getID();
        }
    }
}

class Priorities{
    PriorityQueue<Student> q = new PriorityQueue<>(new CheckStudent());
    public List<Student> getStudents(List<String> events) {
        for(String e: events){
            String[] event = e.split(" ");
            switch(event[0]){
                case "ENTER":
                q.add(new Student(Integer.parseInt(event[3]), event[1], Double.parseDouble(event[2])));
                break;
                case "SERVED":
                q.poll();
            }
        }
        List<Student> returnList = new ArrayList<>();
        while(!q.isEmpty()){
            returnList.add(q.poll());
        }

        return returnList;
    }

}

public class PriorityQueueStudent {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}