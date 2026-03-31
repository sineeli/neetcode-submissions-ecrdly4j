class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_dict;
        for (int i = 0; i < nums.size(); i++) {
            if (nums_dict.find(target - nums[i]) != nums_dict.end()) {
                return {nums_dict[target - nums[i]], i};
            }
            nums_dict[nums[i]] = i;
        }
        return {};
    }
};
