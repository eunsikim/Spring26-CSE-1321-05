import java.util.ArrayList;

public class array_list {
    public static void main(String[] args) {
        // With ArrayLists we cannot use primitive data types
        // instead, we have to use wrapper classes:
        // Example:
        // - Integer for int
        // - Character for char
        // - Double for double
        ArrayList<Integer> my_int_arrList = new ArrayList<>();

        my_int_arrList.add(10);
        my_int_arrList.add(100);

        System.out.println(my_int_arrList.get(0));
        
        my_int_arrList.set(0, 20);

        System.out.println(my_int_arrList.get(0));
        
        my_int_arrList.remove(0);

        System.out.println(my_int_arrList.get(0));
    }
}
