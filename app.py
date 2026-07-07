from flask import Flask, render_template
import json 
import os 

app = Flask(__name__)

# ⭐️ [핵심 추가] app.py 파일이 있는 실제 컴퓨터 안의 '절대 주소'를 자동으로 계산합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'data.json')

@app.route('/art/<int:art_id>')
def art_detail(art_id):
    # ⭐️ 계산된 절대 주소(JSON_PATH)를 이용해 파일을 안전하게 열도록 수정했습니다.
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        art_data = json.load(f)
        
    str_id = str(art_id)

    if str_id in art_data:
        art_info = art_data[str_id]
        
        return render_template(
            'index.html', 
            title=art_info["title"], 
            explanation=art_info["explanation"], 
            audio=art_info["audio_file"],
            image=art_info["image_file"]
        )
    else:
        return "존재하지 않는 작품 번호입니다.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
