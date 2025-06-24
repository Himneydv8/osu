import requests, time, os


def get_info():
    #insert user id
    data = requests.get("https://osu.ppy.sh/users/")
    data = data.content
    
    global_rank = str(data)[650:755].split("|")[0].split("Global ")[1].replace(" ", "")
    
    country_rank = str(data)[650:790].split("|")[1].split("Country ")[1].split("\"")[0].replace(" ", "")
    return [global_rank, country_rank]






running = True
logs = []

data = get_info()
last_global = data[0]
last_country = data[1]
current = time.localtime()
current = time.strftime("%H:%M:%S", current)
print(f"[{current}] {last_global} {last_country}")
logs.append(f"[{current}] {last_global}, {last_country}")

while running == True:
    with open("stop.txt", "r") as file:
        if file.read() != "True":
            running = False
            continue
    data = get_info()
    if data[0] == last_global and data[1] == last_country:
        time.sleep(3)
    else:
        diff1 = int(last_global.replace(",", "")[1:]) - int(data[0][1:].replace(",", ""))
        diff2 = int(last_country.replace(",", "")[1:]) - int(data[1][1:].replace(",", ""))
        string = ""
        current = time.localtime()
        current = time.strftime("%H:%M:%S", current)
        string += f"[{current}] "
        string += f"{data[0]}, {data[1]} | "
        if diff1 > 0:
            string += f"+{str(diff1)}, "
        else:
            string += f"-{str(diff1)}, "
        if diff2 > 0:
            string += f"+{str(diff2)}"
        else:
            string += f"-{str(diff2)}"
        logs.append(string)
        os.system("clear")
        print("\n".join(logs))
        print("running")
        last_global = data[0]
        last_country = data[1]
    