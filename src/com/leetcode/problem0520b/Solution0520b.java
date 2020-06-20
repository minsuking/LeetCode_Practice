package com.leetcode.problem0520b;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution0520b {

        public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
            Map<Integer,Integer> map = new HashMap<>();
            List<List<Integer>> result = new ArrayList<>();
            int val=999999999;
            int valNum=0;
            int f=0;
            int cnt=0;
            for(List list : connections){
                for(int i=0;i<2;i++){
                    int value=(int)list.get(i);
                    map.put(value,map.getOrDefault(value,0)+1);

                }

            }
            for(List list : connections){
                for(int i=0;i<2;i++) {
                    int value = (int) list.get(i);
                    if (val > map.get(value)) {
                        val = map.get(value);
                        valNum = value;
                    }
                }
            }
            for(List list : connections) {
                for (int i = 0; i < 2; i++) {
                    int value = (int) list.get(i);
                    if(valNum == value){
                        result.add(list);
                    }
                }
            }
            return result;
        }

}
