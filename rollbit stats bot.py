print("Rember to do pip install websocket_client")
import websocket #pip install websocket_client
import json
from colorama import Back, Fore, Style, deinit, init

results = {}
rounds = 0
de = 0
ci = 0
un = 0
di = 0
ce = 0
uns = 0
greentrain = 0
greytrain = 0
greytrains = []
greentrains = []
resultss = []
bet = 0
bets = []
win= {}
profit = 0
profit3 = 0
b = 0
multis = []
players = []
maxwager = []
maxswager = []
rounde = 0
players = []
messages = 0
loose = 0
nome = 0
y = 0
loose2 = 0
result = 0
profit2 = 0
multiwin = []
multiswin = []
ping = input("Do you want to show online player stats (Yes / No) ")
roundes = input("Do you want to show round stat (Yes / No) ")
if roundes == "Yes":
    roundes_info = input("What do you want to see (Multi/Train/Bet) you can choose multiple choice ")
    maxround = input("How many round you wanna wait before showing result ")
    reset = input("Do you want to reset every X round? (Yes / No) ")
userinfo = input("Do you want to show user info stats (Yes / No) ")
if userinfo == "Yes":
    name = input("Choose user you want to snipe ")
    messages2 = input("Do you want to know how many message u sent (Yes / No) ")



