public class array_example {
    public static void main(String[] args) {
        // Initializing an integer array called my_int_array
        // of size 10.
        int[] my_int_array = new int[10];

        String[] my_str_array = {"Hello", "World", "!"};

        // Once you initialize an array size, it cannot be changed
        // Instead, you can copy the values into a larger array:
        int[] larger_int_array = new int[my_int_array.length * 2];

        // Transfer the values from my_int_array into larger_int_array
        for(int i = 0; i < my_int_array.length; i++){
            larger_int_array[i] = my_int_array[i];
        }

        // (Optionally) We can assign the larger array to my_int_array:
        my_int_array = larger_int_array;




        //Basic Operations:
        // Adding values
        my_int_array[0] = 100;
        System.out.println(my_int_array[0]);
        // Modifying values:
        my_int_array[0] = 200;
        // Print/Access
        System.out.println(my_int_array[0]);
        // Remove: We cannot remove values, instead
        // we shift the indexes to make it look the we
        // removed a value in an array.

        System.out.println("`numbers` array:");
        int[] numbers = new int[10];

        int value = 10;
        System.out.println("Adding values into `numbers`");
        for(int i = 0; i < numbers.length; i++){
            numbers[i] = value;
            value += 10;
        }

        for(int n : numbers){
            System.out.println(n);
        }
    }
}
