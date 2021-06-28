from random import randint, choice

# author: garbu
# modified by: wnaBee

def generate_card():
    card_types = ["americanexpress","visa13", "visa16","mastercard","discover"]
    type = choice(card_types)

    def prefill(t):
        # typical number of digits in credit card
        def_length = 16

        if t == card_types[0]:
            # override the def lengths
            return [3, randint(4,7)], def_length - 2

        elif t == card_types[1] or t == card_types[2]:
            # visa starts with 4
            if t.endswith("16"):
                return [4], def_length - 1
            else:
                return [4], def_length - 4

        elif t == card_types[3]:
            # master card start with 5
            return [5, randint(1,5)], def_length - 2

        elif t == card_types[4]:
            # discover card starts with 6011
            return [6, 0, 1, 1], def_length - 4

    def finalize(nums):
        check_sum = 0
        check_offset = (len(nums) + 1) % 2

        for i, n in enumerate(nums):
            if (i + check_offset) % 2 == 0:
                n_ = n*2
                check_sum += n_ -9 if n_ > 9 else n_
            else:
                check_sum += n
        return nums + [10 - (check_sum % 10) ]

    # main body
    t = type.lower()
    initial, rem = prefill(t)
    so_far = initial + [randint(1,9) for x in range(rem - 1)]
    return "".join(map(str,finalize(so_far))), type
