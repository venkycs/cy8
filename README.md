# Cy8 - AI-Powered Vulnerability Report Generation

Cy8 is an innovative project that combines the power of AI with modern technologies like OpenAI, RAG (Retrieval-Augmented Generation), and langChain to simplify and accelerate the process of generating vulnerability reports. Designed for security professionals, Cy8 aims to reduce the time and effort spent on researching and documenting trending vulnerabilities.

Sample report here - https://github.com/venkycs/cy8/blob/main/Citrix%20Bleed.md

## Key Features

- **Efficiency**: Cy8 automates the research and report generation process, allowing security analysts to focus on critical tasks.

- **Ease of Use**: Setting up and running Cy8 is straightforward and takes less than 5 minutes.

- **Stay Informed**: Cy8 keeps you up to date by fetching latest information on threats and vulnerabilities.

## Prerequisites

Before using Cy8, make sure you have the following prerequisites in place:

- **OpenAI API Key**: You'll need an OpenAI API key to unlock the AI capabilities integrated into Cy8.

## Getting Started

1. **Clone the Repository**: Start by cloning the Cy8 repository to your local machine:

   ```bash
   git clone https://github.com/venkycs/cy8.git
   cd cy8

2. ***Virtual Environment**: Create a virtual environment and activate it to isolate Cy8's dependencies:

   ```bash
   python -m venv .
   source bin/activate

3. ***Install Dependencies**: Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt

4. ***Running the project**: Setup OpenAI API Key and run the project:

   ```bash
   export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
   python main.py "Vulnerability Name or CVE"


# How Cy8 Works

Cy8 leverages the internet to search for information related to the provided vulnerability. Here's a high-level overview of its operation:

**Internet Research**: Cy8 searches the internet, downloading content from relevant URLs and compiling it into a single file.

**AI Augmentation**: It uses AI-powered techniques to analyze and retrieve essential data using predefined questions about vulnerabilities.

**Question & Answer Generation**: Cy8 transforms the extracted information into a Q&A format and uses it to prompt the generation of detailed vulnerability reports.

**Presentation-Ready**: The resulting report is presented in Markdown format and conveniently converted to HTML for easy sharing and collaboration.
Contribution and Collaboration

We welcome contributions and feedback from the cybersecurity community. Help us enhance Cy8 and make vulnerability research more efficient and exciting. Feel free to open issues, submit pull requests, or provide valuable insights.

# License

This project is licensed under the MIT License.

Ready to take your vulnerability research to the next level? Start using Cy8 today!
