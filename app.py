from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import MarianMTModel, MarianTokenizer
import os

app = Flask(__name__)
CORS(app)

# 禁用全局 JSON 編碼中的 ASCII，確保返回可讀的中文
app.config['JSON_AS_ASCII'] = False

# 模型的路徑
MODEL_PATH = os.path.abspath("./trained-model/")
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"模型目錄不存在：{MODEL_PATH}")

# 嘗試載入模型和分詞器
try:
    tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
    model = MarianMTModel.from_pretrained(MODEL_PATH)
    print("模型和分詞器載入成功！")
except Exception as e:
    raise RuntimeError(f"模型載入失敗：{str(e)}")

# 根路由，提供主頁模板
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 接收表單提交的數據
        tao_sentence = request.form.get("tao_sentence", "").strip()

        if not tao_sentence:
            # 如果沒有輸入，返回錯誤消息
            return render_template("index.html", error="請提供有效的達悟語文本")

        try:
            # 使用模型進行翻譯
            inputs = tokenizer(tao_sentence, return_tensors="pt", truncation=True, max_length=128)
            outputs = model.generate(inputs.input_ids, max_length=128, num_beams=5, early_stopping=True)
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # 渲染結果到模板
            return render_template("index.html", translation=translation, tao_sentence=tao_sentence)

        except Exception as e:
            # 返回錯誤信息
            return render_template("index.html", error=str(e))

    # 如果是 GET 請求，渲染空表單
    return render_template("index.html")
# 主程序入口
if __name__ == "__main__":
    app.run(debug=True, port=3000)

