# 4章
- メッセージに着目することで`Client`クラスが`Service`クラスに対して何をお願いしているかが見える。
    - 「何を」をお願いする場合は、**機能的結合度**のクラス間のメッセージになっている。
    - 「どのように」が含まれている場合は、**手続き的結合**,**制御的結合**のクラス間のメッセージになっている。
    - **再利用したい**クラスが`Client`として「どのように」を含めるメッセージのやり方になる場合は修正が必要。
        - すべてのクラスを、「何を」にすることができないので見極めが必要。
            - Clean Architectureでの、`Entitie`と`Interractor`の区別ができるといいかも
    - 「どのように」が含まれている場合にパブリックメッセージの不足が考えられる。
        - 「どのように」が含まれていることを見つける指標として「**デメテルの法則**」を知っていると気づきやすい

```
メッセージが
    ✗ 「受け手がどのように振る舞うかを指示するもの」ではなく、
    ○ 「送り手が相手を信頼して望むことを頼む」ものであるとき
予期しなかった方法や、新しい方法で再利用できる柔軟なパブリックインターフェースを自然に進化させる。
```


## シーケンスの作成:Customer
### First Step
- `neeb bike`の設定を`Trip`が受け取るべきか?
``` plantuml
@startuml
participant Moe <<Customer>>
participant Trip <<class>>

Moe -> Trip: suitable_trips(\non_data,\n of_difficulty,\n need bike)
activate Trip
Trip --> Moe
deactivate Trip
@enduml
```

### Second Step
- `Moe`が`Trip`,`Bicycle`が「どのように」望むものを用意するかを知っている。
    - `Trip`に旅行一覧を用意してもらってから`Bicycle`に自転車を用意してもらうこと  
- このことにより`Moe`は旅行の準備ロジックが変化したら自身も変化することを求められてしまう
    - これは`制御結合`になっている。
        
``` plantuml
@startuml
participant Moe <<Customer>>
participant Trip <<Class>>
participant Bicycle <<Class>>

Moe -> Trip: suitable_trip(\non_date, \nof_difficulty)
activate Trip
Trip --> Moe
deactivate Trip
note over Moe: for each trip found

Moe -> Bicycle: suitable_bicycle(\ntrip_date, \nroute_type)
activate Bicycle
Bicycle --> Moe
deactivate Bicycle
@enduml
```

### Third Step
- 「どのように」ではなく、「何を」を頼むようにする。
    - これにより、「どのように」を管理するための**クラス**(`TripFinder`)が必要なことがわかる。
    - `Customer`クラスが知りすぎているということに気付ける必要がある。
- 今回の変更による効果
    - `Moe`が「どのように」から切り離されたことで、`Customer`クラスの再利用性が上がる。
    - `Trip`,`Bicycle`の再利用も可能。
    - ただし、`TripFinder`は**手続き的結合**のため、再利用が難しい。
        - `Trip`,`Bicycle`と一緒に使用することが前提のクラスになる。

``` plantuml
@startuml
participant Moe <<Customer>>
participant TripFinder <<a>>
participant Trip <<Class>>
participant Bicycle <<Class>>

Moe -> TripFinder: suitable_trips(\n on_date, \n of_difficulty, \n need_bike)
activate TripFinder
TripFinder -> Trip: suitable_trips(\n on_date, \n of_difficulty)
activate Trip
TripFinder <-- Trip
deactivate Trip
note over TripFinder: for each trip found
TripFinder -> Bicycle: suitable_bicycle(\n on_date, \n route_type)
activate Bicycle
TripFinder <-- Bicycle
deactivate Bicycle
Moe <-- TripFinder
deactivate TripFinder
@enduml
```



## シーケンスの作成:Mechanic
### First Step
- `Trip`が`Mechanic`にすべての指示を出す関係になっている。
``` plantuml
@startuml
Trip -> Trip : bicycles
note over Trip: for each bicycle
Trip -> Mechanic: clean_bicycle(bike)
activate Mechanic
Mechanic --> Trip
deactivate Mechanic
Trip -> Mechanic: clean_bicycle(bike)
activate Mechanic
Mechanic --> Trip
deactivate Mechanic
Trip -> Mechanic: pump_tires(bike)
activate Mechanic
Mechanic --> Trip
deactivate Mechanic
Trip -> Mechanic: lube_chain(bike)
activate Mechanic
Mechanic --> Trip
deactivate Mechanic
Trip -> Mechanic: check_brakes(bike)
activate Mechanic
Mechanic --> Trip
deactivate Mechanic
@enduml
```

### Second Step
- `Trip`と`Mechanic`を繋ぐ`メッセージ`を一つにすることができた
    - `Trip`は旅行の準備に`bicycle`の準備が必要なことを知っている。
    - `Mechanic`にお願いすると`bicycle`を準備してくれることを知っている。
- `Trip`が常に`Mechanic`を「持つ」関係になっている。
    - `Trip`を再利用するためには`Mechanic`が必須の関係になっている。
        - 実質2つのクラスは1つのクラスとして振る舞っている。
``` plantuml
@startuml
Trip -> Trip : bicycles
note over Trip: for each bicycle
Trip -> Mechanic: prepare_bicycle(bike)
activate Mechanic
Mechanic -> Mechanic: clean_bicycle(bike)
Mechanic -> Mechanic: pump_tires(bike)
Mechanic -> Mechanic: lube_chain(bike)
Mechanic -> Mechanic: check_brakes(bike)
Mechanic --> Trip
deactivate Mechanic
@enduml
```

### Third Step
- `Trip`は自身の準備を`Mechanic`に任せる。`prepare_bicycle()`を使わない
    - `Trip`は準備をお願いするときに`bicycles`が必要なことを知らない。(this step)
    - `Trip`は`Mechanic`が「どのように準備するか」を知らない。(Second Step)
- `Mechanic`は`Trip`が持つ`bicycles`を要求する。
- `Mechanic`はすべてを準備したら`Trip`にレスポンスを返す。
``` plantuml
@startuml
Trip -> Mechanic: prepare_trip(self)
activate Mechanic
Mechanic -> Trip: bicycle
deactivate Mechanic
activate Trip
Trip --> Mechanic
deactivate Trip
activate Mechanic
note over Mechanic: for each bicycle
Mechanic -> Mechanic: prepare_bicycle(bike)
Mechanic --> Trip
deactivate Mechanic
@enduml
```


