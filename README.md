# AI-_TEXT_DETECTOR_API
FLASK API FOR FINAL YEAR PROJECT OF MCA

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-text-detector.git
cd ai-text-detector
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the Flask server:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## API Endpoint

### Predict AI-Generated Text

**Endpoint**

```
POST /predict
```

---

### Request Body

```json
{
  "text": "Artificial intelligence is transforming the world."
}
```

---

### Example using curl

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"text":"Artificial intelligence is transforming the world"}'
```

---

### Response

```json
{
  "input_text": "Artificial intelligence is transforming the world",
  "prediction": "AI-generated"
}
```
