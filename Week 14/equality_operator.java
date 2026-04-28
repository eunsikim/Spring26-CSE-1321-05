import java.util.Scanner;

public class equality_operator {
    public static void main(String[] args) {
        // The == operator only works with primitive types
        // With primitive types you compare by the value
        System.out.println(4 == 3);
        System.out.println(4 == 4);

        // With objects (complex types) you have to use 
        // the .equals() function.
        // With complext types, == compare by the reference
        Scanner sc = new Scanner(System.in);

        String s1 = "Hello";
        String s2 = sc.nextLine();
        
        System.out.println(s2.equals(s1));
    }
}
