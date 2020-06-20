package com.leetcode.problem0520c;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution0520c {

        public String mostCommonWord(String paragraph, String[] banned) {
            Set<String> set = new HashSet<>();
            Map<String,Integer> map = new HashMap<>();
            for(String word : banned) set.add(word);
            String temp ="";
            int cnt=0;
            for(char c : paragraph.toCharArray()){
                if(cnt==paragraph.length()-1){
                    if(Character.isLetter(c)){
                        temp += c+"";
                    }
                    temp = temp.toLowerCase();
                    if(!set.contains(temp)){
                        map.put(temp,map.getOrDefault(temp,0)+1);
                    }
                    temp="";
                }
                else {
                    if (Character.isLetter(c)) {
                        temp += c + "";
                    } else {
                        temp = temp.toLowerCase();
                        if (!set.contains(temp)) {
                            map.put(temp, map.getOrDefault(temp, 0) + 1);
                        }
                        temp = "";
                    }
                }
                cnt++;

            }
            int max=0;
            String maxStr="";
            for(String k : map.keySet()){
                if(max<map.get(k)){
                    max=map.get(k);
                    maxStr = k;
                }
            }
            return maxStr;
        }

}
