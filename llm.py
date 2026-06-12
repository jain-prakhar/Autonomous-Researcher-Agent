from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

RATE_LIMIT_SIGNALS = [
    "429",
    "resourceexhausted",
    "quota",
    "rate limit",
    "rate_limit"
]


class LLMWithFallback:

    def invoke(self, prompt):

        try:
            return gemini_llm.invoke(prompt)

        except Exception as e:

            error_text = str(e).lower()

            if any(signal in error_text for signal in RATE_LIMIT_SIGNALS):
                print("Gemini rate limit reached, falling back to Groq")
                return groq_llm.invoke(prompt)

            raise


llm = LLMWithFallback()
