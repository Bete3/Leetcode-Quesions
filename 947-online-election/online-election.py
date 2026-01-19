class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        count = {}
        leader = -1
        maxVotes = 0
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= maxVotes:
                maxVotes = count[p]
                leader = p
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t) - 1
        return self.leaders[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)