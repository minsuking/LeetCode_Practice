package com.leetcode;

import com.leetcode.problem0520a.Solution0520a;
import com.leetcode.problem0520b.Solution0520b;
import com.leetcode.problem0520c.Solution0520c;
import com.leetcode.problem0529a.Solution0529a;
import com.leetcode.problem1150.Solution1150;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
//        Solution0520a solution1150 = new Solution0520a();
//        int[] arr1={2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31};
//        int[] arr2 = {2,42,38,0,43,21};
//
//        int[] result = solution1150.relativeSortArray(arr1,arr2);
//        for(int i=0;i<result.length;i++){
//            System.out.print(result[i]+" ");
//        }

//        Solution0520b solution = new Solution0520b();
//        List<List<Integer>> setList = new ArrayList<>();
//        List<Integer> list = new ArrayList();
//
//
//        list.add(0);
//        list.add(1);
//        setList.add(list);
//        list = new ArrayList();
//        list.add(1);
//        list.add(2);
//        setList.add(list);
//        list = new ArrayList();
//
//        list.add(2);
//        list.add(0);
//        setList.add(list);
//        list = new ArrayList();
//
//        list.add(1);
//        list.add(3);
//        setList.add(list);
//
//        solution.criticalConnections(4,setList);
        //Solution0520c solution = new Solution0520c();
        //String[] banned = {"hit"};
        Solution0529a solution = new Solution0529a();
        int[][] image = {{1,1,1},{1,1,0},{1,0,1}};
        int sr = 1, sc = 1, newColor = 2;
        solution.floodFill(image,sr,sc,newColor);
    }
}
