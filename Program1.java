class GfG {

    // Function to print fibonacci series
    static void printFib(int n) {
        if (n < 1) {
            System.out.println("Invalid Number of terms");
            return;
        }

        // When number of terms is greater than 0
        int prev1 = 1;
        int prev2 = 0;

        System.out.print(prev2 + " ");

        // If n is 1, then we do not need to
        // proceed further
        if (n == 1)
            return;

        System.out.print(prev1 + " ");

        // Print 3rd number onwards using
        // the recursive formula
        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
            System.out.print(curr + " ");
        }
    }

    // Driver code
    public static void main(String[] args) {
        int n = 9;
        printFib(n);
    }
}
