from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # Step 1: build optimized adjacency using patterns
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        # Step 2: BFS logic
        que = deque()
        vis = set()

        que.append((beginWord, 1))
        vis.add(beginWord)

        while que:
            word, dist = que.popleft()

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for nei in pattern_map[pattern]:
                    if nei == endWord:
                        return dist + 1

                    if nei not in vis:
                        vis.add(nei)
                        que.append((nei, dist + 1))

                # Important optimization: prevent reprocessing
                pattern_map[pattern] = []

        return 0
