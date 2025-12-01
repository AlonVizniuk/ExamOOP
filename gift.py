from typing import override
from giftable import Giftable


class Gift(Giftable):

    @override
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")