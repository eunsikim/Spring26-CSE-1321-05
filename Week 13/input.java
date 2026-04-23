import java.util.Scanner;

public class input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        // Flush the buffer, get rid of all trailing \n
        sc.nextLine();

        System.out.print("What class are you taking: ");
        String course = sc.nextLine();

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);
        System.out.println("You are taking " + course);
    }
}
