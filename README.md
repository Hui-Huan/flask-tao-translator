# Flask Tao Translator

## 簡介
Flask Tao Translator 是一個利用 Flask 框架構建的簡單翻譯工具，可以將達悟語翻譯為中文。此應用整合了 NLP 模型，實現準確的語言翻譯。

## 功能
- 翻譯達悟語到中文
- 提供一個簡單的前端達悟語到中文翻譯查詢用戶界面進行輸入和查看結果

## 部署
您可以使用 Heroku 或 Render 等平台來部署應用，詳細步驟請參考專案文檔。

## 目錄結構
flask-tao-translator/
1. app.py              # Flask 應用主文件
2. templates/          # HTML 文件
3. index.html         # 前端模板
4. trained-model        # 存放訓練好的 NLP 模型文件
- config.json         # 模型的配置文件
- pytorch_model.bin   # 訓練好的模型權重
- vocab.json          # 模型的詞彙表
5. static/               # 靜態文件（圖片、CSS 等）
6. requirements.txt    # 依賴項列表
7. README.md           # 專案簡介
