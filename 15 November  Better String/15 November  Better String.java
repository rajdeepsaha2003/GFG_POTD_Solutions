
// User function Template for Java

class Solution {

    
    public static String betterString(String str1, String str2) {
        
        int a = countSub(str1);
        int b = countSub(str2);
        
  
        if (a < b) {
            return str2;
        }
        return str1;
    }
    
  
    static int countSub(String str) {
      
        int[] last = new int[256];
        Arrays.fill(last, -1);
        
    
        int n = str.length();
        int[] dp = new int[n + 1];

        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
          
            dp[i] = 2 * dp[i - 1];

            if (last[str.charAt(i - 1)] != -1) {
                dp[i] = dp[i] - dp[last[str.charAt(i - 1)]];
            }
            last[str.charAt(i - 1)] = (i - 1);
        }
        return dp[n];
    }
}