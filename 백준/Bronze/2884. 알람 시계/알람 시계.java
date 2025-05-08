import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        int A = H*60 + M;
        int B = A - 45;
        if (B < 0) {
            B += 24 * 60;
        }

        System.out.println(B/60 + " " + B%60);
    }
}