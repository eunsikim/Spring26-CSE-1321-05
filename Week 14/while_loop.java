import java.util.Scanner;

public class while_loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a value or -1 to stop: ");
        int choice = Integer.parseInt(sc.nextLine());

        while(choice != -1){
            System.out.println("[LOOP]");
            System.out.print("Enter a value or -1 to stop: ");
            choice = Integer.parseInt(sc.nextLine());
        }

        System.out.println("Program terminated");
    }
}