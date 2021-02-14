#include <iostream>
using namespace std;

int main(){
	int limit;
	cin >> limit;
	int arr[limit];
	for (int i=0;i<limit;i++){
		cin >> arr[i];
	}
	for (int i = limit - 1;i >=0;i--){
		printf("%d ",arr[i]);
	}
	return 0;
}
