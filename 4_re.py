import re
from tkinter import E
# bacd, book, desk
# ca?e
# care, cafe, case, cave
# case, cabe, cace, cade ...

p = re.compile("ca.e")
# .(ca.e) 하나의 문자를 의미 > care, cafe, case (0) | caffe(x)
# ^(^de) 문자열의 시작 > desk, destination (o) | caffe(x)
# $(se$) 문자열의 끝 > case, base (o) | face (x)

def print_match(m):

    if m:
        print(m.group())
    else:
        print("マチングできない")

m = p.match("care")
print_match(m)
# print(m.group()) # 매치되지 않으면 에러가 발생