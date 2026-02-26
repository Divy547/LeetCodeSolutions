// Last updated: 2/26/2026, 3:48:33 PM
1class Solution {
2public:
3    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
4        int n = grid.size();
5        
6        // Start or end blocked
7        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
8
9        queue<pair<int,int>> q;
10        q.push({0,0});
11        grid[0][0] = 1; // mark visited
12        
13        int dist = 1;
14
15        vector<pair<int,int>> dirs = {
16            {-1,-1},{-1,0},{-1,1},
17            {0,-1},        {0,1},
18            {1,-1},{1,0},{1,1}
19        };
20
21        while (!q.empty()) {
22            int sz = q.size();
23            while (sz--) {
24                auto [r,c] = q.front();
25                q.pop();
26
27                if (r == n-1 && c == n-1) return dist;
28
29                for (auto [dr, dc] : dirs) {
30                    int nr = r + dr, nc = c + dc;
31
32                    if (nr >= 0 && nc >= 0 && nr < n && nc < n && grid[nr][nc] == 0) {
33                        q.push({nr, nc});
34                        grid[nr][nc] = 1; // mark visited
35                    }
36                }
37            }
38            dist++;
39        }
40
41        return -1;
42    }
43};