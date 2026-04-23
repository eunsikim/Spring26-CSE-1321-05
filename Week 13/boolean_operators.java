public class boolean_operators {
    public static void main(String[] args) {
        int num_1 = 4;
        int num_2 = 3;

        // We have the same characters
        // for boolean comparison ops.
        // as in Python
        System.out.println(num_1 > num_2);
        System.out.println(num_1 >= num_2);
        System.out.println(num_1 < num_2);
        System.out.println(num_1 <= num_2);
        System.out.println(num_1 == num_2);
        System.out.println(num_1 != num_2);

        // We do not have in, not in, is, is not operators in java.
        System.out.println();
        // Logical Operators
        // AND operator => &&
        System.out.println(true && true);
        System.out.println(true && false);
        // OR operator => ||
        System.out.println(true || true);
        System.out.println(true || false);
        // NOT operator => !
        System.out.println(!(num_1 != num_2));
    }
}
