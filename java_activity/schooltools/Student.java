package schooltools;

public class Student {
    private String name;
    private String course;
    
    public Student(String name, String course) {
        this.name = name;
        this.course = course;
    }
    
    public String introduce() {
        return "My name is " + name + " and I am taking " + course + ".";
    }
}
/home/kentbarneso/Documents/VSCODE/java_activity/schooltools/Student.java