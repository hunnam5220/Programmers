import sys
sys.setrecursionlimit(int(1e6))


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


pre = []
post = []


def preorder(node, nodeinfo):
    # root 부터 좌측 노드를 순회
    pre.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)


def postorder(node, nodeinfo):
    # 깊이가 가장 깊은 맨 왼쪽 노드에 도착할 때까지 재귀 후
    if node.left:
        postorder(node.left, nodeinfo)

    if node.right:
        postorder(node.right, nodeinfo)

    # 올라가며 순회 (좌 > 우)
    post.append(nodeinfo.index(node.data) + 1)


def solution(nodeinfo):
    # y의 크기가 가장 큰 노드가 root가 되니 y를 기준으로 정렬
    new_node = sorted(nodeinfo, key=lambda k: -k[1])

    # root 값 초기화
    root = None

    # 정렬된 노드들을 기준으로 연결 시작
    for node in new_node:
        # root 의 값이 비어있다면?
        if not root:
            root = Tree(node)
        else:
            current = root
            while 1:

                # root의 x 값이 현재 노드의 x값보다 크면
                if node[0] < current.data[0]:

                    # root 좌측 노트가 비어있지 않으면
                    if current.left:
                        current = current.left
                        continue
                    else:
                        # root 좌측 노트가 비어있으면 연결
                        current.left = Tree(node)
                        break

                # 우측 노드 구하기
                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

                break

    # 전위 순회
    preorder(root, nodeinfo)

    # 후위 순회
    postorder(root, nodeinfo)

    return [pre, post]


# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
