def generate_result_list(length: int):
    return [False for i in range(length)]


def get_jump_index(end_of_river: int, leaves_list: list):
    result_list = generate_result_list(end_of_river)
    sec = -1
    for item in leaves_list:
        if False in result_list:
            sec = sec+1
            result_list[item-1] = True

    if False in result_list:
        return -1
    return sec
