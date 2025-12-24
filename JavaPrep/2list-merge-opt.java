// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[] arr1= {1,2,5,9};
        int[] arr2= {3,4};
        int[] result=new int[arr1.length+arr2.length];
        
        System.arraycopy(arr1, 0, result, 0, arr1.length);
        System.arraycopy(arr2, 0, result, arr1.length, arr2.length);

        for(int num:result){
        System.out.println(num);
        }
    }
}