# Document Comparison App

## Overview
This application compares two legal documents to identify similarities and differences using a large language model (LLM).

## Features
- Upload and read PDF, DOCX, and TXT files
- Segment documents into sentences
- Generate embeddings using a pre-trained LLM
- Calculate similarities and highlight differences

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`
4. Upload two documents and view the comparison results

## Approach
- Used Streamlit for the user interface
- Employed `sentence-transformers` for embedding generation
- Calculated cosine similarities to identify similar and different segments

## Challenges
- Handling large documents efficiently
- Ensuring accurate similarity measurements

## Future Improvements
- Enhance the UI for better user experience
- Optimize embedding generation for speed
- Implement advanced comparison metrics
