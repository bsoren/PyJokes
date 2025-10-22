# 📦 PyJokes
*Python-based utility for sending jokes in email*

---

## 📖 Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [License](#license)
- [Contact](#contact)

---

## 🧐 About
Fetches a random joke from internet and sends them in email 
Example:  
> This project is a Python-based utility for sending emails with jokes.  
> It aims to simplify fetching and sending jokes, handle `.env` configuration, and demonstrate modular code structure.

---

## ✨ Features
- ✅ Simple and modular design  
- 🔒 Secure environment variable handling using `python-dotenv`  
- 📨 Supports html template and multiple recipients  
- 📜 Logs all sent emails  

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PyJokes.git
   cd PyJokes
   
   pip3 install pipenv
   pipenv shell
   pipenv install

## 🚀 Usage
### Running the project
```bash
# Run main script
python main.py
```

## 🔧 Configuration
Describe any environment variables, config files, or settings required for your project.

| Variable / Setting | Description                                              | Required |
|--------------------|----------------------------------------------------------|----------|
| `EMAIL_USER`       | Gmail email user used for sending email                  | Yes
| `EMAIL_PASS`       | Above enail user gmail app password                      | Yes
| `TO_EMAILS`        | Comma separted list of emails to whom email will be sent | Yes

**Optional:** instructions for creating a `.env` or config file:
```bash
# .env
EMAIL_USER=abc@gmail.com
EMAIL_PASS="abc xyz ijl mno"
TO_EMAILS="pqr@gmail.com, utv@gmail.com"
```

## 📬 Contact
- Name: Bijay Soren
- Email: bijay.soren@gmail.com
- GitHub: @bsoren

## MIT License

Copyright (c) [2025] [Bijay Soren]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



   
