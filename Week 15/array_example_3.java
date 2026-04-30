import java.util.Arrays;

public class array_example_3 {
    public static void main(String[] args) {
        int[] arr1 = {10, 20, 30};

        int[] arr2 = {10, 20, 30};
        
        System.out.println(arr1 == arr2);
        System.out.println(Arrays.equals(arr1, arr2));
    }
}
