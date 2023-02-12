============================= 事前注意 =============================
* 確認[default.res.json]的[groups]的[game]、[controlpanel]與[cn]有關的有加上[_cn]
    範例:
        {
            "keys": "JP_MSG_cn_png,BigWin_MSG03_FX_cn_png,...",
            "name": "game"
        },
        改為以下
        {
            "keys": "JP_MSG_cn_png,BigWin_MSG03_FX_cn_png,...",
            "name": "game_cn"
        },
* 確認[LoadingView.exml]的[LoadingBar_03_cn_png]有加上[_cn]
    範例:
        source.cn="LoadingBar_03_png"
        改為以下
        source.cn="LoadingBar_03_cn_png"
* 可以修改[ChangeExml.py]、[ChangeRes.py]範例語言，需注意是否專案有該語言
* 專案路徑是否正確
============================= 步驟說明 =============================
1. 點擊[main.py]設定專案路徑/新增語系/新增語系文字相關資料
2. 檢查[事前注意]
3. 點擊右上角播放鍵執行py (vscode)
============================= 完成檢查 =============================
* 圖片及文字對位
* 遊戲特殊玩法的文字
* [default.res.json]是否有新增到[LoadingBar_03_新語系_png]、轉向圖片、成就系統
* tw語系刪除
