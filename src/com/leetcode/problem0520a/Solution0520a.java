package com.leetcode.problem0520a;

import java.util.*;

public class Solution0520a {
        public int[] relativeSortArray(int[] arr1, int[] arr2) {
            Map<Integer,Integer> map = new HashMap<>();
            int[] ans = new int[arr1.length];
            for(int i=0;i<arr1.length;i++){
                map.put(arr1[i],map.getOrDefault(arr1[i],0)+1);
            }
            int t=0;
            for(int i=0;i<arr2.length;i++){
                if(map.containsKey(arr2[i])){
                    int cnt=map.get(arr2[i]);
                    while(cnt>0){
                        ans[t++] = arr2[i];
                        cnt--;
                    }
                    map.remove(arr2[i]);
                }
            }
            List<Integer> list = new ArrayList<>();
            for(int k : map.keySet()){
                int cnt=map.get(k);
                while(cnt>0){
                    list.add(k);
                    cnt--;
                }
            }
            Collections.sort(list);
            for(int val : list){
                ans[t++]=val;
            }
            return ans;
        }
}
