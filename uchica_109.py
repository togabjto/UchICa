def menu():

    #メニュー画面の文字の表示
    functions = ["乗車駅選択","チャージ機能"]
    print("【ウチダ電鉄　交通系ICカード検証システム】")
    print("\n")
    for i in range(len(functions)):
      print(str(i+1)+":"+functions[i])
    print("\n")
    print("使用する機能を入力してください(終了する場合には99を入力)")

    while True:
        try:
            select = int(input())   #数字の入力

        except ValueError:
            print("数字を入力してください") #数値が入れられなかった場合

        else:
            if select == 1:
                return(select)  

            elif select == 2:
                return(select) 

            elif select == 99:  #テスト表示
                return(select) 

            else:
                print("正しい数値を入力してください.")

def charge(balance):

        #表示用

    print("チャージ残高は"+str(balance)+"円です。")
    print("\n")
    print("1:1000円")
    print("2:2000円")
    print("3:3000円")
    print("4:4000円")
    print("5:5000円")
    print("6:6000円")
    print("7:7000円")
    print("8:8000円")
    print("9:9000円")
    print("10:10000円")
    print("\n")
    print("チャージする金額を選択してください。(キャンセルする場合には99を入力)")

    while True:
            try:
                charge = int(input())   #チャージ選択
            except ValueError:
                print("数字を入力してください。")  #数字以外が入力された場合
            else:
                if charge == 99:
                    print("チャージをキャンセルしました。") #キャンセル
                    return balance
                elif charge > 10 or charge < 1:
                    print("正しい数値を入力してください。")  #範囲外の数値が入力された場合
                else:
                    new_balance = charge*1000 + balance
                    print("チャージ残高は"+str(new_balance)+"円です。")
                    return(new_balance)

def select_station():
  stations = ["秋葉原","山梨","長野"]
  fares = [133, 4128, 7990]

  print("【乗車駅選択】")

  for i in range(len(stations)):
    print(f"{i + 1}：{stations[i]}駅まで{fares[i]}円")
  
  while True:
    try:
      print()
      print("乗車した駅を入力してください（キャンセルする場合には99を入力）")
      destination = int(input("> "))
  
      if destination == 99:
        print("駅の選択をキャンセルしました。")
        return 0

      if destination < 1:
        raise IndexError # 1未満のときエラーにする

      print(f"乗車駅は{stations[destination - 1]}駅で料金は{fares[destination - 1]}円です")
      return fares[destination - 1]
    except ValueError: # 文字を入力した時の対策
      print("駅またはキャンセルを選んでください")
    except IndexError: # 範囲外の値を入力したときの対策
      print("駅またはキャンセルを選んでください")

def pay(balance , fare):
    print(f"チャージ残高は[{balance}]円です。")
    if balance < fare:
        print("残高不足です")
        while (balance < fare):
            print("3000円自動チャージします")
            balance += 3000
            print(f"チャージ残高は{balance}円です。")
    balance -= fare
    #print(fare)# でばっく
    #print(balance)# でばっく
    print(f"精算後の残高は{balance}円です。")
    if balance < 500:
        print("残高が500 円未満のため3000 円自動チャージします")
        balance += 3000
        print(f"チャージ残高は{balance}円です。")
    return balance

def main():
    balance = 500
    while(True):
        main = menu()
        if main == 1:
            fare = select_station()
            if fare != 0:
                balance = pay(balance , fare)
            
        elif main == 2:
            balance = charge(balance)
        elif main == 99:
            print("システムを終了します")
            break
        else:
            print("正しい数値を入力してください。 ")
if __name__ == "__main__":
        main()
