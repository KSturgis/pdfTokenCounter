import argparse

import pymupdf  # Handles opening and extracting text from the PDF
import tiktoken  # Handles counting the tokens

def count_gpt_tokens_from_pdf(pdf_filepath, encoding):
    """
    This function opens a PDF file, extracts the text, converts it to GPT tokens using the specified encoding,
    and counts the number of tokens. This should only be used a rough estimate of the pdf file, the just looks
    at the raw text of each page.

    Args:
        pdf_filepath (str): The path to the PDF file.
        encoding (str):  See tiktoken for supported encodings.

    Returns:
        int: The number of GPT tokens in the PDF text.
    """

    # Encode text to GPT tokens using the given encoding
    encoder = tiktoken.get_encoding(encoding)
    # Open the PDF document
    num_tokens = 0
    page_num = 1
    with pymupdf.open(pdf_filepath) as doc:
        # Extract text from all pages
        for page in doc:
            text = page.get_text()
            tokens = encoder.encode(text)

            # Count the number of tokens
            page_tokens = len(tokens)
            num_tokens += page_tokens
            print(f"Page {page_num} has {page_tokens} total:{num_tokens}")
            page_num += 1

    return num_tokens


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="pdyTokenCounter",
    description="Count the approximate number of tokens in a pdf using sl100k_base",
)
parser.add_argument("pdf_file", type=str, help="Path to the PDF file")
parser.add_argument("--encoding", default="cl100k_base")
args = parser.parse_args()

# Example usage
number_of_tokens = count_gpt_tokens_from_pdf(args.pdf_file, args.encoding)

print(
    f"The PDF file '{args.pdf_file}' has approximately {number_of_tokens} GPT tokens."
)
