#include <iostream>
 using namespace std;
 int main()
//this programs prints numbers from 1 -100
/*when the number is mlultiple of 3 it prints fizz
when it is a multiple of 5 it prints buzz
and it is a multiple of 3 and 5 it prints fizzbuzz
*/
 {
 for(int i=1; i<101; i++)
 	{
 	if (i%3==0&i%5==0)            //uses the % operator to signify remainder
 	{
 			          cout<<"fizzbuzz";
 		
		 }
        else if(i%3==0)
		 	        {cout<<"fizz";
			 }
	 else if(i%5==0)
		 	             {cout<<"buzz";
			 }
	 else
        {
			 }          cout<<i<<endl;
	 }
          } 
