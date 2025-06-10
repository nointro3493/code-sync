class Solution {
    public int removeDuplicates(int[] nums) {
        int[] newArr = new int[nums.length - 1];
        int unique_count = 0;

        if(nums.length == 0){
            return 0;
        }
        int j = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i - 1]){
            nums[j] = nums[i];
            j++;
            }
        }

        return j;
        
    }
}