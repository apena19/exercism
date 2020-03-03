class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        c = [int(x) for x in self.card_num[::-2]]
        u2 = [(2 * int(y)) // 10 + (2 * int(y)) % 10 for y in self.card_num[-2::-2]]
        return sum(c + u2) % 10 == 0
