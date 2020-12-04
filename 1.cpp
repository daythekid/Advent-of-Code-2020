//PART 1
// #include <bits/stdc++.h>

// using namespace std;

// int main(){
//     vector<int> arr;
//     int x;
//     while (cin>>x){
//         if (x==-1){
//             break;
//         }
//         arr.push_back(x);
//     }

//     for (int j=0;j<arr.size();j++){
//         if (find(arr.begin(),arr.end(),2020-arr[j])!=arr.end()){
//             cout<<arr[j]<<"  "<<2020-arr[j]<<endl;
//         }
//     }
// }

//PART 2
#include <bits/stdc++.h>

using namespace std;

vector<int> arr;

bool isSubset(int left_nums,int sum_left,int curr_pos,vector<int> coll){
    if (curr_pos>arr.size()){
        return false;
    }
    if (left_nums==0&&sum_left!=0){
        return false;
    }

    if (left_nums==0&&sum_left==0){
        for (auto j:coll){
            cout<<arr[j]<<endl;
        }
        return true;
    }
    vector<int> things = coll;
    things.push_back(curr_pos);
    if (isSubset(left_nums-1,sum_left-arr[curr_pos],curr_pos+1,things)||isSubset(left_nums,sum_left,curr_pos+1,coll)){
        return true;
    }
    return false;
}

int main(){
    int x;
    while (cin>>x){
        if (x==-1){
            break;
        }
        arr.push_back(x);
    }
    sort(arr.begin(),arr.end());

    vector<int> empty = {};
    isSubset(3,2020,0,empty);
    
}
