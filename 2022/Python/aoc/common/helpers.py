def split_list_in_half(list_: list) -> tuple[list, list]:
    if len(list_) % 2 != 0:
        raise RuntimeError("List cannot be safely split in half as its length is not multiple of 2")

    size = len(list_)
    first_half = list_[size // 2:]
    second_half = list_[:size // 2]

    return first_half, second_half