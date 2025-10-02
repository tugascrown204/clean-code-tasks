// Example Task - Factorial Calculation

public class Factorial {
    public static int factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Input should be a non-negative integer.");
        }
        return (n == 0) ? 1 : n * factorial(n - 1);
    }

    public static void main(String[] args) {
        try {
            int number = Integer.parseInt(args[0]);
            System.out.println("Factorial of " + number + " is: " + factorial(number));
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Please provide a non-negative integer as an argument.");
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
        }
    }
}
