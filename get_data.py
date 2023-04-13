from dotenv import load_dotenv
from pmaw import PushshiftAPI
from tqdm import tqdm

import os
import pandas as pd
import csv

load_dotenv('.env')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

NUM_POSTS = 10
OUTPUT_FILENAME = './data.csv'
OUTPUT_FILE = open(OUTPUT_FILENAME, 'w', encoding="utf-8", newline='')

def main():

    punctuation = '''!()-[]{};:'"\<>/?@#$%^&*_~'''

    filters = ['id', 'title', 'score', 'author', 'num_comments', 'url', 'created_utc']
    columns = ['id', 'pov', 'title', 'score', 'author', 'num_comments', 'url', 'created_utc']

    csvwriter = csv.writer(OUTPUT_FILE)
    csvwriter.writerow(columns)

    api = PushshiftAPI()
    api_request_generator = api.search_submissions(subreddit='UkraineRussiaReport', size=NUM_POSTS, filter=filters)

    print("[!] Printing to CSV")

    for post in api_request_generator:
        title = post['title'].translate(post['title'].maketrans('', '', punctuation))
        words = title.split(' ')
        pov = words[0].upper()
        title = " ".join(words[2::])

        csvwriter.writerow([post['id'], pov, title, post['score'], post['author'], post['num_comments'], post['url'], post['created_utc']])
        OUTPUT_FILE.flush()

if __name__ == '__main__':
    print('[!] Getting Submissions')
    main()
    print(f"[!] Done ({OUTPUT_FILENAME})")
    OUTPUT_FILE.close()