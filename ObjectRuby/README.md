# オブジェクト指向設計実践ガイド
オブジェクト指向設計実践ガイドをPythonで実践する。

## メモ
基本的なメモはKindleに記載している。

### オブジェクト指向
- 継承とは、メッセージの**自動委譲**の仕組みである
- クラスの定義で重要なことは、**メソッド(メッセージ)** である。
- シーケンス図を使うことでクラスの役割(メソッド)を明確にできる。
    - **誰が**、**誰に**、**何を**伝えるのか？
        - 誰に**何の責任**があるかがわかる。
- オブジェクト指向プログラミングとは**依存関係を管理**する設計である。
    - オブジェクト指向の3要素
        1. カプセル化:知識の範囲を限定したり隠蔽することで不要な依存を減らす。
        2. 継承:メッセージの委譲を自動化して、カプセル化を効果的に使う。
        3. ポリモーフィズム:メッセージに依存した関係を作る。
    - SOLIDの原則
        1. 単一責任の原則:クラスを1つの目的に集中させてクラス内の依存をシンプルにする
        2. オープン・クローズドの原則:抽象に依存することで既存処理に依存しないで新規処理を作る
        3. リスコフの置換原則:抽象を適切に行うことでポリモーフィズムを正しく扱う
        4. インターフェース分離の原則:使わない機能への依存を作らない
        5. 依存性逆転の原則:抽象(安定した概念)に依存することで、具体的な処理に依存しないようにする。
    - デメテルの法則
        1. 他のクラスにアクセスするためにクラスを経由しない。
        2. シンプルで最短の依存関係を目指す。
        3. 不要なカプセル化はしない。自分のことは自分で実行する。


### テスト
#### テストの**意図**を説明できることが良いテストを作る第一段階
- バグを見つける
- 仕様書となる
- 設計の決定を遅らせる
- 抽象を支える
- 設計の欠陥を明らかにする
- 何をテストするかを知る
    - オブジェクトをメッセージと考えてテストを行う
    - 相手の内部構造などを気にしない設計にする
- いつテストをするかを知る
- テストの方法を知る

#### テストの種類
- 受信と送信の考え方
    - 受信メッセージのテスト。すべてを実施する必要がある。
        - 自分自身が定義するメソッドのテスト
        - 戻り値の状態がテストされるべき
    - 送信メッセージのテスト。一部のみ実施する必要がある。
        - 他のオブジェクトが定義するメソッドのテスト  
        -> 他のオブジェクトの受信メッセージとして基本的にはテストする。
        - 送信する側がテストする必要があるメソッド
            - コマンド（命令）のメソッド。副作用の有るメソッド。  
            -> メッセージを適切に送信したことを保証する必要がある。
                - メッセージの送信にMockを使うことでメッセージの処理内容に依存していないことが確認できる。
        - 送信する側でテストする必要の無いメソッド。
            - クエリ（質問）のメソッド。副作用の無いメソッド。  
            -> 送られたメッセージに対して応答するだけなので、受信ですらメッセージが送られたことを気にしない。

- 状態と振る舞いの考え方
    - 同じメソッドが、`状態のテスト`, `振る舞いのテスト`の対象になることを有る。
    - 状態のテスト
        - 受信側でテストする。
            - メソッドの戻り値を表明するテスト

    - 振る舞いのテスト
        - 送信側でテストする。
            - メソッドを**いつ**、**何回**、**どの引数**、で行ったかのテスト
- テストの対象：図
    ``` plantuml
    @startuml
    class SUT {
        + methodA()
        - methodB()
    }

    class B {
        + query()
        + command()
    }

    A --> SUT #text:blue :○テスト対象\nSUTは受信側\nmethodA()
    SUT -> B #text:red :✗テスト対象外\nSUTは送信側\nquery()
    SUT -> B #text:blue :○テスト対象\nSUTは送信側\ncommand()
    note left of SUT::"methodB()" 
        <color:red>✗テスト対象外</color>
        <color:red>プライベートメソッド</color>
    end note
    @enduml
    ```

#### テストの焦点と視点
- 焦点
    - `テスト対象オブジェクト`か`それ以外`  
    -> `テスト対象オブジェクト`のみに焦点を当てる。
- 視点
    - `テスト対象オブジェクト`の縁に立つ。  
    -> パブリックな情報のみを頼りにテスト行う。プライベートな情報はテストとの密結合を生み出す
