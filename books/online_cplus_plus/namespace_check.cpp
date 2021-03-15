#include <iostream>
using namespace std;
namespace normal{
	const double pi = 3.14;
	double area(int r){
		return pi * r * r;
	} 
}

namespace morePrecision{
	const double pi = 3.1415;
	double area(int r){
		return pi  * r * r;
	}
}
int main(){
	//Method 1: Explicit declaration for all
	cout << "Method 1\n"; 
	cout << normal::area(10) << endl;
	cout << morePrecision::area(10) << endl;
	//Method 2: Declare one with `using`
	cout << "Method 2\n";
	using normal::area;
	cout << area(10) << endl;
	cout << morePrecision::area(10) << endl;
	cout << "Method 3\n";
	//Method 3: Each in ints block
	{
		using normal::area;
		cout << area(10) << endl;
	}
	{
		using morePrecision::area;
		cout << area(10) << endl;
	}
	// using the one from line 23
	cout << area(10) << endl;
	
}