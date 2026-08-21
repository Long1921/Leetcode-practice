# 206 反转链表 | 简单 | 考点：链表、双指针（迭代反转）
# 核心思路：prev/p 两只手从左往右走。每圈四步：
#   ① q = p.next 抢救下一个（改箭头前必做，否则后面的链丢失）
#   ② p.next = prev 掉头  ③ prev = p 挪锚  ④ p = q 挪人
#   p 走到 None 时循环结束，prev 恰好抓着原尾节点 = 新头
# 时间复杂度：O(n)，每个节点处理一次
# 空间复杂度：O(1)，只用三个指针变量
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        p = head
        while p:
            q = p.next
            p.next = prev
            prev = p
            p = q
        return prev

# ---- 本地测试（链表题通用脚手架：build 造链 / show 打印链）----
def build(vals):
    h = None
    for v in reversed(vals):
        h = ListNode(v, h)
    return h

def show(node):
    out = []
    while node:
        out.append(str(node.val)); node = node.next
    return ' -> '.join(out) if out else 'None'

if __name__ == '__main__':
    s = Solution()
    print(show(s.reverseList(build([1,2,3,4,5]))))   # 期望 5 -> 4 -> 3 -> 2 -> 1
    print(show(s.reverseList(build([1]))))            # 期望 1
    print(show(s.reverseList(build([]))))             # 期望 None
