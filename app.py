from flask import Flask, render_template
import json 
import os 

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'data.json')

@app.route('/art/<int:art_id>')
def art_detail(art_id):
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
