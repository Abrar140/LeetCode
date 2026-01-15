class Solution {
    public boolean strongPasswordCheckerII(String password) {
        if (password.length() < 8) {
            return false;
        }

        boolean isDigit = false;
        boolean isLower = false;
        boolean isUpper = false;
        boolean isSpecial = false;

        String specialChars = "!@#$%^&*()-+";

        for (int i = 0; i < password.length(); i++) {
            char p = password.charAt(i);

            if (i > 0 && p == password.charAt(i - 1)) {
                return false;
            }

            if (Character.isDigit(p)) {
                isDigit = true;
            } else if (Character.isLowerCase(p)) {
                isLower = true;
            } else if (Character.isUpperCase(p)) {
                isUpper = true;
            } else if (specialChars.indexOf(p) != -1) {
                isSpecial = true;
            }
        }

        return isDigit && isLower && isUpper && isSpecial;
    }
}
