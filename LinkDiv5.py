from NumHandler import NumHandler


class LinkDiv5(NumHandler):

    def handle(self, number) -> None:

        if not number % 5 :
            print(f"{number} is not primary, dividable by 5")

        else:
            if self.next:
                self.next.handle(number)
