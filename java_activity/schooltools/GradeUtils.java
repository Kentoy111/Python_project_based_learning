package schooltools;

public class GradeUtils {
    public static double computeAverage(double prelim, double midterm, double finals) {
        return (prelim + midterm + finals) / 3.0;
    }
}