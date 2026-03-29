# Restaurant Sentiment Analyzer

My project is a simple sentiment analyzer which i built to understand restaurant reviews using NLP.It uses VADER  with custom tweaks to better see how people actually talk about food.

## Problem Statement

Restaurant platforms like Zomato and Swiggy have millions of reviews, but going through them manually is slow and not practical.So ,I built this project to quickly scan reviews and get a basic sense of customer feedback without reading everything one by one.

## Course Concepts Applied

| Concept | Application |
|---------|-------------|
| **Natural Language Processing (NLP)** | TProcessing and analyzing raw review text |
| **Sentiment Analysis** | Classifying text into positive, negative, or neutral categories |
| **VADER Sentiment Analyzer** | Pre-trained lexicon-based model from NLTK for sentiment scoring |
| **Domain-Specific Keyword Enhancement** | Custom restaurant-related keywords to improve accuracy |
| **Data Processing with Pandas** | Reading, transforming, and exporting CSV datasets |

## Project Structure

```
restaurant_sentiment/
├── main.py              # Main
├── analyzer.py          # Brain
sentiment analysis logic
├── test_reviews_50.csv  # Test case
└── README.md            # Project docs
```

## How It Works

The analyzer works in two stages:

1. It first uses VADER to get a base sentiment score for each review.

2. Then it adjusts that score using restaurant-specific keywords 
   like "delicious", "overpriced", or "undercooked" to better reflect real feedback.
   These adjustments help fix cases where VADER alone might miss context.

3. **Adjusted Score Calculation**:
   ```
   adjusted_score = compound + (0.12 × positive_hits) - (0.12 × negative_hits) - (0.05 × neutral_hits)
   ```

4. **Classification Thresholds**:
   - >= 0.12  → **Positive**
   - <= -0.12 → **Negative**
   - Otherwise → **Neutral**

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone or download this project

2. Install required dependencies:
   ```bash
   pip install pandas nltk
   ```

3. Download NLTK VADER lexicon (run once):
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage

### Run the Application

```bash
python main.py
```

### Option 1: Analyze CSV File

```
Restaurant Feedback Analyzer
1.with csv file
2.with sentences (type exit to stop)
Enter your choice(1/2): 1

Enter csv file path: test_reviews_50.csv
```

**Requirements for CSV file:**
- Must contain a column named `review`
- Other columns (date, source, etc.) are preserved in output

**Output:**
- Displays summary statistics (total, positive, negative, neutral counts)
- Saves results to `<filename>_scanned.csv` with added columns:
  - `analyzed_feedback`: Sentiment label
  - `analyzed_points`: Adjusted sentiment score

### Option 2: Interactive Mode

```
Enter your choice(1/2): 2

give one sentence (type exit to quit):

Enter sentence: The biryani was amazing and well-spiced!
feedback: Positive
points: 0.73

Enter sentence: exit
SEE YOU!!!!
```

## Sample Output

| Review | Feedback | Score |
|--------|----------|-------|
| Best kofta in town, authentic taste | Positive | 0.92 |
| Very slow delivery; momos arrived cold | Negative | -0.24 |
| The veg thali was okay, nothing special | Neutral | -0.19 |

## Dataset

The included `test_reviews_50.csv` contains 50 sample reviews from various Indian restaurants with:
- **Reviews**: Customer feedback text
- **Date**: Review submission date
- **Source**: Platform (Swiggy, Zomato, Google, Dineout, TripAdvisor)

## Limitations
[text](README1.MD)
- Works best with English text
- Sarcasm and irony may be misclassified
- Domain keywords are tuned for Indian restaurant context

## Future Improvements

Some things I’d like to improve:
- Add support for regional languages (Hindi, Tamil, etc.)
- Try ML models like Naive Bayes or LSTM
- Build a simple web interface (Flask or Streamlit)
- Add charts to visualize sentiment trends

## Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and CSV handling |
| `nltk` | Natural language processing and VADER sentiment |

## Author
- Suyash Avatar 
- 25BCE10367
## License
This project is for educational purposes.
