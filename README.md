# Digital Engagement Demo  

This project demonstrates digital engagement analysis and outreach techniques inspired by the Digital Engagement Officer role at the National Fairground and Circus Archive (NFCA). It explores approaches for enhancing digital visibility of collections, including data analysis, AI-driven text recognition, and crowdsourcing concepts ([jobsite.sheffield.ac.uk](https://jobsite.sheffield.ac.uk/job/Digital-Engagement-Officer/1729-en_GB/#:~:text=opportunity,the%20post%20%C2%A0%20Person%20Specification), [libguides.su.edu](https://libguides.su.edu/crowdsourcing#:~:text=with%20archival%20materials%20are%20increasingly,Sign%20Up%20for%20Digital%20Crowdsourcing)).  

## Project Overview  

- `digital_engagement_analysis.py`: A Python script that generates a synthetic dataset of social media interactions (likes, shares, comments) and calculates engagement metrics such as average engagement rate and identifying top‑performing posts. The script demonstrates data literacy and analytic skills required to evaluate digital platforms and improve engagement.  
- `ocr_example.py`: A simple OCR module using the `pytesseract` library and Pillow. It accepts a path to an image file and prints the extracted text, illustrating how AI/HTR technologies can be applied to convert scanned images or handwritten documents into machine‑readable text.  

## How to Run  

1. Ensure you have Python 3.x installed along with the `pandas`, `numpy`, `matplotlib`, `pytesseract`, and `Pillow` libraries. For `pytesseract` you also need the Tesseract OCR engine installed on your system (see the [pytesseract documentation](https://pypi.org/project/pytesseract/) for installation instructions).  
2. Clone this repository or download the files to your local machine.  

### Running the engagement analysis  

```bash
python digital_engagement_analysis.py
```  

The script will create a CSV file with sample social media engagement data, calculate key statistics, and display plots of engagement metrics.  

### Running the OCR example  

Provide the path to an image file containing text:  

```bash
python ocr_example.py path/to/your/image.jpg
```  

The script will output the extracted text from the image using the Tesseract OCR engine.  

## Skills Demonstrated  

- **Digital literacy and data analysis**: Leveraging Python and data-analysis libraries to process engagement data, calculate statistics, and create visualizations to assess effectiveness of online platforms ([jobsite.sheffield.ac.uk](https://jobsite.sheffield.ac.uk/job/Digital-Engagement-Officer/1729-en_GB/#:~:text=opportunity,the%20post%20%C2%A0%20Person%20Specification)).  
- **Awareness of AI/HTR potential**: The project is structured to be extendable; additional modules such as `ocr_example.py` explore handwritten text recognition and AI-powered metadata extraction, aligning with the role’s focus on exploring AI and HTR technologies ([jobsite.sheffield.ac.uk](https://jobsite.sheffield.ac.uk/job/Digital-Engagement-Officer/1729-en_GB/#:~:text=opportunity,the%20post%20%C2%A0%20Person%20Specification)).  
- **Crowdsourcing and community engagement**: Inspired by crowdsourcing initiatives, the project could be extended to include tasks where volunteers help transcribe or enrich metadata, improving accessibility and engagement with archival collections ([libguides.su.edu](https://libguides.su.edu/crowdsourcing#:~:text=with%20archival%20materials%20are%20increasingly,Sign%20Up%20for%20Digital%20Crowdsourcing)).  
- **Documentation and metadata**: Providing clear README instructions and committing code with meaningful messages reflects good documentation practices, akin to creating descriptive metadata for digital objects.  

## Future Work  

- Integrate more advanced AI/HTR modules using open-source OCR or HTR libraries to demonstrate automated transcription of scanned or handwritten material.  
- Build a small web interface where volunteers can contribute by tagging or transcribing items, showcasing crowdsourcing for archives.  
- Analyze real (non-sensitive) engagement data from public social media accounts to produce actionable insights. 
