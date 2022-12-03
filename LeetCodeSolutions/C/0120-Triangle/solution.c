/*

https://leetcode.com/submissions/detail/721639305/
Date of Submission: 2022-06-13

Runtime: 9 ms, faster than 65.83% of C online submissions for Triangle.
Memory Usage: 6.8 MB, less than 65.00% of C online submissions for Triangle.

*/

int min(int left, int right);

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    int currRow = 0;
    int lowestSum = 0;
    if (triangleSize == 1){
        return triangle[0][0];
    }
    else if (triangleSize == 2){
        return triangle[0][0] + min(triangle[1][0], triangle[1][1]);
    }

    while(currRow < triangleSize-1){
        currRow++;
        for(int i=1; i<currRow; i++){
            triangle[currRow][i] += min(triangle[currRow-1][i-1], triangle[currRow-1][i]);
        }
        triangle[currRow][0] += triangle[currRow-1][0];  // left edge case
        triangle[currRow][currRow] += triangle[currRow-1][currRow-1];  // right edge case
    }

    lowestSum = triangle[currRow][0];
    for (int i=1; i<currRow+1; i++){
        lowestSum = min(lowestSum,triangle[currRow][i]);
    }
    return lowestSum;
}

int min(int left, int right){
    if (left < right){
        return left;
    }

    return right;
}