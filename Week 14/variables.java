public class variables {
    public static void main(String[] args) {
        // Number values without decimal points
        // java will assume it is an integer
        int x = 10;
        // You can use casting between
        // primitive data types
        int y = (int)3.14;
        // Number values with decimal point
        // java will assume double
        double pi = 3.14;
        // To define a float value in code
        // You need to add an 'f' at the end.
        float e = 2.72f;
        boolean isTrue = true;
        boolean isFalse = false;

        // If you need to change a variable's
        // value, you do not need to define
        // its data type.
        x = 20;
        pi = 3.15;

        String phone_num = "1234567890";
        // We use special functions to convert a primitive
        // value into a String and vice-versa 
        int phone_num_int = Integer.parseInt(phone_num);
        String phone_num_2 = String.valueOf(phone_num_int);
    }
}
