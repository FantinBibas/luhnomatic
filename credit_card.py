#!/usr/bin/env python3


class CreditCard:
    UNKNOWN_DIGIT = '*'

    def __init__(self, number: str):
        self.number = ''.join([c for c in number if c.isdigit() or c == self.UNKNOWN_DIGIT])

    def __str__(self):
        return self.number

    def get_unknown_digits_nbr(self):
        return self.number.count(self.UNKNOWN_DIGIT)

    def get_card_number_possibilities(self):
        unknown_digits = self.get_unknown_digits_nbr()
        if unknown_digits < 2:
            return 1
        return 10 ** (unknown_digits - 1)

    def get_first_unknown_digit_position(self):
        for i, c in enumerate(self.number):
            if c == self.UNKNOWN_DIGIT:
                return i
        return -1

    def get_luhn_sum(self):
        luhn_sum = 0
        parity = len(self.number) % 2
        for i, digit in enumerate(self.number):
            if digit != self.UNKNOWN_DIGIT:
                digit_val = int(digit)
                if i % 2 == parity:
                    digit_val *= 2
                    if digit_val > 9:
                        digit_val -= 9
                luhn_sum += digit_val
        return luhn_sum

    def get_first_unknown_digit_guess(self):
        luhn_sum = self.get_luhn_sum()
        guess = (10 - luhn_sum % 10) % 10
        if self.get_first_unknown_digit_position() % 2 == len(self.number) % 2:
            if guess % 2 == 0:
                return guess // 2
            return (guess + 9) // 2
        return guess

    def get_all_possibilities(self):
        unknown_digits = self.get_unknown_digits_nbr()
        if unknown_digits == 0:
            return [self]
        if unknown_digits == 1:
            return [CreditCard(self.number.replace('*', str(self.get_first_unknown_digit_guess())))]
        pos = self.get_first_unknown_digit_position()
        possibilities = []
        sub_number = list(self.number)
        for i in range(0, 10):
            sub_number[pos] = str(i)
            sub_card = CreditCard(''.join(sub_number))
            possibilities += sub_card.get_all_possibilities()
        return possibilities
