from NumHandler import NumHandler


class LinkDiv3(NumHandler):

    def handle(self, number) -> None:

        if not number % 3 :
            print(f"{number} is not primary, dividable by 3")

        else:
            if self.next:
                self.next.handle(number)
