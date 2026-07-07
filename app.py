from flask import Flask, render_template
import json 

app = Flask(__name__)

@app.route('/art/<int:art_id>')
def art_detail(art_id):
    # 1. 누군가 접속할 때마다 data.json 파일을 열어서 데이터를 읽어옵니다.
    with open('data.json', 'r', encoding='utf-8') as f:
        art_data = json.load(f)
        
    # 2. 주소창으로 들어온 숫자(예: 1)를 JSON의 이름표 모양(문자열 "1")으로 맞춰줍니다.
    str_id = str(art_id)

    # 3. 데이터가 존재하면 HTML에 꽂아주고, 없으면 에러를 냅니다.
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
    app.run(host='0.0.0.0', port=5000, debug=True)