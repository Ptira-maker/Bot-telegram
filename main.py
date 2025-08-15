#!/usr/bin/env python3
"""
Telegram Bot demo per Replit
Comandi:  /start   -> saluto
          Qualsiasi testo -> echo
"""

import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# Leggo il token dalla variabile d’ambiente (impostata in Replit Secrets)
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("Manca la variabile d'ambiente TOKEN!")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ---------- handlers ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ciao! Sono vivo su Replit 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt = update.message.text
    await update.message.reply_text(f"Hai scritto: {txt}")

# ---------- main ----------
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot avviato. In ascolto…")
    app.run_polling()

if __name__ == "__main__":
    main()
