public class for_loop {
    public static void main(String[] args) {
        // The regular FOR is great whenever we know 
        // how many iterations we want to work.

        // `int i = 0` happens before the loop
        //
        // `i < 10` is the condition, this for loop is a 
        // pre-iteration check (like a while loop)
        //
        // `i++` is what happens at the end of a single iteration
        for(int i = 0; i < 10; i++){ // i++ is similar to i += 1
            System.out.println("Hello World");
        }

        System.out.println();

        // This is just an example to showcase the order of operations
        // in a for loop
        for(int i = 0, j = 9; i < 10; i++, j--, System.out.println("Increasing i and decreasing j")){ // j-- is similar to j -= 1
            System.out.println("i: " + i + ", j: " + j);
        }
    }
}
