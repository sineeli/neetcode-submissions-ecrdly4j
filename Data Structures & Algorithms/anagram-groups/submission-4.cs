public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var newDict = new Dictionary<string, List<string>>();

        for (int i = 0; i < strs.Length; i++) {
            // 1. Sort the characters of the string to create a key
            char[] chars = strs[i].ToCharArray();
            Array.Sort(chars);
            string sortedKey = new string(chars);

            // 2. Check if the key exists; if not, initialize a new list
            if (!newDict.TryGetValue(sortedKey, out List<string> group)) {
                group = new List<string>();
                newDict.Add(sortedKey, group);
            }

            // 3. Add the original string to the list
            group.Add(strs[i]);
        }

        return new List<List<string>>(newDict.Values);
    }
}
