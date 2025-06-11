class Solution {
    public int removeElement(int[] nums, int val) {
        int not_val = 0;

        int j = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[j] = nums[i];
                j++;
                not_val++;
            }

            else{
                continue;
            }
        }
        return not_val;
    }
}