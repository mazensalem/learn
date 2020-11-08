def solve(n):
    nums = [0 for i in range(n + 1)]
    nums[0] = 0
    nums[1] = 1
    i = 1
    while True:
        isstop = False
        if 2 <= 2 * i and 2 * i <= n:
            nums[2 * i] = nums[i]
        else:
            isstop = True
        if 2 <= 2 * i + 1 and 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        else:
            if isstop:
                break
        i += 1

    return max(nums)


def solve1(s):
    ns = "".join(list(set(s)))
    di = {}
    result = 0
    for char in ns:
        delete = 0
        vals = di.values()
        while s.count(char) - delete in vals:
            result += 1
            delete += 1
        else:
            if s.count(char) - delete:
                di[char] = s.count(char) - delete
    return result
