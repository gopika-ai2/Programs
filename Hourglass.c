#include <stdio.h>

int main() {
    int n = 5;

    // Outer loop to iterate through each row
    for (int i = 0; i < 2 * n - 1; i++) {
      
        // Determine the row level relative to the center
        int l = (i < n) ? i : 2 * n - 2 - i;

        // Print leading spaces
        for (int j = 0; j < l; j++) {
            printf(" ");
        }

        // Print stars in the current row
        for (int k = 0; k < 2 * (n - l) - 1; k++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
