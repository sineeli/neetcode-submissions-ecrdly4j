class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int curr_max = nums[0];
        int curr_min = nums[0];
        int ans = nums[0];
        int temp = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                temp = curr_max;
                curr_max = curr_min;
                curr_min = temp;
            }
            curr_max = max(nums[i], nums[i] * curr_max);
            curr_min = min(nums[i], nums[i] * curr_min);
            ans = max(curr_max, ans);
        }
        return ans;
    }
};
