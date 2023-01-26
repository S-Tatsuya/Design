def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f"円盤[{no}]を{x}軸から{y}軸へ移動")

    if no > 1:
        move(no - 1, 6 - x - y, y)
