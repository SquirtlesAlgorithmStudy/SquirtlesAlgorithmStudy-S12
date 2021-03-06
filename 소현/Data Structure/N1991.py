# 작성자 : SH_WON_96
# 2021-02-27 (과거 했던 코드 리뷰)
# 알고리즘 - 재귀
# 문제번호 : 트리 순회

import sys
input = sys.stdin.readline

class Node: # Node로
    def __init__(self, item,left,right): # item 은 root , 좌, 우 받을 수 있음
        self.item = item
        self.left = left
        self.right = right


# 중위순회(왼,루트,오)
def inorder(node):
    if node.left != ".": # 왼쪽에 있으면
        inorder(tree[node.left]) # 왼쪽으로 가서 다시 중위순회
    print(node.item,end="") # 왼쪽 다 돌았으면 루트
    if node.right != ".": # 왼쪽 없으면 이제 오른쪽으로 가자
        inorder(tree[node.right])

# 전위순회(루트,왼,오)
def preorder(node):
    print(node.item, end="") # 루트 먼저 찍고 시작하기
    if node.left != ".": # 왼쪽 있으면
        preorder(tree[node.left]) #왼쪽으로 가서 다시 전위순회
    if node.right != ".": # 다 끝나고 이제 오른쪽 있으면 거기서 전위순회
        preorder(tree[node.right])

# 후위순회(왼,오,루트)
def postorder(node):
    if node.left != ".": # 왼쪽 있으면
        postorder(tree[node.left]) # 왼쪽가서 후위순회
    if node.right != ".": # 이제 오른쪽 있으면
        postorder(tree[node.right]) #오른쪽가서 후위순회
    print(node.item, end="") #끝났으니까 루트 출력하자!




N = int(input())
# 트리를 딕셔너리 형태로 생성
tree = {}

# 트리에 데이터 받기
for i in range(N):
    data = input().rstrip().split()
    tree[data[0]] = Node(item=data[0],left=data[1],right=data[2]) # root에다가 dictionary 형태로 만들어주기 / 각각 노드기준으로 binarytree를 만드는거지.

print(tree)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])


