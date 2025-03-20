# plagiat_detection.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def detect_plagiarism(text1, text2):
    # Téléchargement des stopwords en anglais
    stop_words = set(stopwords.words('english'))
    
    # Tokenisation des deux textes
    text1_tokens = word_tokenize(text1)
    text2_tokens = word_tokenize(text2)

    # Filtrage des tokens (enlevant la ponctuation et les stopwords)
    text1_tokens = [word for word in text1_tokens if word.isalnum() and word not in stop_words]
    text2_tokens = [word for word in text2_tokens if word.isalnum() and word not in stop_words]

    # Reconstruction des textes nettoyés
    text1_cleaned = ' '.join(text1_tokens)
    text2_cleaned = ' '.join(text2_tokens)

    # Création de vecteurs TF-IDF pour comparer les textes
    vectorizer = TfidfVectorizer().fit_transform([text1_cleaned, text2_cleaned])
    vectors = vectorizer.toarray()

    # Calcul de la similarité cosinus
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1]
