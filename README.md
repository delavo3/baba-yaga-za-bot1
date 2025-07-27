# Baba Yaga ZA Bot

Telegram‑бот, отвечающий в стиле канала «Баба Яга ЗА» — резкий, честный, мудрый.

## Команды
- `/пинок` — пинок под пятку  
- `/отвар` — вечерний отвар с рефлексией  
- `/урок` — короткий урок от Яги  
- любые сообщения — ответ в стиле Бабы Яги

## Как запустить на Render
1. Форкни или импортируй этот репозиторий в GitHub.
2. Перейди на render.com, нажми **New → Web Service**, выбери репозиторий.
3. Настройки:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
   - Environment Variables:
     - `TELEGRAM_TOKEN`
     - `OPENAI_API_KEY`

## Локальный запуск
```bash
cp .env.example .env
# впиши свои токены
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```
