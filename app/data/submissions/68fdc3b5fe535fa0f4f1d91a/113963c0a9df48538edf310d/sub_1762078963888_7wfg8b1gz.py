class ThiSinh:
    def __init__(self, idx, name, d1, d2):
        self.id = f"TS{idx:02d}"
        self.name = name.title().strip()
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.avg = self.calc_avg()

    def calc_avg(self):
        score_1 = self.d1 / 10 if self.d1 > 10 else self.d1
        score_2 = self.d2 / 10 if self.d2 > 10 else self.d2
        return round((score_1 + score_2) / 2, 2)

    def rank(self):
        a = self.avg
        if a >= 9.5:
            return "XUAT SAC"
        elif a >= 8.0:
            return "DAT"
        elif a >= 5.0:
            return "CAN NHAC"
        else:
            return "TRUOT"

    def show(self):
        return f"{self.id} {self.name} {self.avg:.2f} {self.rank()}"

ls = []
n = int(input())
for i in range(1, n + 1):
    name = input().strip()
    d1 = float(input())
    d2 = float(input())
    ls.append(ThiSinh(i, name, d1, d2))

ls.sort(key=lambda x: x.avg, reverse=True)

for ts in ls:
    print(ts.show())
