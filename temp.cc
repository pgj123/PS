#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
bool compare(pair<int, int> p1, pair<int, int> p2){
    if((float)p1.second/p1.first == (float)p2.second/p2.first) return p1.first < p2.first;
    return (float)p1.second/p1.first > (float)p2.second/p2.first;
}
int main(){
    int c, n;
    scanf("%d %d", &c, &n);
    vector<pair<int, int>> v, v2;
    int t1, t2;
    for(int i = 0; i < n; i++){
        scanf("%d %d", &t1, &t2);
        v.push_back({t1, t2});
    }
    sort(v.begin(), v.end(), compare);
    
    int total_person = c;
    int total_cost = 0;
    pair<int, int> p;
    int first_choice, second_choice, final_choice;

    for(int i = 0 ; i < n; i++){
        printf("%d %d\n", v[i].first, v[i].second);
    }
    for(int i = 0 ; i < n; i++){ // v.first : 비용 , v.second : 사람
        p = v[i];
        first_choice = total_person / p.second;
        total_person -= first_choice * p.second;
        total_cost += first_choice * p.first; // 여기까지 확실
        v2.push_back(p);
        else{
            if(!v2.empty()){
                first_choice = 
                for(int i = 0 ; i < v2.size() ; i++){

                }
            }
        }
    }
    printf("%d", total_cost);
}