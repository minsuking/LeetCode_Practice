package com.leetcode.problem0529a;

public class Solution0529a {

        public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
            image[sr][sc]=newColor;
            if(sc<image[0].length-1) {
                if (image[sr][sc + 1] == 1) {
                    floodFill(image, sr, sc + 1, newColor);
                }
            }
            if(sr<image.length-1){
                if(image[sr+1][sc]==1) {
                    floodFill(image, sr + 1, sc, newColor);
                }
            }
            if(sc>0) {
                if (image[sr][sc - 1] == 1) {
                    floodFill(image, sr, sc - 1, newColor);
                }
            }
            if(sr>0) {
                if (image[sr - 1][sc] == 1) {
                    floodFill(image, sr - 1, sc, newColor);
                }
            }
            return image;
        }


}
