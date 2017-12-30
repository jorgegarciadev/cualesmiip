# -*- coding: utf-8 -*-

from app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(debug = True, host='0.0.0.0', port=8000)
