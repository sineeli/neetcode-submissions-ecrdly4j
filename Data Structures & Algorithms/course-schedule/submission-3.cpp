class Solution {
    unordered_map<int, vector<int>> graph;
    vector<int> state; // 0=unvisited, 1=visiting, 2=done

    bool dfs(int node) {
        if (state[node] == 1) return false; // cycle
        if (state[node] == 2) return true;  // already processed

        state[node] = 1; // mark visiting

        auto it = graph.find(node);
        if (it != graph.end()) {
            for (int nei : it->second) {
                if (!dfs(nei)) return false;
            }
        }

        state[node] = 2; // mark done
        return true;
    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.clear();
        state.assign(numCourses, 0);

        for (auto &p : prerequisites) {
            int course = p[0], pre = p[1];
            graph[pre].push_back(course);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) return false;
        }
        return true;
    }
};