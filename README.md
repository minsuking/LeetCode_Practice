# LeetCode_Practice
Practice Leetcode Problem
![1](https://user-images.githubusercontent.com/60283244/142562615-2d1f183f-33d3-4a15-83f3-e1e9e89aeec6.JPG)
```python
def trailingZeroes(self, n: int) -> int:
        
    # Calculate n!
    n_factorial = 1
    for i in range(2, n + 1):
        n_factorial *= i
    
    # Count how many 0's are on the end.
    zero_count = 0
    while n_factorial % 10 == 0:
        zero_count += 1
        n_factorial //= 10
        
    return zero_count
```
![2-1](https://user-images.githubusercontent.com/60283244/142562618-f983876d-45e0-4e27-b03c-7bce231207df.JPG)
![2-2](https://user-images.githubusercontent.com/60283244/142562619-9a40a984-0467-476d-874a-0b797870c916.JPG)
![2-3](https://user-images.githubusercontent.com/60283244/142562621-df1a8862-b595-4aba-bb8f-37e2fbae9e10.JPG)
![2-4](https://user-images.githubusercontent.com/60283244/142562623-a9733ba9-75b0-480d-a57b-9d3d53b09a30.JPG)
![2-5](https://user-images.githubusercontent.com/60283244/142562625-50a60f2b-6db8-463f-b5c5-57b23a2cf4a7.JPG)
![2-6](https://user-images.githubusercontent.com/60283244/142562628-425ffe43-4f6e-4c4b-bec1-71eb53653135.JPG)
```python
def trailingZeroes(self, n: int) -> int:
        
    zero_count = 0
    for i in range(5, n + 1, 5):
        current = i
        while current % 5 == 0:
            zero_count += 1
            current //= 5

    return zero_count
```
```python
def trailingZeroes(self, n: int) -> int:
        
    zero_count = 0
    for i in range(5, n + 1, 5):
        power_of_5 = 5
        while i % power_of_5 == 0:
            zero_count += 1
            power_of_5 *= 5

    return zero_count
```
![2-7](https://user-images.githubusercontent.com/60283244/142562630-d42234e3-8d31-4739-9ba6-15cfcd5bd13f.JPG)
![3-1](https://user-images.githubusercontent.com/60283244/142562632-a1fdad40-76e3-48e5-9cb6-42fcee1c6160.JPG)
![3-2](https://user-images.githubusercontent.com/60283244/142562633-64af0929-1c62-4e56-a385-2d17e9e93437.JPG)
```python
def trailingZeroes(self, n: int) -> int:
    zero_count = 0
    current_multiple = 5
    while n >= current_multiple:
        zero_count += n // current_multiple
        current_multiple *= 5
    return zero_count
```
![3-3](https://user-images.githubusercontent.com/60283244/142563170-d596a880-c0fb-4492-802b-35889b3fdbd8.JPG)
```python
def trailingZeroes(self, n: int) -> int:
    zero_count = 0
    while n > 0:
        n //= 5
        zero_count += n
    return zero_count
```
Complexity Analysis

Time complexity : O(\log \, n)O(logn).

In this approach, we divide nn by each power of 55. By definition, there are \log_5nlog 
5
​
 n powers of 55 less-than-or-equal-to nn. Because the multiplications and divisions are within the 32-bit integer range, we treat these calculations as O(1)O(1). Therefore, we are doing \log_5 n \cdot O(1) = \log \, nlog 
5
​
 n⋅O(1)=logn operations (keeping in mind that \loglog bases are insignificant in big-oh notation).

Space complexity : O(1)O(1).

We use only a fixed number of integer variables, therefore the space complexity is O(1)O(1).
