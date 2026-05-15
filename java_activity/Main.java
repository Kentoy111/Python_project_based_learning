import java.util.Scanner;
import java.util.Random;
import java.time.LocalDateTime;
import schooltools.Student;
import schooltools.GradeUtils;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        
        System.out.print("Enter student name: ");
        String name = input.nextLine();
        System.out.print("Enter course: ");
        String course = input.nextLine();
        
        Student student = new Student(name, course);
        
        System.out.println("\n--- STUDENT REPORT ---");
        System.out.println(student.introduce());
        double average = GradeUtils.computeAverage(89, 91, 94);
        System.out.println("Final Grade: " + average);
        System.out.println("Random Student Number: " + (1000 + rand.nextInt(9000)));
        System.out.println("Date and Time: " + LocalDateTime.now());
        
        input.close();
    }
}