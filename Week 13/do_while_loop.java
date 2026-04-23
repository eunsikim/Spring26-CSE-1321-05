import java.util.Scanner;

public class do_while_loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int choice = 0;

        do{
            System.out.println("[LOOP]");
            System.out.print("Enter a value or -1 to stop: ");
            choice = Integer.parseInt(sc.nextLine());
        }
        while(choice != -1);

        System.out.println("Program terminated");
    }
}