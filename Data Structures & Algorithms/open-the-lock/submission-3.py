class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for d in deadends:
            if d == '0000':
                return -1
            visited.add(d)
        q = deque()

        q.append(('0000', 0))
        visited.add('0000')

        def children(parent):
            children_list = []
            for i in range(4):
                for dir in [-1,1]:
                    temp = (int(parent[i]) + dir)%10
                    children_list.append(parent[:i] + str(temp) + parent[i+1:])
            return children_list

        while q:
            parent, step = q.popleft()
            for code in children(parent):
                if code == target:
                    return step + 1
                if code not in visited:
                    visited.add(code)
                    q.append((code, step+1))
        return -1
