//fizzbuzz program by David Idajili
#include<iostream>
using namespace std;
int main(){
       //loop to iterate from 1 to 100
	for(int i = 1; i<=100; i++){
		
		if((i%3 == 0)&&(i%5 == 0))           //check if i is both a multiple of 3 and 5
			cout<<"FizzBuzz"<<"\n";     //print FizzBuzz 

		else if(i%3 == 0)                    //check if i is a multiple of 3
			cout<<"Fizz"<<"\n";         //print Fizz 

		else if(i%5 == 0)                    //check if i is a multiple of 5
			cout<<"Buzz"<<"\n";         //print Buzz

		else                                 
			cout<<i<<"\n";              //print i

	}
	return 0;
}
