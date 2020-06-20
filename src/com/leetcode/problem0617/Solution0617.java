package com.leetcode.problem0617;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution0617 {

    public int[][] mergeNumbers(int[][] nums){
        int[][] result = new int[nums.length][2];
        PriorityQueue<int[]> queue = new PriorityQueue<>();

        for(int i=0;i<nums.length;i++){
            queue.add(nums[i]);
        }
        int[] waitArray = queue.poll();
        int cnt=0;
        while(!queue.isEmpty()){

            int[] temp = queue.peek();
            int first = temp[0];
            int last = temp[1];
            if(waitArray[1]<first){
                result[cnt][0] = waitArray[0];
                result[cnt++][1] = waitArray[1];
                waitArray[0] = first;
                waitArray[1] = last;
            }else{
                if(!(waitArray[1] > last)){
                    result[cnt][0] = first;
                    result[cnt++][1] = last;
                }
                queue.poll();
            }


        }

        return result;
    }

}
