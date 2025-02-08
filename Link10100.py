from NumHandler import NumHandler


class Check_10_100(NumHandler):

    def handle(self, number) -> None:
        if 100 >= number >= 10:
            if self.next:
                self.next.handle(number)
        else:
            print(f"{number} is not in range")
