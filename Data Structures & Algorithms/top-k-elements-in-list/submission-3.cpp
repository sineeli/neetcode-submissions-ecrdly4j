class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> nums_count;
        vector<vector<int>> buckets(nums.size() + 1);

        // Count frequency
        for (int num : nums) {
            nums_count[num]++;
        }

        // Put numbers into buckets by frequency
        for (auto& [num, freq] : nums_count) {
            buckets[freq].push_back(num);
        }

        // Collect top k frequent elements
        vector<int> res;
        for (int i = buckets.size() - 1; i >= 0; i--) {
            for (int num : buckets[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