def on_message(ws, message):
    global de, ci, di, un, uns, ce, greentrain, greytrain, bet,bets,results,resultss,greentrains,b, profit,maxwager,rounde,messages,loose,name, nome, maxwager,multis,multiswin,multiwin,maxswager, players,greytrains, a, loose2,profit2,profit3,result
    global rounds,y
    test = json.loads(message)
    event = test[0]
    payload = test[1]
    if roundes.lower() == "yes":
        if '["x-roulette-wagers",' in message:
            result = payload['amount']
            multi = payload['multiplier']
            result = result / 100
            multi = multi/100
            multis.append(multi)
            maxwager.append(result)
            maxswager.append(result)
            bet = int(bet) + 1

        if '["x-roulette",{"x' in message:
            rounds = rounds + 1
            rounde = rounde + 1
            print(Fore.MAGENTA + "rounds : " + str(rounde))
            #bet info
            bets.append(bet)
            bet = 0
            result = payload['result']
            if result not in results:
                results[result] = 1
                resultss.append(result)
            else:
                results[result] = results[result] + 1

            for i in range(0,len(multis)):
                if float(multis[i]) <= float(result):
                    profit =  profit + multis[i] * maxswager[i]
                    profit2 = profit2 + multis[i] * maxswager[i]
                    multiswin.append(multis[i])
                else:
                    loose2 = loose2 + maxswager[i]
                    loose = loose + maxswager[i]
            #Multi info
            if result >= 100:
                ce = ce + 1
                de = de + 1
                ci = ci + 1
                di = di + 1
            elif result >= 50:
                ci = ci + 1
                di = di + 1
                de = de + 1
            elif result >= 10:
                di = di + 1
                de = de + 1
            elif result >= 2:
                de = de + 1
            #train info
            if result < 2:
                if greentrain > 2:
                    greentrains.append(greentrain)
                greentrain = 0
                greytrain = greytrain + 1
                un = un + 1
                if result == 1:
                    uns = uns + 1
            else:
                if greytrain > 2:
                    greytrains.append(greytrain)
                greytrain = 0
                greentrain = greentrain + 1

        if int(rounds) == int(maxround):
            rounds = 0
            if "Multi" in roundes_info:
                print(Fore.BLUE + Style.DIM + "\n" + "\n" + "Multi info")
                print(Style.NORMAL + "Number of 1.99 or - : " + str(un))
                print("Number of 2 or + : " + str(de))
                print("Number of 10 or + : " + str(di))
                print("Number of 50 or + : " + str(ci))
                print("Number of 100 or + : " + str(ce))
                print("Number of 1 : " + str(uns))
                print("Max multi fall : " + str(max(resultss)))
                print("Multi fall : " + str(result))
            if "Train" in roundes_info:
                print(Fore.CYAN + Style.DIM + "\n" + "\n" + "Train info")
                if len(greentrains) > 0:
                    print("Number of greentrain(3 green or + ) : " + Fore.GREEN + Style.BRIGHT + str(len(greentrains)))
                    print(Style.NORMAL + "Longest green train : " + Fore.GREEN + Style.BRIGHT + str(max(greentrains)))
                    if len(greytrains) > 0:
                        print(Style.NORMAL + "Number of greytrain(3 grey or + ) : " + Fore.RED + Style.BRIGHT + str(len(greytrains)))
                        print(Fore.GREEN + Style.NORMAL + "Longest greytrain : " +  Fore.RED + Style.BRIGHT + str(max(greytrains)))
                else:
                    print("There wasnt any train")
            if "Bet" in roundes_info:
                print(Fore.RED + Style.NORMAL + "\n" + "\n" + "Bet info")
                print("Number of bet in total : " + str(len(maxwager)))
                print("Max number of bet in a round : " + str(max(bets)))
                print("Number of bet during this round : " + str(len(maxswager)))
                print("Total waggered of all player : " + str(round(sum(maxwager))))
                print("Round waggger of all player : " + str(round(sum(maxswager))))
                print("Max bet in the round : " + str(max(maxswager)))
                print("Max bet in totals : " + str(max(maxwager)))
                print("Max multi hitted : " + str(max(multiswin)))
                print("Min multi hitted : " + str(min(multiwin)))
                print("Total profit : " + str(round(profit)))
                print("Total Loose : " + str(round(loose)))
                print("Round profit : " + str(round(profit2)))
                print("Round loose : " + str(round(loose2)))
                maxswager = []
                multis = []
                multiwin = []
                profit2 = 0
                loose2 = 0
            if reset == 1:
                print(Fore.RED + Style.BRIGHT + "reseting")
                results = {}
                rounds = 0
                de = 0
                ci = 0
                un = 0
                di = 0
                ce = 0
                uns = 0
                greentrain = 0
                greytrain = 0
                greytrains = []
                greentrains = []
                resultss = []
                bet = 0
                bets = []
                win = {}
                profit = 0
                b = 0
                multis = []
                players = []
                maxwager = []
                maxswager = []
                rounde = 0
                players = []
                messages = 0
                loose = 0
                nome = 0
                y = 0
                multiwin = []
                multiswin = []
                loose2 = 0
                profit2 = 0
    if userinfo.lower() == 'yes':
        if name in message:
            if messages2.lower() == "yes":
                if '["chat",' in message:
                    messages = messages + 1
                    print(Fore.LIGHTRED_EX + "Current message count : " + Style.BRIGHT + str(messages))
            nome = 1
            if '["x-roulette-wagers",' in message:
                amount = payload['amount']
                multi = payload['multiplier']
                amount = amount/ 100
                multi = multi / 100
                multis.append(multi)
                maxwager.append(amount)
                maxswager.append(amount)
                bet = bet + 1

        if nome == 1:
            if '["x-roulette",{"x' in message:
                rounds = rounds + 1
                rounde = rounde + 1
                print(Fore.MAGENTA + Style.NORMAL + "rounds : " + str(rounde))
                result = payload['result']
                for i in range(0,len(multis)):
                    if float(multis[i]) <= float(result):
                        profit = profit + multis[i] * maxwager[i]
                        multiwin.append(multis[i])
                        multiswin.append(multis[i])
                    else:
                        loose = loose + maxwager[i]
                profit3 = profit -sum(maxswager)
                print(Fore.YELLOW +"Stats of : " + name)
                print(Fore.YELLOW + "You waggered a total of : " + Fore.RED + Style.BRIGHT  + str(sum(maxswager)))
                print(Fore.YELLOW + "You waggered this round : " + Fore.RED + Style.BRIGHT  + str(sum(maxwager)))
                print(Fore.YELLOW + "You won a total of : " + Fore.LIGHTGREEN_EX + Style.BRIGHT  + str(profit))
                print(Fore.YELLOW + "And lost a total of : " + Fore.RED + Style.BRIGHT  + str(loose))
                print(Fore.YELLOW + "Profit : " + Fore.LIGHTGREEN_EX + Style.BRIGHT + str(profit3))
                print(Fore.YELLOW + "Biggest bet this round : " + Fore.RED + Style.BRIGHT + (str(max(maxwager))))
                print(Fore.YELLOW + "Lowest bet this round : " + Fore.RED + Style.BRIGHT + (str(min(maxwager))))
                print(Fore.YELLOW + "Biggest multi played : " + Fore.RED + Style.BRIGHT + (str(max(multis))))
                print(Fore.YELLOW + "Lowest multi played : " + Fore.RED + Style.BRIGHT + (str(min(multis))))
                print(Fore.YELLOW + "Multi fall : " + Fore.LIGHTGREEN_EX + Style.BRIGHT  + str(result))

                if len(multiswin) > 0:
                    print(Fore.YELLOW + "Biggest multi hitted total : " + Fore.LIGHTGREEN_EX + Style.BRIGHT + str(max(multiswin)))
                    if len(multiwin) > 0:
                        print(Fore.YELLOW + "Biggest multi hitted this round : " + Fore.LIGHTGREEN_EX + Style.BRIGHT  + str(max(multiwin)))

                nome = 0
                multis = []
                multiwin = []
                maxwager = []
    if ping.lower() == 'yes': # check if the user
        if '["ping",{"online":' in message:
                player = payload["online"]
                players.append(player)
                y = y +1
                if y == 10:
                    print(Fore.GREEN + "Current amount of player : " + str(player))
                    print(Fore.GREEN + "Max amount of player : " + str(max(players)))
                    y = 0




def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("open")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.rollbit.com/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(origin="https://www.rollbit.com")