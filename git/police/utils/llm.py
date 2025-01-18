from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def ask_qwen(question):
    template = "{question}"

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="qwen2:0.5b")

    chain = prompt | model

    return chain.invoke({"question": question})

def ask_qwen_coder(question):
    template = "{question}"

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="qwen2.5-coder:0.5b")

    chain = prompt | model

    return chain.invoke({"question": question})