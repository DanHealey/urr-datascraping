# URR Datascraping/Classification

Project to classify sentiments of Reddit posts relating to Ukraine-Russia war. Reddit posts were scraped using Pushshift API and language models were used for classification.

Dataset: [Kaggle Link](https://www.kaggle.com/datasets/danhealey/russia-ukraine-sentiment-analysis)

| Classification | # Posts |
| -------------- | ------- |
| Ukraine (UA)   |   6618  |
| Russia (RU)    |   5601  |
| Neither (NONE) |    284  |
| Total:         |  12503  | 

Models:

| Model | Validation Accuracy |
| ---------------  | ------- |
| Median value     | 52%     |
| Embedding+Dense  | ~65%    | 
| Embedding+LSTM   | ~72%    |
| BERT Fine Tuning | ~80%    |
