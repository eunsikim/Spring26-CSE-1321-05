public class array_example_2 {
    public static int[] double_array_size(int[] original_array){
        int[] larger_array = new int[original_array.length * 2];

        for(int i = 0; i < original_array.length; i++){
            larger_array[i] = original_array[i];
        }

        return larger_array;
    }
    public static void main(String[] args) {
        System.out.println("Initializing `numbers` array:");
        int[] numbers = new int[10];
        System.out.println();

        int value = 10;
        System.out.println("Adding values into `numbers`");
        for(int i = 0; i < numbers.length; i++){
            numbers[i] = value;
            value += 10;
        }
        System.out.println();

        System.out.println("Printing `numbers`");
        for(int n : numbers){
            System.out.println(n);
        }
        System.out.println();

        System.out.println("Doubling `numbers`");
        numbers = double_array_size(numbers);
        System.out.println();

        System.out.println("Printing `numbers`");
        for(int n : numbers){
            System.out.println(n);
        }
    }
}
