exampleLang = 'cn'; #專案一定會有cn/en，因為Image.source會出現命名為'Menu'的檔案，會使判斷錯誤，不能使用en
exampleSource = 'source.' + exampleLang;
exampleX = 'x.' + exampleLang;
exampleStates = ',' + exampleLang;
exampleText = 'text.' + exampleLang;
exampleTextArr = [
    'JP大奖',
    'JP巨奖',
    'JP中奖',
    '加速',
    '是否开启加速？',
    '点击以开始免费游戏',
    '线数 :',
    '转轮数 :',
    '资料下载…'
];

newLang = '';
newTextArr = [];

def buildNewLine(strArr):
    line = '';    
    for str in strArr:
        if (exampleSource in str):
            b = str.split("=");
            c = b[1].split(exampleLang);
            d = c[0] + newLang + c[1];
            e = 'source.' + newLang + '=' + d;
            line += str + ' ' + e + ' ';
        elif (exampleX in str):
            b = str.split("=");
            c = 'x.' + newLang + '=' + b[1];
            line += str + ' ' + c + ' ';
        elif (exampleStates in str):
            b = str.split(exampleStates);
            c = exampleStates + ',' + newLang;
            line += b[0] + c + b[1];
        elif (exampleText in str):
            b = str.split("=");
            c = b[1].split('"');
            i = exampleTextArr.index(c[1]);
            d = 'text.' + newLang + '="' + newTextArr[i] + '"';
            line += str + ' ' + d + ' ';
        else:
            line += str + ' ';  

    return line;     

def addLang(path):
    exmlRead = open(path, 'r');
    exmlWrite = open(path, 'r+');
    for line in exmlRead:
        if (exampleSource in line or exampleX in line or exampleStates in line or exampleText in line):
            strArr = line.split(" ");
            newLine = buildNewLine(strArr);
            exmlWrite.write(newLine);   
        else:
            exmlWrite.write(line);         
