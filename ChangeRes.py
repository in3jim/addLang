import json

exampleLang = 'cn'; #專案一定會有cn/en，因為Image.source會出現命名為'Menu'的檔案，會使判斷錯誤，不能使用en
newLang = '';
resPath = "/Users/jianyinxuan/Desktop/addLangByPython/default.res.json"; 

def addLang(path):
    exmlRead = open(path, 'r');
    exmlWrite = open(path, 'r+');
    text = exmlRead.read();
    res = json.loads(text);
    changeRes(res['groups'], 'keys');
    changeRes(res['resources'], 'url');
    exmlWrite.write(json.dumps(res, sort_keys=True, indent=4, separators=(',', ': ')))

def changeRes(res, key): 
    groupsLength = len(res);
    endText = '';

    if(key == 'keys'):
        endText = '"}';
    else:
        endText = '_png"}';

    for index in range(groupsLength):    
        if(exampleLang in res[index][key]):
            textArr = json.dumps(res[index]).split(exampleLang);
            addGroup = '';
            for text in textArr:
                if (text != endText):
                    addGroup += text + newLang;
                else:
                    addGroup += text;  
            res.append(eval(addGroup));