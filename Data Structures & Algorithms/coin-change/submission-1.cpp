class Solution {
int output;
vector<int> memo; // memo[sum] = min coins used to reach sum

void backtrack(int &coin_sum, int &num_coins, const vector<int> &coins, int target){
    if (coin_sum == target){
        output = min(num_coins, output);
        return;
    }
    if (coin_sum > target) return;
    if (num_coins >= output) return;
    if (memo[coin_sum] != -1 && memo[coin_sum] <= num_coins)
            return;
    memo[coin_sum] = num_coins;
    for (auto coin: coins){
        coin_sum += coin;
        num_coins++;
        backtrack(coin_sum, num_coins, coins, target);
        coin_sum -= coin;
        num_coins--;
    }
}


public:
    int coinChange(vector<int>& coins, int amount) {
        output = INT_MAX;
        memo.assign(amount + 1, -1);
        int coin_sum = 0, num_coins = 0;
        backtrack(coin_sum, num_coins, coins, amount);

        return (output == INT_MAX) ? -1 : output;
    }
};
