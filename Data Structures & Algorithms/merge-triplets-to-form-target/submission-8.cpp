class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool x = false, y = false, z = false;
        
        for (auto t: triplets) {
            x = x || ((t[0] == target[0]) && (t[1] <= target[1]) && (t[2] <= target[2]));
            y = y || ((t[0] <= target[0]) && (t[1] == target[1]) && (t[2] <= target[2]));
            z = z || ((t[0] <= target[0]) && (t[1] <= target[1]) && (t[2] == target[2]));
        }
        return ( x && y && z);
    }
};
