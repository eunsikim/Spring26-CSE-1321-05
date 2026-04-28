import java.util.Scanner;
// If you do not want to deal with flushing the buffer
// You can treat every input as a String and convert it
// if necessary
public class input_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = Integer.parseInt(sc.nextLine()); // int(input("Enter your age: "))

        System.out.print("What class are you taking: ");
        String course = sc.nextLine();

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);
        System.out.println("You are taking " + course);
    }
    
}
