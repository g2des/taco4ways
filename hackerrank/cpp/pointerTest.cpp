#include <iostream>

using namespace std;

void update (int *a, int *b){
	int temp, temp2;
	temp = *a + *b;
	temp2 = abs( *a - *b);
	*a = temp;
	*b = temp2;
}

int main(){
	int a, b;
	int *pa = &a, *pb = &b;
	cin >> a >> 	b;
	update(pa, pb);
	printf("%d\n%d\n",a, b);
	return 0;
}
