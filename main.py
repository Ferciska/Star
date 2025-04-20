import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Получаем токен и chat_id из переменных окружения
BOT_TOKEN = os.getenv('API_TOKEN')  # Токен вашего бота
CHAT_ID = os.getenv('CHAT_ID')  # Ваш chat_id

# Функция для отправки сообщения в Telegram
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response

# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')

# Обработка данных формы
@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные из формы
    nickname = request.form['nickname']
    age = request.form['age']
    timezone = request.form['timezone']
    platform = request.form['platform']
    license = request.form['license']
    play_time = request.form['play_time']
    experience = request.form['experience']
    hobbies = request.form['hobbies']
    team_experience = request.form['team_experience']
    mods = request.form['mods']
    rules = request.form['rules']
    build_skills = request.form['build_skills']
    play_reason = request.form['play_reason']
    why_star_house = request.form['why_star_house']
    help_project = request.form['help_project']

    # Формируем сообщение для Telegram
    message = f"""
    1. Имя / Никнейм: {nickname}
    2. Возраст: {age}
    3. Часовой пояс / Город: {timezone}
    4. Платформа: {platform}
    5. Лицензия или пиратка: {license}
    6. Время для игры: {play_time}
    7. Опыт в Minecraft: {experience}
    8. Любимые занятия в игре: {hobbies}
    9. Опыт в командах / на серверах: {team_experience}
    10. Используешь моды / аддоны?: {mods}
    11. Соблюдаешь ли правила и уважаешь других?: {rules}
    12. Умеешь ли строить?: {build_skills}
    13. Играешь ли ты ради фана, командной игры или достижений?: {play_reason}
    14. Почему хочешь в Star House?: {why_star_house}
    15. Готов ли помочь проекту чем-то ещё?: {help_project}
    """
    
    # Отправляем сообщение в Telegram
    send_to_telegram(message)

    # Ответ пользователю
    return "Спасибо за заполнение анкеты! Мы свяжемся с вами скоро."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
