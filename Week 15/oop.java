class Dog{
    // Attributes (initialized in the body of the class, not the constructor)
    private int age;
    private float weight;
    private String name;
    private String furColor;
    private String breed;
    private int id;
    public static int nextID = 1;

    // Constructors
    // Default Constructor:
    public Dog(){
        age = 2;
        weight = 100.5f;
        name = "Fable";
        furColor = "brown";
        breed = "mixed";
        id = nextID;

        System.out.println("A dog named " + name + " has been created with ID: " + id);
        nextID++;
    }
    public Dog(int age, float weight, String name, String furColor, String breed){
        // Any time there is ambiguity due to the name of the attribute and parameter
        // you can use the keyword `this.` to specify the member attribute.
        // `this.age` refers to the attribute age, not the parameter
        this.age = age;
        this.weight = weight;
        this.name = name;
        this.furColor = furColor;
        this.breed = breed;
        id = nextID;

        System.out.println("A dog named " + name + " has been created with ID: " + id);
        nextID++;
    }

    public void bark(){
        System.out.println("Woof! Woof!");
    }
    
    public void eat(float food_weight){
        weight += food_weight;
    }

    // Setter & Getter
    // Setter Function
    public void set_name(String name){
        this.name = name;
    }
    
    // Getter Function
    public String get_name(){
        return name;
    }
}

public class oop {
    public static void main(String[] args) {
        System.out.println("Dog's nextID: " + Dog.nextID);
        Dog d1 = new Dog();

        System.out.println("Dog's nextID: " + Dog.nextID);
        Dog d2 = new Dog(1, 200, "Quasar", "black", "Norwegian Lundehund");
        
        System.out.println("Dog's nextID: " + Dog.nextID);
        Dog d3 = new Dog();
        
        System.out.println("Dog's nextID: " + Dog.nextID);
        Dog d4 = new Dog();


        // Changing Names
        // System.out.println(d1.name);
        // System.out.println(d2.name);
        
        // d2.rename("Waffle");
        // System.out.println(d1.name);
        // System.out.println(d2.name);
        

    }
}
