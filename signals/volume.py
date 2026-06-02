def get_volume_score(volume_ratio):

    if volume_ratio >= 5:
        return 20

    elif volume_ratio >= 3:
        return 16

    elif volume_ratio >= 2:
        return 12

    elif volume_ratio >= 1.5:
        return 8

    elif volume_ratio >= 1.2:
        return 4

    return 0