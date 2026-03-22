// Last updated: 3/22/2026, 10:33:44 PM
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        
        // Start or end blocked
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;

        queue<pair<int,int>> q;
        q.push({0,0});
        grid[0][0] = 1; // mark visited
        
        int dist = 1;

        vector<pair<int,int>> dirs = {
            {-1,-1},{-1,0},{-1,1},
            {0,-1},        {0,1},
            {1,-1},{1,0},{1,1}
        };

        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                auto [r,c] = q.front();
                q.pop();

                if (r == n-1 && c == n-1) return dist;

                for (auto [dr, dc] : dirs) {
                    int nr = r + dr, nc = c + dc;

                    if (nr >= 0 && nc >= 0 && nr < n && nc < n && grid[nr][nc] == 0) {
                        q.push({nr, nc});
                        grid[nr][nc] = 1; // mark visited
                    }
                }
            }
            dist++;
        }

        return -1;
    }
};