class Baccarat:
    from Trump import Trump as trump
    def is_int(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def change(value):
        if value == "A":
            number = 1
        elif value == "J":
            number = 0
        elif value == "Q":
            number = 0
        elif value == "K":
            number = 0
        else:
            number = int(value)
        return number

    def sum_hand_first(hand):
        hand_sum = 0
        for card in hand:
            number = Baccarat.change(card[1])
            hand_sum += number
            hand_first = int(str(hand_sum)[-1])
        return hand_first

    def judge(player_hand_first, banker_hand_first):
        if player_hand_first == banker_hand_first:
            result = "Draw"
        elif player_hand_first > banker_hand_first:
            result = "Player"
        elif player_hand_first < banker_hand_first:
            result = "Banker"
        return result

    def calc_divident(bet_money, result):
        if result == "Player":
            bet_money *= 2
        elif result == "Banker":
            bet_money *= 1.95
        else:
            bet_money *= 9
        return int(bet_money)

    def play(self):
        #playerかbankerに賭ける
        print("それではバカラを開始します。")
        bet_chara = input("PlayerとBankerとDrawのどれに賭けますか >>>")
        if bet_chara != "Player" and bet_chara != "Banker" and bet_chara != "Draw":
            while True:
                bet_chara = input("PlayerかBankerかDrawのいずれかで入力してください。>>>")
                if bet_chara != "Player" and bet_chara != "Banker" and bet_chara != "Draw":
                    continue
                else:
                    break
        #賭け金設定
        bet_money = input("賭け金を入力してください >>>")
        while True:
            a = Baccarat.is_int(bet_money)
            if a == True:
                bet_money = int(bet_money)
                break
            else:
                bet_money = input("数字で入力してください >>>")
        #デッキからカードを配る 
        deck = Baccarat.trump().setDeck()
        player_hand = []
        banker_hand = []
        for i in range(2):
            player_hand.append(Baccarat.trump().draw(deck))
            banker_hand.append(Baccarat.trump().draw(deck))
        #開始時の一桁目
        player_hand_first = Baccarat.sum_hand_first(player_hand)
        banker_hand_first = Baccarat.sum_hand_first(banker_hand)
        #手札の確定
        natural = False
        print("Playerのハンドは{}、\nBankerのハンドは{}です。".format(player_hand, banker_hand))
        if player_hand_first < 8 and banker_hand_first < 8:
            #playerがドローする場合
            if player_hand_first <= 5:
                game_continue = input("Playerがドローします。エンターを押してください。")
                add = Baccarat.trump().draw(deck)
                add_num = Baccarat.change(add[1])
                print("Playerは{}をドローしました。".format(add))
                player_hand.append(add)
                player_hand_first = Baccarat.sum_hand_first(player_hand)
                #bankerのハンドとplayerのドローによって分岐
                if banker_hand_first <= 6:
                    if banker_hand_first <= 2:
                        banker_hand.append(deck.draw())
                    elif banker_hand_first == 3 and add_num != 8:
                        banker_hand.append(deck.draw())
                    elif banker_hand_first == 4 and 2 <= add_num <= 7:
                        banker_hand.append(deck.draw())
                    elif banker_hand_first == 5 and 4 <= add_num <= 7:
                        banker_hand.append(deck.draw())
                    elif banker_hand_first == 6 and 6 <= add_num <= 7:
                        banker_hand.append(deck.draw())
                    if len(banker_hand) == 3:
                        game_continue = input("Bankerがドローします。エンターを押してください。")
                        print("Bankerは{}をドローしました。".format(banker_hand[2]))
                        banker_hand_first = Baccarat.sum_hand_first(banker_hand)
            #playerがドローしない場合
            else:
                if banker_hand_first <= 5:
                    print("Playerはドローしません。")
                    banker_hand.append(Baccarat.trump().draw(deck))
                    banker_hand_first = Baccarat.sum_hand_first(banker_hand)
                    game_continue = input("Bankerがドローします。エンターを押してください。")
                    print("Bankerは{}をドローしました。".format(banker_hand[2]))
        #ナチュラルウィンの判定
        elif player_hand_first != banker_hand_first:
            natural = True
        #勝敗
        result = Baccarat.judge(player_hand_first, banker_hand_first)
        if natural == True:
                print("ナチュラルウィン！！！")
        print("Playerの手は{}、Bankerの手は{}となりましたので、".format(player_hand_first, banker_hand_first))
        if result == "Draw":
            print("結果は引き分けになります。")
        else:
            print("勝者は{}になります。".format(result))
        #結果とかけ金
        if bet_chara == result:
            divident = Baccarat.calc_divident(bet_money, result)
            print("あなたの勝利です。配当は{}円になります。".format(divident))
        else:
            print("あなたの負けです。")
        print("またの挑戦をお待ちしております。")