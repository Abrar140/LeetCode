// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
    int [] arr={1,2,3,4,5,6};
    
    int max=arr[0];
    
    for(int num:arr){
        if(num>max){
            max=num;
        }
    }
    System.out.println(max);
    
    
        
    }
}