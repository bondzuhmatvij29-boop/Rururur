from flask import Flask, request, jsonify

app = Flask(__name__)

# Змінна для збереження повідомлення в пам'яті
latest_message = "Повідомлень поки немає."
SECRET_KEY = "2026KEY#123"

@app.route('/send', methods=['POST'])
def send():
    global latest_message
    # Отримуємо дані з POST-запиту (від сайту на Neocities)
    key = request.form.get('key')
    message = request.form.get('message')

    if key == SECRET_KEY:
        latest_message = message
        return "Повідомлення успішно відправлено в додаток!"
    else:
        return "Помилка: Невірний ключ!", 403

@app.route('/get-message', methods=['GET'])
def get_message():
    # Цей шлях буде опитувати твій додаток у Sketchware
    return jsonify({"message": latest_message})

if __name__ == '__main__':
    # Запускаємо локально на телефоні через Pydroid 3
    app.run(host='0.0.0.0', port=5000, debug=True)
