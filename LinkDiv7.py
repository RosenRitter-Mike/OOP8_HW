from NumHandler import NumHandler


class LinkDiv7(NumHandler):

    def handle(self, number) -> None:

        if not number % 7 :
            print(f"{number} is not primary, dividable by 7")

        else:
            if self.next:
                self.next.handle(number)
            else:
                print(f"{number} is a primary number")
