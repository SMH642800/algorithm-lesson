###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW5 
# 概念題 :book: 
## 1.  Heap Sort
- 題目 :
    1. 下圖為Max Heap。Heap Sort的每一回合，會將Heap的最大值刪除後，又恢復為Heap。請畫出==第一回合恢復的過程==。
    2. 投影片69頁的公式如下，請解釋此公式的含意。

---

- 解答 : 
    1. ![](https://i.imgur.com/iRBUjwK.jpg)
    
    2. 在每一層時，所有的node在restore時所需要的比較次數總和，總共要做==d-1==次 
       ==(d: 樹高)==
       ![](https://i.imgur.com/zhl8Bxn.jpg)


## 2. Problem平均的Lower Bound
- 題目 :
    - 下圖為二元樹。參考投影片77頁，已知最高點(root)的深度為1，請算出二元樹的External Path Length，以及葉子平均深度。
    - ![](https://i.imgur.com/ytA0PUo.png)
    
- 解答 : 
    - External Path Length **(depth * number of leaves)** :  (4 * 4) + (3 * 2) = 22
    - Leaf's 平均深度 : 
        - c (Leaf總數) = 4 + 2 = 6
        - d (樹高) = 4
        - M (Leaf深度的總和) = (2 * 3) + (4 * 4) = 22
        - 平均深度 : **M/n!** = 22 / 6 = 3.666...
    
## 3. Problem Transformation
- 題目 : 
    - Sorting problem reduces to Convex Hull Problem
    - 請說明，若要排序五個數字：4,1,3,2,5，如何轉為Convex Hull Problem後，完成排序。
- 解答 : 
    - **X -> (X, X^2)**
        ![](https://i.imgur.com/iaqrn5B.jpg)

---

# 程式題 : Greedy類型 :desktop_computer:
- 所謂Greedy，就是每回合找最佳解，可得到整體的最佳解
- [更多Greedy類型題目](https://leetcode.com/tag/greedy/)

## 4. 圓型打字機
- [1974. Minimum Time to Type Word Using Special Typewriter - LeetCode](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/)
- 題目：
    - 一個 a ~ z 的一個特殊的圓型打字機，下圖是LeetCode上面的範例圖
    ![](https://i.imgur.com/hnuupO8.png)
    - 上面會有一個指針，當指針指到某個英文字母時才能輸入目前指到的英文字母，這個指針最初預設會停在 ‘a’。
    - 記時規則：每一秒只能做一個動作，能操作的動作如下：
        - 將指針順時針或逆時針移動一個字
        - 輸入目前指到的英文字母
    - 題目會給一個 word 字串，目標是用最短秒數打完這組字串，最終回傳這個最短秒數。
    - 範例：
        - 輸入：‘abd’
        - 輸出：6
        - 說明：
            - 轉到a(0秒)
            - 印出a(1秒)
            - 轉到b(1秒)
            - 印出b(1秒)
            - 轉到d(2秒)
            - 印出d(1秒)
            - 總和為6秒

---

:::info
解題思路 : 
- 先將字元轉換成ASCII，再跟前一個字元的ASCII進行相減
- 若超過中間(26/2)，則代表往另一邊找會比較快
:::
1. 程式碼 : 
``` python
class Solution:
    def minTimeToType(self, word: str) -> int:
        total_seconds = 0   
        now_word = 'a'   # 初始化: 指標在a
        
        for w in word:
            # 先將字元轉換成ASCII，再跟前一個字元的ASCII進行相減
            # 若差過中間(26/2)，則代表往另一邊找會比較快
            move_sec = abs(ord(w) - ord(now_word))
            if move_sec > 13:
                total_seconds += (26 - move_sec)
            else:
                total_seconds += move_sec
            total_seconds += 1   # 輸出秒數
            now_word = w   # 將輸入的字元記錄下來
        
        return total_seconds
```
2. 測試結果 :
![](https://i.imgur.com/9UdldQY.png)
3. 花費時間 : 26 min
4. 自己完成的程度 : 自己完成，有查一些語法問題

## 5. 跳到最後
- [55. Jump Game](https://leetcode.com/problems/jump-game/)
- 題目：
    - 已知一個數列，每個數字代表可以向後跳的最大距離，請判斷是否可從起點，多次跳躍後，可到達最終點。
    - 範例：
        - 輸入：3,2,4,2,4
        - 輸出：true
        - 說明
            - 由index 0的位置，跳躍3個數至index 3。
            - 從index 3的位置，跳躍1個數，最到達最終點。
    - 範例：
        - 輸入：3,2,1,0,4
        - 輸出：false
        - 說明
            - 由index 0,1,2最遠只能跳到index 3。
            - 由index 0,1,2最遠只能跳到index 3。

---

:::info
解題思路 : 
- **method 1** : 
    - 設定一個target_index，當作能走到的點，預設為list的最後一個
    - 從倒數第二個index往前一個個檢查，若能到達則把target_index替換掉
    - 若能走到第一個index，代表絕對能夠從第一個index走到最後一個index
- **method 2** : 
    - 設定一個far_reach_index，代表目前能走到最遠的點，預設為最一開始的起點
    - 利用enumerate函數，將目前的index能走到最遠的點和far_reach_index進行比較，兩者之間取最大值
    - 若發現目前的index已經超過far_reach_index時，則代表絕對走不到最後一個index
:::

1. 程式碼 : 
    - method 1
    ```python
    class Solution:
        def canJump(self, nums: List[int]) -> bool:
            target_index = len(nums) - 1
            # 從倒數第二個index往前一個個檢查
            for index in range((len(nums)-2), -1, -1):
                # 若能到達則把target_index替換掉
                if (index+nums[index] >= targetIndex):
                    target_index = index
            # 若能走到第一個index，代表能夠從第一個index走到最後一個index
            if target_index == 0:  
                return True
            else:
                return False
    ```
    - method 2
    ```python
    class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far_reach_index = 0   # 最遠能達到的index
        # enumerate(sequence: list, [start=0]):
        # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        for index, number in enumerate(nums):
            if index > far_reach_index:
                return False
            far_reach_index = max(far_reach_index, index + number)
        return True
    ```
2. 測試結果 : 
![](https://i.imgur.com/QyaR3Eg.png)
3. 花費時間 : 40 min
4. 自己完成的程度 : 一開始先自己想出解法，後面有再上網查其他人的做法


# 本週心得
- 程式題的部分，寫得算滿開心的，現在都會自己先想看看，等寫不出來或著是寫出來但覺得不夠好時，還會去上網找看看其他人的做法，增進思考
