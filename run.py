# -*- coding: utf-8 -*-

from app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
