def sum(*statistik):
    count = 0
    for stat in statistik:
        count += stat
    return count


def average(*statistik):
    jumlah = 0
    for stat in statistik:
        jumlah += 1
    rata_rata = sum(*statistik)/jumlah
    return rata_rata


def max(*statistik):
    maksimal = statistik[0]
    for stat in statistik:
        if (stat > maksimal):
            maksimal = stat
    return maksimal


def min(*statistik):
    minimal = statistik[0]
    for stat in statistik:
        if (stat < minimal):
            minimal = stat
    return minimal
