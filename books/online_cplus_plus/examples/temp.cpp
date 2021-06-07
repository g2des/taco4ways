#include <iostream>
#include <array>
#include <string>
#include <typeinfo>

using namespace std;

int main(){
	int num1, num2;
	int *num_ptr;
	num_ptr = &num1;
	*num_ptr = 10;
	num_ptr = &num2;
	*num_ptr = 20;
	cout << "Num1 points to : " << num1 << endl;
	cout << "Num2 points to : " << num2 << endl;
	const char * hello_ptr = "Hello world";
	cout << *hello_ptr << endl;
	// cout << *(string *)hello_ptr << endl;
	cout << "\n\nPointer to pointer" << endl;
	char c = 'z';
	char * c_ptr;
	c_ptr = &c;
	char **c_ptr_pth;
	c_ptr_pth = &c_ptr;
	cout << "Char " << c << endl;
	cout << "Char Pointer " << (void *) c_ptr << endl;
	cout << "Char Pointer to Pointer " << (void *)c_ptr_pth << endl;
}
