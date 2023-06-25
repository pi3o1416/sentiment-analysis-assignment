
import numpy as np
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from scipy.special import softmax


class RobertaSentmentAnalysisModel():
    def __init__(self):
        self.MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.config = AutoConfig.from_pretrained(self.MODEL)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL)


    @staticmethod
    def preprocess(text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def rank_scores(self, scores):
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        label_score = {self.config.id2label[ranking[i]]: scores[ranking[i]] for i in range(scores.shape[0])}
        return label_score

    def classify_text(self, text):
        text = self.preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        labeled_scores = self.rank_scores(scores)
        return next(iter(labeled_scores))
