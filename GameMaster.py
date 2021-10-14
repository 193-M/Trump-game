class GameMaster:
    from Baccarat import Baccarat as baccarat
    from Poker import Poker as poker
    from BlackJack import BlackJack as blackjack
    def __init__(self):
        print("トランプゲームカジノへようこそ！")
        ask_play = input("ゲームをプレイしますか？ Yes or No >>>")
        if ask_play == "Yes":
            GameMaster.game_play(self)

    def game_play(self):
        print("どのカードゲームをプレイしますか？")
        number = int(input("0:バカラ, 1:ポーカー, 2:ブラックジャック >>>"))
        if number == 0:
            GameMaster.baccarat.play(self)
        elif number == 1:
            GameMaster.poker.play(self)
        elif number == 2:
            GameMaster.blackjack.play(self)


# game = GameMaster()
# game