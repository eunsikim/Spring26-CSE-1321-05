public class overloaded_method {
    // Overloaded methods allows us to have multiple functions with
    // the same name. But, there are a couple of rules that you
    // have to meet:
    // 1. The names of the functions must be the same.
    // 2. The signature of each overloaded method must be unique.
    //    Signature: The data type of your parameter(s) and their position.

    // Signature: (int, int)
    public static int add(int num1, int num2){
        System.out.println("add(int, int)");
        return num1 + num2;
    }
    
    // Signature: (double, double)
    public static double add(double num1, double num2){
        System.out.println("add(double, double)");
        return num1 + num2;
    }

    public static int add(int num1, double num2){
        System.out.println("add(int, double)");
        return num1 + (int)num2;
    }

    public static void add(double num1, int num2){
        System.out.println("add(double, int)");
        System.out.println("ERROR!!");
    }
    
    // Translate this function header to java: `def add(num1, num2=10):`
    public static int add(int num1){
        System.out.println("add(int)");
        // return num1 + 10;
        return add(num1, 10);
    }

    // Here we are trying to create a print function
    // that works like in Python
    public static void print(String message){
        System.out.println(message);
    }
    public static void print(String message, String end){
        System.out.print(message + end);
    }

    public static void main(String[] args) {
        System.out.println(add(4, 3));
        System.out.println(add(4.5, 3.5));
        System.out.println(add(4, 3.5));
        add(3.5, 4);
        System.out.println(add(40));

        print("hello world");
        print("Hello World", ", ");
        print("Hello CSE 1321");
    }
}
