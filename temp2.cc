#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    int t,k;
    scanf("%d", &t);
    for(int i = 0 ; i < t; i++){
        scanf("%d", &k);
        int file[k];
        vector <int> cost;

        for(int j = 0 ; j < k; j++){
            scanf("%d", &file[j]);
        }
        sort(file, file+k);
        int total_cost = 0;
        for(int j = 0 ; j < k-1; j++){
            if(cost.empty()){
                cost.push_back(file[j] + file[j+1]);
                total_cost += file[j] + file[j+1];
                j+=1;
            }
            else{
                bool need_new_inserted = true;
                int cost_size = cost.size();
                for(int h = 0; h < cost.size(); h++){
                    if(cost[h] <= file[j+1]){
                        cost[h] += file[j];
                        total_cost += file[j] + cost[h];
                        need_new_inserted = false;
                        break;
                    }
                }
                if(need_new_inserted){
                    cost.push_back(file[j] + file[j+1]);
                    total_cost += file[j] + file[j+1];
                }
                sort(cost.begin(), cost.end());
            }
        }
        for(int j = 0; j < cost.size(); j++){
            total_cost += cost[j];
            printf("%d\n", cost[j]);
        }
        printf("%d\n", total_cost);
    }
}