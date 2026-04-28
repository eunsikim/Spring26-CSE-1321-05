public class for__each_loop {
    public static void main(String[] args) {
        // Just assume the line below is a list
        int[] my_numbers = {10, 11, 23};

        // FOR EACH loop
        for(int i : my_numbers){ // == for i in my_numbers: ...
            System.out.println(i);
        }
    }
}
