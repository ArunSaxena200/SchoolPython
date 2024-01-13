class Cookie:
    def __init__(self, cookieType="sugar"):
        self.cookieType = cookieType

    def __str__(self):
        return f"Cookie(type: {self.cookieType})"

chocolateChipCookie = Cookie("chocolate chip")
print(chocolateChipCookie)
