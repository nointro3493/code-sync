class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";

        String common_prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(common_prefix)) {
                common_prefix = common_prefix.substring(0, common_prefix.length() - 1);
                if (common_prefix.isEmpty()) return "";
            }
        }

        return common_prefix;
    }
}