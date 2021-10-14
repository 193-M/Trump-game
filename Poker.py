class Poker:
    from Trump import Trump as trump
    def is_int(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

    def error_check(s):
        if len(s) > 5:
            message = "ハンドは5枚です。"
        elif len(s) != len(set(s)):
            message = "選択したカードが重複しています。"
        else:
            for i in s:
                if len(i) != 1:
                    message = "カンマ区切りで入力してください。"
                    break
                int_check = Poker.is_int(i)
                if int_check == False:
                    message = "0~4の数字で入力してください。"
                    break
                else:
                    if int(i) >= 5:
                        message = "0~4の数字で入力してください。"
                        break
                    else:
                        message = None
        return message

    def hand_check(hand):
        hand_num = sorted([Poker.trump().change(i[1]) for i in hand])
        hand_suit = [i[0] for i in hand]
        double_num = list(set(hand_num))
        point_num = []
        if len(set(hand_suit)) == 1:
            point = 5 #フラッシュ
            point_num = sorted(hand_num, reverse = True)
            if len(double_num) == 5 and hand_num[0] + 4 == hand_num[4]:
                point = 8 #ストレートフラッシュ
                point_num = [hand_num[4]]
                if hand_num[4] == 13:
                    point = 9 #ロイヤルストレートフラッシュ
        elif len(double_num) == 5 and hand_num[0] + 4 == hand_num[4]:
            point = 4 #ストレート
            point_num.append(hand_num[4])
        else:
            if len(double_num) == 2:
                if 2 <= hand_num.count(double_num[0]) <= 3:
                    point = 6 #フルハウス
                    if hand_num.count(double_num[0]) == 3:
                        point_num = sorted(double_num)
                    else:
                        point_num = sorted(double_num, reverse = True)
                else:
                    point = 7 #フォーカード
                    point_num.append(hand_num[1])
            elif len(double_num) == 3:
                if hand_num.count(double_num[0]) == 2 or hand_num.count(double_num[1]) == 2:
                    point = 2 #ツーペア
                    point_num.append(hand_num[1]); point_num.append(hand_num[3])
                    point_num.sort(reverse = True)
                else:
                    point = 3 #スリーカード
                    point_num.append(hand_num[2])
            elif len(double_num) == 4:
                point = 1 #ワンペア
                point_num = [num for num in double_num if hand_num.count(num) > 1]
            else:
                point = 0 #ノーペア
        return point, point_num
    
    def stfla_check(hand):
        hand_suit = [x[0] for x in hand]
        set_hand_suit = list(set(hand_suit))
        hand_num = [Poker.trump().change(i[1]) for i in hand]
        sort_hand_num = sorted(hand_num)
        flag = False
        index = None
        if len(set(hand_num)) == 5:
            if len(set_hand_suit) == 2:
                if hand_suit.count(set_hand_suit[0]) == 4 or hand_suit.count(set_hand_suit[1]) == 4:
                    flag = True
                    if hand_suit.count(set_hand_suit[0]) == 4:
                        suit = set_hand_suit[0]
                    else:
                        suit = set_hand_suit[1]
                    for i, s in enumerate(hand):
                        if s[0] != suit:
                            index = i
                            break
            else:
                if sort_hand_num[3] - sort_hand_num[0] <= 4 or sort_hand_num[4] - sort_hand_num[1] <= 4:
                    flag = True
                    if sort_hand_num[4] - sort_hand_num[1] <= 4:
                        num = sort_hand_num[0]
                    else:
                        num = sort_hand_num[4]
                    index = hand_num.index(num)
        return flag, index

    def point_to_hand(point):
        hand_list = ["ノーペア", "ワンペア", "ツーペア", "スリーカード", "ストレート", "フラッシュ", 
                    "フルハウス", "フォーカード", "ストレートフラッシュ", "ロイヤルストレートフラッシュ"]
        return hand_list[point]
    
    def calc_div(bet_money, point):
        ratio_list = [1, 1, 2, 3, 4, 5, 7, 20, 50, 100]
        div = bet_money * ratio_list[point]
        return div

    def judge(player, dealer):
        player_point, player_num = player[0], player[1]
        dealer_point, dealer_num = dealer[0], dealer[1]
        if player_point > dealer_point:
            result = "Player"
        elif player_point < dealer_point:
            result = "Dealer"
        else:
            if player_point == 0:
                result = "Draw"
            else:
                for i in range(len(player_num)):
                    if player_num[i] < dealer_num[i]:
                        result = "Dealer"
                        break
                    elif player_num[i] > dealer_num[i]:
                        result = "Player"
                        break
                    else:
                        result = "Draw"
        return result
    #メイン
    def play(self):
        deck = Poker.trump().setDeck()
        game_continue = input("それではドローポーカーを始めます。↩️")
        #手札を用意
        player_hand = []
        dealer_hand = []
        for i in range(5):
            player_hand.append(Poker.trump().draw(deck))
            dealer_hand.append(Poker.trump().draw(deck))
        print("あなたのハンドは{}です。".format([card[0] + card[1] for card in player_hand]))
        #賭け
        bet_money = input("賭け金を入力してください >>>")
        while True:
            a = Poker.is_int(bet_money)
            if a == True:
                bet_money = int(bet_money)
                break
            else:
                bet_money = input("数字で入力してください >>>")
        #手札の交換
        change = input("ハンドを交換しますか？ Yes or No >>>")
        while True:
            if change != "Yes" and change != "No":
                change = input("YesかNoで入力してください。 >>>")
            else:
                break
        if change == "Yes":
            print("一番左のカードから順番に0,1,2,3,4として、どのカードを交換しますか？")
            while True:
                change_card = input("複数枚の場合はカンマ','区切りで入力してください。>>>").split(",")
                check = Poker.error_check(change_card)
                if check != None:
                    print(check)
                else:
                    change_card = [int(i) for i in change_card]
                    break
            for i in range(len(change_card)):
                add_card = Poker.trump().draw(deck)
                game_continue = input("{}枚目は{} ↩️".format(i + 1, (add_card[0] + add_card[1])))
                player_hand[change_card[i]] = add_card
            print("あなたのハンドは{}になりました。".format([card[0] + card[1] for card in player_hand]))
        player = Poker.hand_check(player_hand)
        player_result = Poker.point_to_hand(player[0])
        game_continue = input("あなたの役は{}です。↩️".format(player_result))
        #ディーラーハンドの変更
        stfla_check_dealer = Poker.stfla_check(dealer_hand)
        dealer = Poker.hand_check(dealer_hand)
        if stfla_check_dealer[0] == True:
            dealer_hand[stfla_check_dealer[1]] = Poker.trump().draw(deck)
            count = 1
        else:
            if dealer[0] <= 3:
                dealer_hand_num = [x[1] for x in dealer_hand]
                count = 0
                for i, card in enumerate(dealer_hand_num):
                        if dealer_hand_num.count(card) == 1:
                            dealer_hand[i] = Poker.trump().draw(deck)
                            count += 1
                print("Dealerはハンドを{}枚交換しました。".format(count))
        dealer = Poker.hand_check(dealer_hand)
        dealer_result = Poker.point_to_hand(dealer[0])
        game_continue = input("Dealerのハンドは{}で、{}でした。↩️".format([card[0] + card[1] for card in dealer_hand], dealer_result))
        result = Poker.judge(player, dealer)
        if result == "Player":
            print("おめでとうございます。あなたの勝利です。")
            divident = Poker.calc_div(bet_money, player[0])
            print("配当は{}円になります。".format(divident))
        elif result == "Dealer":
            print("Dealerの勝利となりました。")
        else:
            print("引き分けとなりました。")
        print("またの挑戦をお待ちしております。")

# game = Poker()
# game.play()