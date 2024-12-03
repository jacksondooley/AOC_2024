from utils import get_input

if __name__ == "__main__":
    input: str = get_input(1)

    rows: list[str] = input.split("\n")

    left_list_map_count = {}
    right_list_map_count = {}

    for row in rows:
        nums: list[int] = [int(num) for num in row.split()]

        if len(nums) == 2:
            left_list_map_count[nums[0]] = left_list_map_count.get(nums[0], 0) + 1
            right_list_map_count[nums[1]] = right_list_map_count.get(nums[1], 0) + 1


    cum_sum_diff = 0
    for k, v in left_list_map_count.items():
        if k in right_list_map_count:
            cum_sum_diff += left_list_map_count[k] * k * right_list_map_count[k]

    print(cum_sum_diff)

    
