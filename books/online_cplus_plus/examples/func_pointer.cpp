#include <iostream>
using namespace std;

int addition(int a, int b){return a+b;}
int minus_num(int a, int b){return a-b;};

int operation(int a, int b, int (*func_to_call)(int, int)){
	int g;
	g = (*func_to_call)(a, b);
	return g;
}

int main(){
	int (*subtraction)(int, int) = minus_num;
	int m = operation(5, 4, addition);
	int n = operation(20, m, subtraction);
	cout << n <<endl;
	return 0; 
}
