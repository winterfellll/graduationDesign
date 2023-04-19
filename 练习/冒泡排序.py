def solution(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:  # 升序用>，降序用<
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

    # for i in range(len(lst)):
    #     for j in range(i + 1, len(lst)):
    #         if lst[j] > lst[i]:
    #             lst[j], lst[i] = lst[i], lst[j]
    # return lst


def main():
    list = [1, 23, 32, 223, 12, 3, 34]
    print(solution(list))


if __name__ == "__main__":
    main()
