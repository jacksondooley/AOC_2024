from utils import get_input

if __name__ == "__main__":
    input: str = get_input(1)
    
    rows: list[str] = input.split("\n")

    l1, l2 = [], []

    for row in rows:
        nums: list[int] = [int(num) for num in row.split()]

        if len(nums) == 2:
            l1.append(nums[0])
            l2.append(nums[1])

    l1.sort()
    l2.sort()

    print(l1)
    print(l2)

    cum_sum_diff = 0

    for i in range(len(l1)):
        cum_sum_diff += abs(l1[i] - l2[i])

    print(cum_sum_diff)

