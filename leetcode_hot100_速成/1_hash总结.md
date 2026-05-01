### #1 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
```py
定义dic
遍历nums的下标i和值x
if target-x in dic:   #曾经出现的数与当前x相加正好=target
return [dic[target-x],i]
dic[x]=i   # 记录当前数x的下标是i
```
dic={}    -> 记录出现过的数字及其下标
            {"3":0, "4": 1, }
tar=5
[3,4,6,1,2]    i=0 x=3 tar-x=2 dic[3]=0
            i=1, x=4, tar-x=1  dic[4]=1


### #49 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

思路：维护一个哈希表d(defaultdict(list))
for s遍历strs，字符串s排序后，异位词将相等
按sorted_s为key， 将s加入d中
取出d中的值并加入同一list list(d.values())

### #128 最长连续序列  
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

核心思路是找到连续序列的起点
```py
将nums转成哈希集合set
ans = 0
x->for循环set
如果存在x-1, 跳过当前循环   #x不是起点
y = x+1
while y in set: 不断查找set中的下一个元素--易错：使用循环查找
    y+=1
# y的最终值是序列末尾的下一个数
ans=max(ans, y-x)
```
