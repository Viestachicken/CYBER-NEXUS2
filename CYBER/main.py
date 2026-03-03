import requests
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# Ambil dari Environment Variables (Lebih Aman)
HF_TOKEN = os.getenv("HF_TOKEN", "")

# MODEL PALING CANGGIH: DeepSeek-Coder-V2 (Spesialis Hacking & Complex Coding)
MODEL_ID = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"

# JALUR ROUTER TERBARU (ANTI-NEMPEL)
API_URL = f"https://router.huggingface.co{MODEL_ID}"

@app.route('/')
def index():
    return "<h1>Nexus Cyber-Core Online</h1><p>Send POST requests to /chat</p>"

    @app.route('/chat', methods=['POST'])
    def chat():
        user_message = request.json.get("message")
            if not user_message:
                    return jsonify({"message": {"content": "Target belum ditentukan, Bre."}})

                        headers = {
                                "Authorization": f"Bearer {HF_TOKEN.strip()}",
                                        "Content-Type": "application/json"
                                            }
                                                
                                
                                                   # Prompt 'Black-Hat' Assistant Style (Untuk Edukasi Keamanan)
                                                        payload = {
                                                                "inputs": f"Instruction: You are an elite cybersecurity expert. Provide deep technical analysis, exploit explanations, and advanced code. Language: Indonesian.\nUser: {user_message}\nAssistant:",
                                                                        "parameters": {
                                                                                    "max_new_tokens": 1024,
                                                                                                "temperature": 0.3, # Lebih rendah agar lebih presisi/akurat
                                                                                                            "top_p": 0.95,
                                                                                                                        "return_full_text": False
                                                                                                                                }
                                                                                                                                    }

                                                                                                                                        try:
                                                                                                                                                response = requests.post(API_URL, headers=headers, json=payload, timeout=90)
                                                                                                                                                        
                                                                                                                                                                if response.status_code == 503:
                                                                                                                                                                            return jsonify({"message": {"content": "Sistem sedang 'warming up'... Coba lagi dalam 30 detik."}})
                                                                                                                                                                                    
                                                                                                                                                                                            if response.status_code != 200:
                                                                                                                                                                                                        return jsonify({"message": {"content": f"Breach Failed (Error {response.status_code}): {response.text}"}})

                                                                                                                                                                                                                result = response.json()
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                if isinstance(result, list) and len(result) > 0:
                                                                                                                                                                                                                                            bot_reply = result[0].get('generated_text', "Data korup.")
                                                                                                                                                                                                                                                    elif isinstance(result, dict):
                                                                                                                                                                                                                                                                bot_reply = result.get('generated_text', "Format data tidak dikenal.")
                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                    bot_reply = "Respon server enkripsi tidak terbaca."

                                                                                                                                                                                                                                                                                        except Exception as e:
                                                                                                                                                                                                                                                                                                bot_reply = f"System Crash: {str(e)}"

                                                                                                                                                                                                                                                                                                    return jsonify({"message": {"content": bot_reply.strip()}})

                                                                                                                                                                                                                                                                                                    if __name__ == '__main__':
                                                                                                                                                                                                                                                                                                        # Gunakan port dari environment (Standar Koyeb/Render)
                                                                                                                                                                                                                                                                                                            port = int(os.environ.get("PORT", 5000))
                                                                                                                                                                                                                                                                                                                app.run(host='0.0.0.0', port=port)
                                                                                                                                                                                                                                                                                                                