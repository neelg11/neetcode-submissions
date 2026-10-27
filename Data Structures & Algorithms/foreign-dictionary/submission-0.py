class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}
        
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
            else:
                if len(first) > len(second):
                    return ""

        queue = [c for c in indegree if indegree[c] == 0]
        result = []
        for c in queue:
            result.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return "".join(result) if len(result) == len(graph) else ""             
