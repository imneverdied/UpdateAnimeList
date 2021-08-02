import os
FULL_LIST = []  # 初始清單
DIR_LIST = []   # 資料夾清單
PATH_LIST = []  # 完整路徑清單


def outTXT(PATH, list):  # 產TXT函數
    f = open(PATH, 'a')
    for index in range(len(list)):
        if list[index] != '':
            f.write(list[index]+'\n')
    f.close()
    print('產出 ' + PATH)


資料夾清單 = r"資料夾清單.txt"
資料夾路徑清單 = r"資料夾路徑清單.txt"
最新動畫json = r"最新動畫.json"
try:
    os.remove(資料夾清單)
    os.remove(資料夾路徑清單)
    os.remove(最新動畫json)
except OSError as e:
    print(e)
else:
    print("已刪除 "+資料夾清單 + " "+資料夾路徑清單 + " "+最新動畫json)


# 讀來源
path = '動畫清單S.txt'
f = open('動畫清單.txt', 'r')
words = f.read()
f.close()

FULL_LIST = words.split('\n')

# 資料夾清單處理
for index in range(len(FULL_LIST)):
    # 把F:\aniGamerPlus_v22.3\bangumi\刪除
    temp = FULL_LIST[index].replace('F:\\aniGamerPlus_v22.3\\bangumi\\', '')
    if '\\' in temp:
        PATH_LIST.append(temp)
    else:
        DIR_LIST.append(temp)

outTXT('資料夾清單.txt', DIR_LIST)  # 產出資料夾清單.txt
outTXT('資料夾路徑清單.txt', PATH_LIST)  # 產出資料夾路徑清單.txt

PPPP = ""
# 讀來源
path = '資料夾路徑清單.txt'
f = open('資料夾路徑清單.txt', 'r')
words = f.read()
FULL_LIST = words.split('\n')
f.close()
PATH_LIST_F = []

PATH_LIST_F = FULL_LIST[0].split('\\')
PPPP = PATH_LIST_F[0]
TEMP_INDEX = 0
for index in range(len(FULL_LIST)):
    PATH_LIST_F = FULL_LIST[index].split('\\')

    if PATH_LIST_F[0] in PPPP:  # 排除重複名子
        ZZZ = 0  # 無作用
    else:
        EPISODE = index - TEMP_INDEX
        TEMP_INDEX = index
        PPPP = PPPP + "," + str(EPISODE) + "|" + PATH_LIST_F[0]
# 補最後一部級數
EPISODE = len(FULL_LIST)-1 - TEMP_INDEX
PPPP = PPPP + "," + str(EPISODE)

# print(PPPP)

config_L = []
config_L = PPPP.split('|')

# 產出最新動畫.json
f = open('最新動畫.json', 'a', encoding = "UTF-8")
f.write('[')  # json開頭

for index in range(len(config_L)):

    NAME_EP = []
    NAME_EP = config_L[index].split(',')
    f.write('{\n')
    f.write('"NAME":"' + NAME_EP[0] + '",\n')
    f.write('"RNAME":"' + NAME_EP[0] + '",\n')
    f.write('"NBRTYPE":"[1]",\n')
    f.write('"PATH":"/bangumi/'+NAME_EP[0]+'/",\n')
    f.write('"SEASON":"",\n')
    f.write('"EPISODE":"' + NAME_EP[1] + '",\n')
    f.write('"EXT":"mp4",\n')
    f.write('"CC":"0"\n')
    if index == (len(config_L)-1):
        f.write('}')
    else:
        f.write('},')


f.write(']')  # json結尾
f.close()
print('產出 最新動畫.json')
