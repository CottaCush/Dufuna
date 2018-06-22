#include <iostream>
using namespace std;
int main( )
{
	int i = 1;
	int n = 100;
	for (i; i <= n; i++)
	{
		int k = i % 3;
		int j = i % 5;
		if (k == 0 && j == 0)
		{
			cout << "FIZZBUZZ" << endl;
		}
		
		else if (k == 0)
		{
			cout << "FIZZ" << endl;
		}
		else if (j == 0)
		{
			cout << "BUZZ" << endl;
		}
		else
		{
			cout << i << endl;
		}
	}
	return 0;
}
