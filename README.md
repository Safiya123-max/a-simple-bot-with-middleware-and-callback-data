# Telegram Bot for Andrew Huberman Protocols 🧠

An asynchronous Telegram bot designed to deliver structured Andrew Huberman scientific protocols (PDF guides) directly to users, featuring an automated channel subscription system via custom middleware.

## 🚀 Key Features
* **Grid-Based Navigation:** Organizes protocols into a clean, 2-column inline layout matching the original dashboard structure.
* **Smart Subscription Check:** Features custom Async Middleware that intercepts all requests, restricting access to PDFs until the user joins your Telegram channel.
* **Anti-Spam Verification:** Utilizes Telegram's native `show_alert` to handle non-subscribed verification clicks instantly without clogging the chat history.
* **Seamless Message Cleaning:** Automatically detects and deletes heavy PDF or image bubbles before showing the "Access Denied" screen, keeping the user interface spotless.
* **Dynamic File Delivery:** Uses `FSInputFile` and localized path mappings to automatically fetch and attach the correct document based on callback data.

## 🛠 Tech Stack
* **Language:** Python 3.11+
* **Framework:** Aiogram 3.x (Async)
* **Architecture:** Custom Async Middlewares & CallbackData Factory

## 🔧 Installation & Setup
1. Clone the repository:
```bash
git clone [https://github.com/your-username/huberman-protocols-bot.git](https://github.com/your-username/huberman-protocols-bot.git)
cd huberman-protocols-bot

```

2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

```

3. Install dependencies:

```bash
pip install -r requirements.txt

```

4. Configure environment variables:

* Set your bot token in `main.py` (or use a `.env` file).
* Update `CHANNEL_ID` and `CHANNEL_URL` variables inside your middleware file.
* Make sure the bot is promoted to **Administrator** in your channel.

5. Run the bot:

```bash
python main.py

