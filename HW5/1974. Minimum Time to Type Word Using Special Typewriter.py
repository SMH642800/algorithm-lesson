"""
- 一個 a ~ z 的一個特殊的圓型打字機，下圖是LeetCode上面的範例圖
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
"""


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