- テストの焦点と視点:図

    ``` plantuml
    @startuml
    class SUT {
        methodA() 
    }

    class B {
        query()
        command()
    }

    A -> SUT
    SUT *-- publicMethodA
    SUT *-- privateMethodB
    SUT -> B

    note top of A : <color:red>✗焦点を当てない</color>
    note top of B : <color:red>✗焦点を当てない</color>
    note right of privateMethodB : <color:red>✗視点に入れない</color>

    note top of SUT : <color:blue>○焦点を当てる</color>
    note left of publicMethodA : <color:blue>○視点に入れる</color>
    
    @enduml
    ```

#### ユニットテストの注意点
1. テストコード上にテスト対象オブジェクト以外のオブジェクトの生成がなくても、`テスト対象オブジェクト`内でオブジェクト生成が有る場合は注意する。 
    - 解決策：`テスト対象オブジェクト`が生成する`オブジェクト`は基本的に**依存性の注入**を使用する。
    - 効果
        1. 依存関係をテストコードから把握できる。
        2. ダック・タイピングに対応している場合に`クラス`依存から`メソッド`依存に切り替えられる。
    - 図:アンチパターン

        ``` plantuml
        @startuml
        class Gear {}
        Test -> Gear : テスト
        Gear .-> Wheel : 生成
        note bottom of Gear : Wheelを生成している。\nTestコードからは`Gear`と`Wheel`の依存関係が見えない
        @enduml
        ```



    - 図:変更後

        ``` plantuml
        @startuml
        class Gear {}
        Test -> Gear : `Wheel`を渡してテストする
        Test --> Wheel : 生成
        Gear --> Wheel : 使う

        note right of Gear : `Wheel`を依存性の注入で取得する。\n依存関係がTestコードから見える
        note top of Gear : `Wheel`クラスへの依存ではなく\n`diameter`メソッドへの依存になる。
        @enduml
        ```

2. 具象クラス同士を結合したテストは、実行コストが低い場合は効果的だが、抽象クラス（ロール）を使うほうが良い
    - `テストダブル`を作成して、具象クラスではなく抽象クラスに対して動作を確認する。
        - <span style="color:red">**Mockではない！！**</span>
    - `抽象クラス（ロール）`に依存していることが理解しやすくなる。
    - `Wheel`クラスを使わずにテストができる。
    - <span style="color:red">課題：`Wheel`クラスのインターフェースが変わっても`Gear`クラスを修正しなくてもテストが通ってしまう。</span>

    - 図:アンチパターン

        ``` plantuml
        @startuml
        class Wheel { 
            diameter()
        }
        Test -> Gear : `Wheel`を渡してテストする
        Test --> Wheel : 生成
        Gear --> Wheel : 使う

        note right of Gear : 具象(`Wheel`)クラスを使ってテストをする
        note top of Test : 具象(`Wheel`)クラスを生成している。
        @enduml
        ```
    - 図:変更後

        ``` plantuml
        @startuml
        class DiameterDouble {
            diameter()
        }

        interface IDiameterable {}
        Test -> Gear : `DimaeterDouble`を渡してテストする
        Test --> DiameterDouble : 生成
        Gear -->  IDiameterable : 使う
        DiameterDouble -|> IDiameterable

        note right of Gear : 抽象(`Diameterable`)クラスを使ってテストをする
        note top of Test : 抽象(`Diameterable`)クラスを生成している。
        @enduml
        ```

## まとめ

## 参考図書
- [オブジェクト指向設計実践ガイド](https://www.amazon.co.jp/オブジェクト指向設計実践ガイド-～Rubyでわかる-進化しつづける柔軟なアプリケーションの育て方-Sandi-Metz-ebook/dp/B01L8SEVYI/ref=sr_1_1?adgrpid=60166663624&gclid=CjwKCAiA76-dBhByEiwAA0_s9T8Doy6X60kftt7nd5F06Etw_4_PZHiYQYfRsmetbgNhcWkpD7DmNBoCkGsQAvD_BwE&hvadid=618622324444&hvdev=c&hvlocphy=1009285&hvnetw=g&hvqmt=e&hvrand=10463125238993718055&hvtargid=kwd-536214242527&hydadcr=27266_14598084&jp-ad-ap=0&keywords=オブジェクト指向実践ガイド&qid=1672217521&sr=8-1)
