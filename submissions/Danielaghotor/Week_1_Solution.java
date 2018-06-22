public class FizzBuzzMain {
	public static void main(String[] args) {
		
		for ( int fb=1; fb<=100; fb++) {
			if ((fb%3==0) && (fb%5==0)) {
				System.out.println("FizzBuzz");
			}
			else if (fb%3==0) {
				System.out.println("Fizz");
			}
			else if (fb%5==0) {
				System.out.println("Buzz");
			}
		else
			System.out.println(fb);	
		}
	}
}
