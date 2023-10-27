Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
  
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool firstRow = false;
        bool firstCol = false;

        // Set Markers in the frist row and col
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<matrix[0].size(); j++){
                if(matrix[i][j] == 0){
                    if(i == 0) firstRow = true;
                    if(j == 0) firstCol = true;
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Replace inner matrix
        for(int i = 1; i<matrix.size(); i++ ){
            for(int j = 1; j<matrix[0].size(); j++ ){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            } 
        }

        if(firstRow){
            for(int j = 0; j<matrix[0].size(); j++){
                matrix[0][j] = 0;
            }
        }
        if(firstCol){
            for(int i = 0; i<matrix.size(); i++){
                matrix[i][0] = 0;
            }
        }

    }
};
