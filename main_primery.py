from Link10100 import Check_10_100
from LinkDiv2 import LinkDiv2
from LinkDiv3 import LinkDiv3
from LinkDiv5 import LinkDiv5
from LinkDiv7 import LinkDiv7

link0 = Check_10_100()
link2 = LinkDiv2()
link3 = LinkDiv3()
link5 = LinkDiv5()
link7 = LinkDiv7()

head = link0
link0.next = link2
link2.next = link3
link3.next = link5
link5.next = link7

num_list: list = [12, 17, 23, 100, 121, 169]
for num in num_list:
    head.handle(num)
print()

for num in range(30,60):
    head.handle(num)