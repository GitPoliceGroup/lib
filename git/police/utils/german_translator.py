from transformers import MarianMTModel, MarianTokenizer
import sentencepiece as spm
import sacremoses
import torch


class GermanTranslator:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-de"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, english_text):
        try:
            input_ids = self.tokenizer.encode(english_text, return_tensors="pt")
            output_ids = self.model.generate(input_ids)
            german_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
            return german_text
        except Exception as e:
            print(f"Error in translation: {e}")
            return english_text



# Example usage:
if __name__ == "__main__":
    # Test the function with some examples
    test_sentences = [
        "Hello, how are you?",
        "I love programming",
        "The weather is nice today"
    ]
    gt = GermanTranslator()
    for sentence in test_sentences:
        translated = gt.translate(sentence)
        print(f"English: {sentence}")
        print(f"German: {translated}")
        print("-" * 50)