#include <iostream>
#include <vector>

using namespace std;

int main(){
	int n, q;
	cin >> n >> q;
	vector<vector<int>> vec;
	for(int i=0;i<n;i++){
		int size;
		cin >> size;
		vector<int> temp;
		int num;
		for (int j=0;j<size;j++){
			cin >> num;
			temp.push_back(num);
		}
		vec.push_back(temp);
	}
	for(int i=0;i<q;i++){
		int q1, q2;
		cin >> q1 >> q2;
		printf("%d\n", vec[q1][q2]);
	}
	return 0;
}
