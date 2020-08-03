
#Dynamic Programming Approch of problem14, again my brain is to explode!!!

      #       0 1 2 3 ... sum
      # 0  3
      # 1  5
      # 2  6


def displayMatrix(matrix):
    for row in matrix:
        print(row)


def finSubsetwithsum(array,sum):

    n=len(array)

    matrix=[[False for x in range(sum+1)] for y in range(n)]

    for i in range(n):
        matrix[i][0]=True

    for j in range(1,sum+1):
        if array[0]==j:
            matrix[0][j]=True


    for i in range(1,n):
        for j in range(1,sum+1):
            if(matrix[i-1][j]==True):
                matrix[i][j]=True
            elif(j>array[i]):
                matrix[i][j]=matrix[i-1][j-array[i]] #Check the including solution

    displayMatrix(matrix)

array = [1,3,7,2,1,2]
print(finSubsetwithsum(array,15))



#I realized that this is not the way to solve thi :Here is the java implentatin from  https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
#Lets tackle this later. If you implement it, please try to post in that page, they don have python implementaion currently

# // A Java program to count all subsets with given sum.
# import java.util.ArrayList;
# public class SubSet_sum_problem
# {
# 	// dp[i][j] is going to store true if sum j is
# 	// possible with array elements from 0 to i.
# 	static boolean[][] dp;
#
# 	static void display(ArrayList<Integer> v)
# 	{
# 	System.out.println(v);
# 	}
#
# 	// A recursive function to print all subsets with the
# 	// help of dp[][]. Vector p[] stores current subset.
# 	static void printSubsetsRec(int arr[], int i, int sum,
# 										ArrayList<Integer> p)
# 	{
# 		// If we reached end and sum is non-zero. We print
# 		// p[] only if arr[0] is equal to sun OR dp[0][sum]
# 		// is true.
# 		if (i == 0 && sum != 0 && dp[0][sum])
# 		{
# 			p.add(arr[i]);
# 			display(p);
# 			p.clear();
# 			return;
# 		}
#
# 		// If sum becomes 0
# 		if (i == 0 && sum == 0)
# 		{
# 			display(p);
# 			p.clear();
# 			return;
# 		}
#
# 		// If given sum can be achieved after ignoring
# 		// current element.
# 		if (dp[i-1][sum])
# 		{
# 			// Create a new vector to store path
# 			ArrayList<Integer> b = new ArrayList<>();
# 			b.addAll(p);
# 			printSubsetsRec(arr, i-1, sum, b);
# 		}
#
# 		// If given sum can be achieved after considering
# 		// current element.
# 		if (sum >= arr[i] && dp[i-1][sum-arr[i]])
# 		{
# 			p.add(arr[i]);
# 			printSubsetsRec(arr, i-1, sum-arr[i], p);
# 		}
# 	}
#
# 	// Prints all subsets of arr[0..n-1] with sum 0.
# 	static void printAllSubsets(int arr[], int n, int sum)
# 	{
# 		if (n == 0 || sum < 0)
# 		return;
#
# 		// Sum 0 can always be achieved with 0 elements
# 		dp = new boolean[n][sum + 1];
# 		for (int i=0; i<n; ++i)
# 		{
# 			dp[i][0] = true;
# 		}
#
# 		// Sum arr[0] can be achieved with single element
# 		if (arr[0] <= sum)
# 		dp[0][arr[0]] = true;
#
# 		// Fill rest of the entries in dp[][]
# 		for (int i = 1; i < n; ++i)
# 			for (int j = 0; j < sum + 1; ++j)
# 				dp[i][j] = (arr[i] <= j) ? (dp[i-1][j] ||
# 										dp[i-1][j-arr[i]])
# 										: dp[i - 1][j];
# 		if (dp[n-1][sum] == false)
# 		{
# 			System.out.println("There are no subsets with" +
# 												" sum "+ sum);
# 			return;
# 		}
#
# 		// Now recursively traverse dp[][] to find all
# 		// paths from dp[n-1][sum]
# 		ArrayList<Integer> p = new ArrayList<>();
# 		printSubsetsRec(arr, n-1, sum, p);
# 	}
#
# 	//Driver Program to test above functions
# 	public static void main(String args[])
# 	{
# 		int arr[] = {1, 2, 3, 4, 5};
# 		int n = arr.length;
# 		int sum = 10;
# 		printAllSubsets(arr, n, sum);
# 	}
# }
# //This code is contributed by Sumit Ghosh







