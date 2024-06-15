import os
from openai import OpenAI
from law_keywords import law_keywords
from dotenv import load_dotenv
load_dotenv()

class LanguageModel():

    def __init__(self, config):
        self.key = os.getenv("OPENAI_API_KEY")
        self.model = config['llm_model']
        self.client = OpenAI(api_key=self.key)

    def explain_similarity(self, sentence1, sentence2):
        prompt = f"Explain the similarities and differences between the following two sentences, reffer to them as 'doc1, doc2':\n\n1. {sentence1}\n\n2. {sentence2}\n\nExplanation:"
        response = self.ask(prompt)
        return response

    def ask(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )
        return response.choices[0].message.content

    def ask_doc_type(self, text):
        first_50000_tokens = text[:50000]
        areas_of_law = list(law_keywords.keys())
        prompt = f"from these legal areas \n\n1 {areas_of_law} \n\n2 what is legal area of this text: \n\n2 {first_50000_tokens} \n\n Legal area:"
        response = self.ask(prompt)
        for law_area in areas_of_law:
            if law_area in response:
                return law_area
        return "unknown"