import ChangeExml
import ChangeRes
import os

# 設定要改的專案路徑
exmlfile = "/Users/jianyinxuan/Documents/GameProject/h5-slot-Spindrift/main/resource/eui_skins";  
# 設定新的語系相關資料[對照替換]
ChangeExml.newLang = 'kor';
ChangeExml.newTextArr = [
    'JP대상',
    'JP거상',
    'JP중상',
    '가속',
    '가속을 켜시겠습니까?',
    '클릭하여 무료 게임 시작',
    '라인 :',
    '릴 수 :',
    '자료 다운로드…'
];
# 設定要改的專案路徑
resPath = "/Users/jianyinxuan/Documents/GameProject/h5-slot-Spindrift/main/resource/default.res.json"; 
ChangeRes.newLang = 'kor';


exmlPath = []; 
index = 0; 

def pathsProcess(): 
    dirs = os.listdir(exmlfile);
    # 輸出所有exml文件路徑
    for file in dirs:
        if ('sgcp' in os.path.basename(file)):
            pathA = exmlfile + '/sgcp'
            sgcp = os.listdir(pathA); 
            for sgcpfile in sgcp:
                exmlPath.append(pathA + '/' + sgcpfile); 
        elif ('.DS_Store' in os.path.basename(file)):
            continue; 
        else:
            exmlPath.append(exmlfile + '/' + file); 

def main():
    pathsProcess(); 
    for path in exmlPath:
        print(path); 
        ChangeExml.addLang(path);  
    ChangeRes.addLang(resPath); 

main()