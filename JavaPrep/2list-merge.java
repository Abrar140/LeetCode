// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[] arr1= {1,2,5,9};
        int[] arr2= {3,4};
        int[] result=new int[arr1.length+arr2.length];
        
        for(int i=0; i<arr1.length;i++){
            result[i]=arr1[i];
        }
         for(int i=0; i<arr2.length;i++){
            result[i+arr1.length]=arr2[i];
        }
        
        
        for(int num:result){
        System.out.println(num);
        }
        
        
        
    }
}