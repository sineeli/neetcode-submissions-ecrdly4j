class Solution {
    vector<string> output;
    vector<string> dict_map = {
        "",    "",    "abc",  "def",  "ghi",
        "jkl", "mno", "pqrs", "tuv",  "wxyz"
    };

    void dfs(int idx, string &res, const string &digits){
        if (idx == (int)digits.size()){
            output.push_back(res);
            return;
        }
        int d = digits[idx] - '0';
        const string &letters = dict_map[d];
        for (char ch: letters){
            res.push_back(ch);
            dfs(idx + 1, res, digits);
            res.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        output.clear();
        if (digits.empty()) return output;

        string res;
        dfs(0, res, digits);
        return output;
    }
};
