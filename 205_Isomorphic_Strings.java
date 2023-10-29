205. Isomorphic Strings


Example 1:
Input: s = "egg", t = "add"
Output: true
  
Example 2:
Input: s = "foo", t = "bar"
Output: false
  
Example 3:
Input: s = "paper", t = "title"
Output: true


class Solution {
    public boolean isIsomorphic(String s, String t) {
    if (s.length() != t.length()) {
      return false;
    }
    // Create a hashmap to store character mappings
    Map<Character, Character> charMappingMap = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {

      char original = s.charAt(i);
      char replacement = t.charAt(i);

      if (!charMappingMap.containsKey(original)) {
        if (!charMappingMap.containsValue(replacement))
          charMappingMap.put(original, replacement);
        else
          return false;
      }
      else {
        char mappedCharacter = charMappingMap.get(original);
        if (mappedCharacter != replacement)
          return false;
      }
    }

    return true;
  }
}
