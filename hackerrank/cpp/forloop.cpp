#include <iostream>

using namespace std;

int main(){
	int i, j;
	cin >> i;
	cin >> j;
	for (int num=i;num<=j;num++){

	if (num > 9){
		if (num %2==0){
			printf("even\n");
		}else{
			printf("odd\n");
		}
	} else if(num == 1){
		printf("one\n");
	}else if (num == 2){
		printf("two\n");
	
	}else if (num == 3){
		printf("three\n");
	
	}else if (num == 4){
		printf("four\n");
	
	}else if (num == 5){
		printf("five\n");
	
	}else if (num == 6){
		printf("six\n");
	
	}else if (num == 7){
		printf("seven\n");
	
	}else if (num == 8){
		printf("eight\n");
	
	}else if (num == 9){
		printf("nine\n");
	}
	}
	return 0;
}
	
	
