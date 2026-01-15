class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer>  rom_int = new HashMap<>();
        rom_int.put('I', 1);
        rom_int.put('V', 5);
        rom_int.put('X', 10);
        rom_int.put('L', 50);
        rom_int.put('C', 100);
        rom_int.put('D', 500);
        rom_int.put('M', 1000);
        rom_int.put('Z', 0);
        int total = 0;
        int n = s.length();
        for(int i = 0; i<n; i++){
            char cur_char = s.charAt(i);
            char next_char = 'Z';
            if(i+1<n)
            {
            next_char = s.charAt(i+1);
            }
            int int_cur_char = rom_int.get(cur_char);
            int int_next_char= rom_int.get(next_char);

            if (int_cur_char<int_next_char){
                total -= int_cur_char;
            }
            else{
                total = total+int_cur_char;
            }
        
        }  
        return total;      
    }
}