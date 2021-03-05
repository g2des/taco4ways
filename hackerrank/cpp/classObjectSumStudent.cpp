#include <cmath>
#include <iostream>
using namespace std;

class Student{
	private:
		int scores[5];
	public:
		void input(){
			for(int i=0;i<5;i++){
				cin >> scores[i];
			}
		}
		int calculateTotalScore(){
			int sum = 0;
			for(int i=0;i<5;i++){
				sum += scores[i];
			}
			return sum;
		}
};

int main(){
	int n;
	cin >> n;
	Student students[n];
	for(int i=0;i<n;i++){
		students[i].input();
	}
	int kris_score = students[0].calculateTotalScore();
	int count = 0;
	for (int i=1; i < n;i++){
		int temp_sum = students[i].calculateTotalScore();
		if(temp_sum > kris_score){
			count++;
		}
	}
	cout << count;
	return 0;
}

