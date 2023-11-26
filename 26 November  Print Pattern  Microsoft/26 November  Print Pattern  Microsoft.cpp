class Solution{
public:
    vector<int> pattern(int N){
        
        vector<int>ans;
        int i=N;
        while(N>0){
            ans.push_back(N);
            N-=5;
        }
        N=N-5;
        while(N<i){
            N+=5;
            ans.push_back(N);
        }
        return ans;
    }
};