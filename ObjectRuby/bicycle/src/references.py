from collections import namedtuple


# 悪い例
class ObscuringReferences:
    def __init__(self, data: list[list[int]]):
        self._data = data

    def diameters(self):
        # 0はリム、1はタイヤ
        return map(lambda x: x[0] + (x[1] * 2), self._data)


# 良い例
class RevealingReferences:
    Wheel = namedtuple("Wheel", "rim tire")

    def __init__(self, data: list[list[int]]):
        self.__wheels = self.__wheelify(data)

    def diameters(self):
        return map(lambda wheel: wheel.rim + (wheel.tire * 2), self.__wheels)

    def __wheelify(self, data: list[list[int]]):
        # このメソッドだけが引数のdataの配列構造を知っている
        # 渡す側は結局配列構造を知らないと駄目だけど・・・
        return map(lambda x: self.Wheel(x[0], x[1]), data)


if __name__ == "__main__":
    input = [[622, 20], [622, 23], [559, 30], [559, 40]]

    print("--- 悪い例 ---")
    obscuring = ObscuringReferences(input)
    for value in obscuring.diameters():
        print(value)

    print("--- 良い例 ---")
    revealing = RevealingReferences(input)
    for value in revealing.diameters():
        print(value)
