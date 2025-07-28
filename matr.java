public class matr {
    public static void main(String[] args) {
        // Initializing a 3x3 matrix
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Printing the matrix
        for (int i = 0; i < matrix.length; i++) {          // for each row
            for (int j = 0; j < matrix[i].length; j++) {   // for each column
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(); // Move to next line after each row
        }
    }
}


