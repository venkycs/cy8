import os
import shutil
from url_finder import search_term
from url_downloader_to_file import url_list_downloader
from vuln_report_writer import generate_vul_report
from rag_qa import rag_query_runner
from datetime import datetime
import argparse
import logging
from datetime import datetime
from vuln_report_writer import generate_vul_report
import markdown

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.basicConfig(filename='logs.txt', level=logging.INFO)


def clear_tmp_directory(tmpdir_path):
    # Check if the directory exists
    if os.path.exists(tmpdir_path):
        # Remove the directory and its contents
        shutil.rmtree(tmpdir_path)
    # Recreate the directory
    os.makedirs(tmpdir_path)


def convert_md_to_html(report, html_file):
    html_text = markdown.markdown(report, extensions=["markdown.extensions.extra"])
    with open(html_file, "w", encoding="utf-8") as html_output:
        html_output.write(html_text)


def explore_vulnerability(vulnerability_string, count=5):
    print("Researching on vulnerability this may take few min: " + vulnerability_string)
    clear_tmp_directory("tempdir")
    url_list = search_term(vulnerability_string, count)
    url_list_downloader(url_list)
    report = generate_vul_report(rag_query_runner("tempdir/temp_data.txt", vulnerability_string))
    convert_md_to_html(report, vulnerability_string + ".html")
    logging.info(f"[{current_time}] Started exploring vulnerability")
    for _ in range(count):
        print(vulnerability_string)


def main():
    # Check for the OpenAPI environment variable
    openapi_key = os.environ.get("OPENAI_API_KEY")
    if openapi_key is None:
        # If the environment variable is not found, print an error message and exit
        print("Error: OPENAI_API_KEY environment variable not found, use following command:\nexport OPENAI_API_KEY=\"OPENAI_API_SECRET\"")
        print("to get your key by visiting: https://platform.openai.com/account/api-keys")
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parser = argparse.ArgumentParser(description="Print a vulnerability string a specified number of times.")
    parser.add_argument("vuln", type=str, help="Vulnerability CVE or Name for research")
    parser.add_argument("--count", type=int, default=5, help="Number of times to print the vulnerability (default: 5)")
    args = parser.parse_args()
    logging.info(f"[{current_time}] Started exploring vulnerability: {args.vuln} (with search depth: {args.count})")
    explore_vulnerability(args.vuln, args.count)
    print("Vulnerability exploration completed")
    logging.info(f"[{current_time}] Vulnerability research completed for {args.vuln}")


if __name__ == "__main__":
    main()
