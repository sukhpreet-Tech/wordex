from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Gemini API Key
API_KEY = "YOUR_API_KEY"

# LLMlangchain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY
)

# Prompt
prompt = ChatPromptTemplate.from_template(
    "You are Defenser AI Assistant. Answer the user's question.\nQuestion: {question}"
)

# Chain
chain = prompt | llm

# Chat Loop
print("Defenser AI Online (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chain.invoke({"question": user_input})

    print("Defenser:", response.content)