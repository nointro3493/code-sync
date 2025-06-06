class Solution {
    public int reverse(int x) {
        String str_int = String.valueOf(x);
        String reverse = "";
        if (str_int.charAt(0) == '-') {
            reverse = "-";
            for (int i = str_int.length() - 1; i > 0; i--) {
                reverse = reverse + str_int.charAt(i);
            }
        }

        else {
            for (int i = str_int.length() - 1; i >= 0; i--) {
                reverse = reverse + str_int.charAt(i);
            }

        }

        if (Long.parseLong(reverse) > Integer.MAX_VALUE || Long.parseLong(reverse) < Integer.MIN_VALUE) {
            // Out of int bounds — return an error, fallback value, or throw exception
            return 0; // or handle it as needed
        }

        else {

            return Integer.parseInt(reverse);
        }
    }
}