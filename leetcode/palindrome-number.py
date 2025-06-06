class Solution {
    public boolean isPalindrome(int x) {
        String str_int = String.valueOf(x);
        String [] integer = str_int.split("");
        int j = integer.length - 1;
        int i = 0;
        while(i < j){
            if(integer[i].equals(integer[j])){
                i++;
                j--;
                continue;
                
                
            }

            else{
               return false;
            }

            
            }
            
            return true;
    

}

}