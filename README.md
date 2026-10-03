# Amazon Review Sentiment Analysis

A simple Python project that uses the OpenAI API to classify Amazon product reviews from **1 (very negative) to 5 (very positive)**.

## Tech

* Python
* Pandas
* OpenAI API

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ChikondiBanda1/amazon_review_sentiment_analysis.git
cd amazon_review_sentiment_analysis
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a file called `.env` in the project folder:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not share or commit your API key.

### 5. Run the project

```bash
python main.py
```

If `python` doesn't work on macOS/Linux, use:

```bash
python3 main.py
```

The program will load the Amazon reviews and use the OpenAI API to assign sentiment scores.

## Example

```text
Sentiment Scores: [4, 4, 4, 5, 3, 4, 5]
```
