# Python 刷题语法速查表

## 为什么适合用 Python 刷题

- 语法简洁，写题速度快
- 内置数据结构强，适合面试高频题
- 更容易把注意力放在思路而不是语言细节上
- 和你当前的 Agent / LangChain 学习主线一致

---

## 1. 输入输出与基础习惯

### 常见写法

```python
print(x)
print(a, b)
```

### 多变量交换

```python
a, b = b, a
```

### 同时赋值

```python
left, right = 0, len(nums) - 1
```

---

## 2. 列表 list

### 创建

```python
nums = [1, 2, 3]
arr = [0] * 10
matrix = [[0] * n for _ in range(m)]
```

### 常用操作

```python
nums.append(4)
nums.pop()
nums.pop(0)
nums.insert(1, 99)
nums.remove(2)
len(nums)
```

### 排序

```python
nums.sort()
nums.sort(reverse=True)
nums.sort(key=lambda x: x[1])

new_nums = sorted(nums)
```

### 反转

```python
nums.reverse()
rev = nums[::-1]
```

### 切片

```python
nums[l:r]
nums[:r]
nums[l:]
nums[::-1]
```

---

## 3. 字符串 str

### 常用操作

```python
s = "abc"
len(s)
s[0]
s.lower()
s.upper()
s.strip()
s.split(",")
"-".join(["a", "b", "c"])
```

### 字符串转列表

```python
chars = list(s)
```

### 列表转字符串

```python
res = "".join(chars)
```

### 判断字符类型

```python
ch.isdigit()
ch.isalpha()
ch.isalnum()
```

---

## 4. 字典 dict

### 创建

```python
d = {}
d = {"a": 1, "b": 2}
```

### 常用操作

```python
d["a"] = 10
val = d.get("a", 0)
"a" in d
d.pop("a")
```

### 遍历

```python
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)
```

### 高频用途

- 计数
- 去重
- 建映射关系

---

## 5. 集合 set

### 创建

```python
s = set()
s = {1, 2, 3}
```

### 常用操作

```python
s.add(4)
s.remove(2)
s.discard(10)
1 in s
```

### 高频用途

- 去重
- O(1) 判断元素是否存在

---

## 6. collections 常用工具

### Counter

```python
from collections import Counter

cnt = Counter(nums)
cnt = Counter(s)
```

### defaultdict

```python
from collections import defaultdict

d = defaultdict(int)
d = defaultdict(list)
d = defaultdict(set)
```

### deque

```python
from collections import deque

q = deque()
q.append(1)
q.appendleft(2)
q.pop()
q.popleft()
```

### 高频用途

- `Counter`：统计频次
- `defaultdict(list)`：分组
- `deque`：队列、BFS、单调队列

---

## 7. 堆 heapq

Python 默认是小顶堆。

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

x = heapq.heappop(heap)
```

### 取前 k 大

```python
heapq.nlargest(k, nums)
heapq.nsmallest(k, nums)
```

### 模拟大顶堆

```python
heapq.heappush(heap, -x)
```

---

## 8. bisect 二分

```python
import bisect

idx = bisect.bisect_left(nums, target)
idx = bisect.bisect_right(nums, target)
```

### 作用

- 找插入位置
- 找左边界 / 右边界

---

## 9. 常用遍历技巧

### enumerate

```python
for i, x in enumerate(nums):
    print(i, x)
```

### zip

```python
for a, b in zip(nums1, nums2):
    print(a, b)
```

### 倒序遍历

```python
for i in range(n - 1, -1, -1):
    print(i)
```

---

## 10. 排序中的 key

### 按第二个元素排序

```python
arr.sort(key=lambda x: x[1])
```

### 按多个条件排序

```python
arr.sort(key=lambda x: (x[0], -x[1]))
```

---

## 11. 前缀和

### 一维前缀和

```python
pre = [0] * (n + 1)
for i in range(n):
    pre[i + 1] = pre[i] + nums[i]
```

### 区间和

```python
sum_lr = pre[r + 1] - pre[l]
```

---

## 12. 双指针常用框架

### 左右指针

```python
left, right = 0, len(nums) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

### 快慢指针

```python
slow = 0
for fast in range(len(nums)):
    if condition:
        nums[slow] = nums[fast]
        slow += 1
```

---

## 13. 滑动窗口模板

```python
left = 0
for right in range(len(s)):
    # 1. 扩大窗口
    # 2. 更新状态

    while 窗口不满足条件:
        # 3. 缩小窗口
        left += 1

    # 4. 更新答案
```

---

## 14. 二分模板

### 左闭右闭

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

---

## 15. 链表常用技巧

### 虚拟头节点

```python
dummy = ListNode(0)
dummy.next = head
cur = dummy
```

### 快慢指针找中点

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### 反转链表

```python
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

---

## 16. 树的 DFS / BFS 模板

### DFS

```python
def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
```

### BFS

```python
from collections import deque

q = deque([root])
while q:
    node = q.popleft()
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
```

---

## 17. 回溯模板

```python
res = []
path = []

def backtrack(start):
    if 满足结束条件:
        res.append(path[:])
        return

    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
```

---

## 18. 动态规划思考顺序

写 DP 时优先按下面顺序思考：

1. `dp[i]` 或 `dp[i][j]` 表示什么
2. 状态转移方程是什么
3. 初始值是什么
4. 遍历顺序是什么

---

## 19. 常见易错点

- `[[0] * n] * m` 会造成二维数组联动修改
- `dict[key]` 直接取值可能 KeyError，优先 `get`
- `list.pop(0)` 是 O(n)，队列优先用 `deque`
- 字符串不可变，频繁拼接优先用列表再 `join`
- 二分、滑窗、链表题最容易写错边界

---

## 20. 一周速成最常用库

```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
```

---

## 21. 面试时的推荐写法风格

- 变量名尽量清晰：`left`、`right`、`slow`、`fast`
- 先写框架，再补细节
- 关键逻辑前可以口述思路
- 尽量避免过度炫技写法

---

## 22. 建议重点掌握的 Python 能力

- 列表、字典、集合的常用操作
- `Counter`、`defaultdict`、`deque`
- 堆 `heapq`
- 二分 `bisect`
- 排序 `sort(key=...)`
- 回溯、DFS、BFS、滑窗、二分模板

---

## 最后建议

- 刷题时优先保证代码稳定正确，再考虑写得多短。
- 每学完一个题型，就把对应模板手敲 2 到 3 遍。
- Python 的优势是“快和清晰”，不是“写花活”。
