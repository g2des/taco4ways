#include<iostream>
using namespace std;

int main(){
    cout << "enter number of elements in the array : ";
    int len;
    cin >> len;
    int arr[len];
    cout << "array of size " << sizeof(arr)/sizeof(arr[0]) << " created" << endl;
    while (true)
    {
        cout << "1. Add all element\n2. Replace value at index\n3. delete value at index\n4. Exit" << endl;
        int option;
        cin >> option;
        switch (option)
        {
        case 1:
            for(int i=0; i< len;i++){
                cin >> arr[i];
            }
            break;
        case 2: 
            cout << "Enter value to replace and index to replace at " << endl;
            int index;
            cin >> index;
            cin >> arr[index];
            break;
        case 3:
            cout << "Enter index to delete " << endl;
            cin >> index;
            arr[index] = 0;
            break;
        case 4:  
        default:
            exit(0);
        }
        for(auto num: arr){
            cout << num << ", ";
        }
        cout << endl;
    }
    
}