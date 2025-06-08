class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char currentChar;
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        for(int i  = 0; i < s.length(); i++){
             currentChar = s.charAt(i);
            if (map.containsKey(currentChar)) {
               
            // currentChar is closing bracket
               
                if(!(s.contains(")") || s.contains("]") || s.contains("}"))){
                    return false;
                }

                 else if (stack.isEmpty() || stack.peek() != map.get(currentChar)) {
                    return false;  // mismatch or no opening bracket
                }

                else {stack.pop();}
            }

            else if(s.length() == 1) {
            return false;
           
        }

            else{
                 stack.push(currentChar);

            }
        
    }

    return stack.isEmpty();
}
}