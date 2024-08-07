/*
You are given a floor of size 5xN. You have tiles of 2 different sizes: 1x5 and 2x5. Of course, you can rotate the tiles to get 2 more tile sizes: 5x1 and 5x2. You have to do the flooring using these tiles in the following way:
1. Floor space should be completely covered by tiles.
2. You cannot break tiles, ie, you have to use a tile entirely or not at all.
3. Any tile should not extend beyond the floor space.
4. Tiles should be placed parallel to the floor boundaries.

Your task is to find the number of ways in which you can lay the tiles on the floor.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains N - the length of the floor. The width of the floor is fixed to be 5.

Constraints

1 <= T <= 10000
1 <= N <= 106

Output Format

For each test case, print the number of ways in which you can lay the tiles on the floor, separated by new line. Since the output can be very large, print result % 1000000007 [1e9+7].

Sample Input 0

5
2
4
20
120
10
Sample Output 0

2
5
466098
562804719
457
Explanation 0

Self Explanatory

  */

dp = [0]*1000001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

k = 1000000007

for i in range(5, 1000001) :
    dp[i] = (dp[i-1] + dp[i-2] + (dp[i-5] * 8)) % k

for _ in range(int(input())) :
    print(dp[int(input())])
