from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from langchain.document_loaders import WikipediaLoader


def answer_question_about(person_name, question):
    # Get Wikipedia Article
    docs = WikipediaLoader(query=person_name, load_max_docs=1)
    context_text = docs.load()[0].page_content
    print(context_text)
    # Connect to OpenAI Model
    f = open('C:\\Users\\dahmedsiddiqui\\Desktop\\OPEN_AI_KEY.txt')
    api_key = f.read()
    print(api_key)
    model = ChatOpenAI(openai_api_key=api_key)

    # Ask Model Question
    human_prompt = HumanMessagePromptTemplate.from_template(
        'Answer this question\n{question}, here is some extra context:\n{document}')

    # Assemble chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

    # result
    result = model(chat_prompt.format_prompt(question=question, document=context_text).to_messages())

    print(result.content)

topic = input("Enter topic for wiki search :")
que = input("Enter your question :")
answer_question_about(topic,que)