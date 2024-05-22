d_1 = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
d_10 = {
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}
d_1020 = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

d_0 = {
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million'
}

def int2txt(n: str) -> list:
    if n:
        return [n[i:i+3:][::-1] for i in range(0, len(n),3)][::-1]

def hundred(n:str) -> str:
    if not n.isdigit():
        return 'Wrong input'
    match len(n):
        case 0:
            return 'Wrong input'
        case 1:
            return d_1[int(n)]
        case 2:
            try:
                return d_1020[int(n)]
            except KeyError:
                return f"{d_10[int(n[0])*10]} {d_1[int(n[1])]}"
        case 3:
            try:
                return f"{d_1[int(n[0])]} hundred {d_1020[int(n[1:])]}"
            except KeyError:
                try:
                    return f"{d_1[int(n[0])]} hundred {d_10[int(n[1])*10]} {d_1[int(n[2])]}"
                except KeyError:
                    return f"{d_1[int(n[0])]} hundred {d_1[int(n[2])]}"

res = int2txt(input()[::-1])
match len(res):
    case 0:
        print('Wrong input')
    case 1:
        print(hundred(res[0]))
    case 2:
        print(f"{hundred(res[0])} thousand {hundred(res[1])}")
    case 3:
        print(f"{hundred(res[0])} million {hundred(res[1])} thousand {hundred(res[2])}")