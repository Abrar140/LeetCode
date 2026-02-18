        String str = "aabbc";
        Map<Character, Integer> map = new HashMap<>();

        for(char c : str.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }