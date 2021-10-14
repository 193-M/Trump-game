from Trump import Trump
class BlackJack(Trump):
    def is_int(self, n):
            try:
                int(n)
                return True
            except ValueError:
                return False
    #絵札の数値変換
    def value_change(self, value):
        if value == "J" or value == "Q" or value == "K":
            number = 10
        elif value == "A":
            number = 1
        else:
            number = int(value)
        return number
    #手札の計算
    def calc_hand(self, value):
        int_value = [BlackJack().value_change(val) for val in value]
        sum_value = sum(int_value)
        if "A" in value:
            if sum_value <= 11:
                sum_value += 10
        return sum_value
    #プレイヤーの操作
    def player_play(self, hand):
        count = 0
        burst = False; BJ = False
        while True:
            hand_value = [card[1] for card in hand]
            player_calc = BlackJack().calc_hand(hand_value)
            print("あなたのハンドは{}で、合計は{}です。".format([card[0] + card[1] for card in hand], player_calc))
            if player_calc == 21:
                if count == 0:
                    game_continue = input("ブラックジャック！↩️")
                    BJ = True
                break
            elif player_calc > 21:
                game_continue = input("バースト！ ↩️")
                burst = True
                break
            else:
                change = input("ヒット or スタンド >>>")
                while True:
                    if change != "ヒット" and change != "スタンド":
                        change = input("ヒットかスタンドで入力してください。>>>")
                    else:
                        break
                if change == "スタンド":
                    break
                else:
                    count += 1
                    add_card = BlackJack().draw(BlackJack().deck)
                    print("引いたカードは{}でした。".format([add_card[0] + add_card[1]]))
                    hand.append(add_card)
        return hand, player_calc, burst, BJ
    #ディーラーの操作
    def dealer_play(self, hand, p_burst):
        count = 0
        burst = False; BJ = False
        game_continue = input("ディーラーの二枚目は{}でした。↩️".format([hand[1][0] + hand[1][1]]))
        if p_burst == True:
            hand_calc = BlackJack().calc_hand([card[1] for card in hand])
            if hand_calc == 21:
                BJ = True
                game_continue = input("ブラックジャック ↩️")
        else:
            while True:
                hand_value = [card[1] for card in hand]
                hand_calc = BlackJack().calc_hand(hand_value)
                print("ディーラーの合計は{}".format(hand_calc))
                if hand_calc > 21:
                    burst = True
                    game_continue = input("バースト！↩️")
                    break
                if hand_calc == 21:
                    if count == 0:
                        BJ = True
                        game_continue = input("ブラックジャック ↩️")
                    break
                elif hand_calc >= 17:
                    break
                else:
                    game_continue = input("ディーラーがドローします。↩️")
                    add_card = BlackJack().draw(BlackJack().deck)
                    print("ディーラーの引いたカードは{}".format([add_card[0] + add_card[1]]))
                    hand.append(add_card)
                    count += 1
        return hand, hand_calc, burst, BJ
    #判定
    def judge(self, player_hand, dealer_hand):
        player_hand, player_calc, p_burst, p_BJ = BlackJack().player_play(player_hand)
        dealer_hand, dealer_calc, d_burst, d_BJ = BlackJack().dealer_play(dealer_hand, p_burst)
        if p_burst == True or p_BJ == True or d_burst == True or d_BJ == True:
            if p_BJ == True or d_BJ == True:
                if p_BJ == True:
                    if d_BJ == True:
                        result = "Draw"
                    else:
                        result = "Player"
                else:
                    if d_BJ == True:
                        result = "Dealer"
            else:
                if p_burst == True:
                    result = "Dealer"
                elif d_burst == True:
                    result = "Player"
        else:
            if player_calc > dealer_calc:
                result = "Player"
            elif player_calc < dealer_calc:
                result = "Dealer"
            else:
                result = "Draw"
        return result, p_BJ
    #メイン
    def play(self):
        game_continue = input("それではブラックジャックを始めます。↩️")
        deck = BlackJack().setDeck()
        player_hand = []
        dealer_hand = []
        for i in range(2):
            player_hand.append(BlackJack().draw(deck))
            dealer_hand.append(BlackJack().draw(deck))
        #賭け
        bet_money = input("賭け金を入力してください >>>")
        while True:
            a = BlackJack().is_int(bet_money)
            if a == True:
                bet_money = int(bet_money)
                break
            else:
                bet_money = input("数字で入力してください >>>")
        print("ディーラーの一枚目は{}".format([dealer_hand[0][0] + dealer_hand[0][1]]))        
        result, p_BJ = BlackJack().judge(player_hand, dealer_hand)
        if result == "Dealer" or result == "Draw":
            if result == "Dealer":
                game_continue = input("ディーラーの勝利となりました。↩️")
            else:
                game_continue = input("引き分けとなりました。↩️")
        else:
            game_continue = input("あなたの勝利です。↩️")
            if p_BJ == True:
                div = int(bet_money * 2.5)
            else:
                div = bet_money * 2
            game_continue = input("配当は{}円になります。".format(div))
        print("またの挑戦をお待ちしております。")
            
game = BlackJack()
game.play()