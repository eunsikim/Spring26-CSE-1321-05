import java.util.Scanner;

public class switch_statements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your order: ");
        String order = sc.nextLine();

        switch(order){
            case "burger":
                System.out.println("You've ordered a burger.");
                // If you dont add a break at the end of a case
                // It will pass through to the case below.
                break;
            case "fries":
                System.out.println("You've ordered fries.");
                break;
            case "drink":
                System.out.println("You've ordered a drink");
                break;
            default:
                System.out.println("We do not serve those.");
                break;
        }
    }
}