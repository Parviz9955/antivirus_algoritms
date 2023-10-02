import math


def numeric_check(bit_list):
    if isinstance(bit_list, list):
        for i in range(len(bit_list)):
            if bit_list[i] != 0 and bit_list[i] != 1:
                raise Exception('list must have includ only 1 or 0')
    return bit_list


def transformer(bit_list):
    for i in range(len(bit_list)):
        bit_list[i] = 2 * bit_list[i] - 1
    return bit_list


class PST:

    def __init__(self, bit_list):
        self.bit_list = numeric_check(bit_list)
        self.t_bit_list = transformer(self.bit_list)

    def frequency_test(self):
        s = abs(sum(self.t_bit_list)) / math.sqrt(len(self.t_bit_list))
        if s <= 1.82138636:
            return True
        else:
            return False

    def sequence_identical_test(self):  # Test for sequence of identical bits
        n = len(self.bit_list)
        p = sum(self.bit_list) / n
        v = 0
        for i in range(n - 1):
            if self.bit_list[i] != self.bit_list[i + 1]:
                v += 1

        s = abs(v - 2 * n * p * (1 - p)) / 2 * math.sqrt(2 * n) * p * (1 - p)

        if s <= 1.82138636:
            return True
        else:
            return False

    def extended_randomness_test(self):  # Extended Randomness Test
        s_list = [0]
        for i in range(len(self.t_bit_list)):
            s_list.append(sum(self.t_bit_list[0:i]))
        s_list.append(0)
        l = -1
        for k in s_list:
            if k == 0:
                l += 1
        e_keys = {-9: 0, -8: 0, -7: 0, -6: 0, -5: 0, -4: 0, -3: 0, -2: 0, -1: 0,
                  1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for s_item in s_list:
            if s_item in e_keys:
                e_keys[s_item] += 1

        y_list = []

        for key in e_keys:
            y_list.append(abs(e_keys[key] - l) / math.sqrt(2 * l * (4 * abs(key) - 2)))

        flag = True
        for y in y_list:
            if y > 1.82138636:
                flag = False
        return flag
