# Currency-Converter
💱 Currency Converter Web App

A full-stack currency converter web application built using Flask (Python) for the backend and HTML, CSS, JavaScript for the frontend.
The app fetches real-time exchange rates using the ForexRateAPI and provides a clean, interactive UI with dropdown currency selection and live conversion.

🚀 Features

Real-time currency conversion using an external API

Dynamic currency dropdowns loaded from CSV

Flask REST API (/convert) with JSON communication

Modern UI with background video and 3D model support

CORS enabled for safe frontend–backend interaction

Error handling for invalid inputs and API failures

🛠 Tech Stack

Frontend

HTML5, CSS3

JavaScript (Fetch API)

Jinja2 templating

<model-viewer> for 3D visuals

Backend

Python

Flask

Flask-CORS

Requests

CSV data handling

API

ForexRateAPI (currency exchange rates)

📂 Project Structure
project/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── video/
│   │   └── finalbg.mp4
│   ├── img/
│   │   └── bit_coin.glb
│   └── data/
│       └── currencies.csv

⚙️ Setup & Run
pip install flask flask-cors requests
python app.py


Open in browser:

http://127.0.0.1:5000/

🔁 API Endpoint

POST /convert

{
  "from": "USD",
  "to": "INR",
  "amount": "100"
}


Response

{
  "result": 8300.45
}

👥 Team Project

This project was developed collaboratively as a team effort, focusing on:

Frontend UI/UX design

Backend API integration

Data handling and validation

System integration and testing

📌 Notes

API key is currently stored locally for development

CSV-based currency list allows easy extension

Designed to be modular and scalable

If you want, I can:

tighten this into one-page README

add team member credits section

add screenshots section

or write a professional academic-submission version

