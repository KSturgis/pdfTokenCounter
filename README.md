# Description
This is a very simple Python command that counts the number of tokens in a PDF file.
This tool can be used to understand how many tokens would be needed in the context
window of a GPT model to add the PDF as text. *Note:* This does not take into account 
multimodal ingestion that may involved.

In Artificial Intelligence, Large Language Model Generative Pre-trained Transformer
(AI LLM GPT) the first step of processing text is to tokenize the text into a mathematical
vector representation that is passed into the attention block and the rest of the 
transformer architecture.

# Usage
You will need a python environment (or venv) with tiktoken and pymupdf

```
pip install tiktoken pymupdf
python pdfTokenCounter.py path/to/pdf/document.pdf
```

## Why are AI LLMs Important?
AI LLMs are revolutionizing various fields by enabling machines to understand and process 
human language with unprecedented capability.  They power applications like chatbots, 
machine translation, text summarization, and even creative writing.  As AI LLM technology 
continues to develop, they hold immense potential for further advancements in fields like 
scientific research, education, and human computer interaction.

## Keywords
ChatGPT, LLM, GPT-3, token, AI