from NumHandler import NumHandler


class LinkDiv2(NumHandler):

    def handle(self, number) -> None:

        if not number % 2 :
            print(f"{number} is not primary, it is even (dividable by 2)")

        else:
            if self.next:
                self.next.handle(number)
