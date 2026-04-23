public class arithmetic_operators {
    public static void main(String[] args) {
        // For Every operator, if both operands are integer, the 
        // the resulting value will be an integer.
        // If one or both operands are double, the resulting value
        // will be a double.
        int int_num_1 = 4;
        int int_num_2 = 3;
        double db_num1 = 4.0;
        double db_num2 = 3.0;

        // Integer operations
        System.out.println(int_num_1 + int_num_2);
        System.out.println(int_num_1 - int_num_2);
        System.out.println(int_num_1 * int_num_2);
        // Integer Division: Both operands are integers
        System.out.println(int_num_1 / int_num_2);
        System.out.println(int_num_1 % int_num_2);

        System.out.println();

        // Intger/Double operations
        System.out.println(int_num_1 + db_num2);
        System.out.println(int_num_1 - db_num2);
        System.out.println(int_num_1 * db_num2);
        System.out.println(int_num_1 / db_num2);
        System.out.println(int_num_1 % db_num2);

        System.out.println();

        // Double operations
        System.out.println(db_num1 + db_num2);
        System.out.println(db_num1 - db_num2);
        System.out.println(db_num1 * db_num2);
        System.out.println(db_num1 / db_num2);
        System.out.println(db_num1 % db_num2);
    }
}
