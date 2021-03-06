import sys

num = int(sys.stdin.readline().strip())
myTree = {} # 딕셔너리

for i in range(num):
  root, left, right = sys.stdin.readline().strip().split()
  myTree[root] = [left, right] # root를 키로 가지게 한다 !


def DLR(root): # 전위순회
  if root != '.':
    print(root, end = '')
    DLR(myTree[root][0]) # 루트 다음 왼쪽
    DLR(myTree[root][1]) # 그 다음 오른쪽


def LDR(root): # 중위순회
  if root != '.':
    LDR(myTree[root][0]) # 왼쪽부터
    print(root, end = '') # root
    LDR(myTree[root][1]) #오른쪽

def LRD(root): # 후위순회
  if root != '.':
    LRD(myTree[root][0]) #왼쪽부터
    LRD(myTree[root][1]) #오른쪽
    print(root, end = '')

DLR('A')
print() # 줄바꿈 !
LDR('A')
print()
LRD('A')
