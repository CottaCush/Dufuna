public class Fizzbuzz {    
    public static void main(String[] args) {
        // TODO code application logic here
        int endcount=100; //end of my counter
        for (int i=1;i<=endcount;i++){ //initialized a for loop to count from 1 - 100
            
            if ((i % 3)==0 && (i % 5)==0){ // condition for fizzbuzz
                System.out.println ("FizzBuzz" );
            } 
            else if ((i % 3)==0){ //condition fizz
                System.out.println ("Fizz" );
            } 
            else if ((i % 5)==0){ // condition for buzz
                System.out.println ("Buzz" );
            } 
            else{
            System.out.println ( i ); //print the number if it does not satisfy the fizz,buzz or fizzbuzz condition
            }
        }
    }
    
}