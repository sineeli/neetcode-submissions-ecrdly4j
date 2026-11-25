public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sdict = new Dictionary<char, int>();
        Dictionary<char, int> tdict = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++) {
            if (!sdict.ContainsKey(s[i])) {
                sdict[s[i]] = 1;
            } else {
                sdict[s[i]] += 1;
            }
        }

        for (int j = 0; j < t.Length; j++) {
            if (!tdict.ContainsKey(t[j])) {
                tdict[t[j]] = 1;
            } else {
                tdict[t[j]] += 1;
            }
        }

        Dictionary<char, int> largerDictionary = new Dictionary<char, int>();
        Dictionary<char, int> smallDictionary = new Dictionary<char, int>();

        if (sdict.Count >= tdict.Count) {
            largerDictionary = sdict;
            smallDictionary = tdict;
        } else {
            largerDictionary = tdict;
            smallDictionary = sdict;
        }

        foreach (var kvp in largerDictionary) {
            if (!smallDictionary.TryGetValue(kvp.Key, out int defaultV)) {
                return false;
            } else {
                if (kvp.Value != smallDictionary[kvp.Key]) {
                    return false;
                }
            }
        }

        return true;
    }
}
