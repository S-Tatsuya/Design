def total():
    print("5人の点数の合計点と平均点を求めます。")

    tensu1 = int(input("1番目の点数:"))
    tensu2 = int(input("2番目の点数:"))
    tensu3 = int(input("3番目の点数:"))
    tensu4 = int(input("4番目の点数:"))
    tensu5 = int(input("5番目の点数:"))

    total = 0
    total += tensu1
    total += tensu2
    total += tensu3
    total += tensu4
    total += tensu5

    print(f"合計は{total}点です。")
    print(f"平均は{total / 5}点です。")
