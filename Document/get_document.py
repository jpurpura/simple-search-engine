import os
import json

from document import Document
from doc_id import DocID
from doc_url import DocURL
# for using bookkeeping.json

BAD_EXTENSIONS = [".jpg", ".zip", ".png", ".css"]
BAD_FILES = ["39/373", "35/269", "8/121"]


def read_json(file_name):
    with open(file_name) as json_data:
        json_dict = json.load(json_data)
    return json_dict


def make_document(json_dict, count=None):
    doc_list = []
    for doc_id, doc_url in json_dict.items()[:count]:
        for ext in BAD_EXTENSIONS:
            if doc_url.endswith(ext):
                continue
        # if ".jpg" in doc_url or ".zip" in doc_url or ".png" in doc_url or ".css" in doc_url:
        #     continue
        if ".txt" in doc_url and "Wumpus" in doc_url:
            continue
        if doc_id in BAD_FILES:
            continue
        doc_list.append(Document(DocID(doc_id), DocURL(doc_url)))
    return doc_list

# for iterating over WEBPAGES_RAW


def get_docs_in_dir(doc_dir):
    return [os.path.join(doc_dir, doc) for doc in os.listdir(doc_dir)]


def get_all_docs(directory):
    all_docs = []
    for sub_dir in os.listdir(directory):
        sub_dir = os.path.join(directory, sub_dir)
        if os.path.isdir(sub_dir):
            all_docs.append(get_docs_in_dir(sub_dir))
    return all_docs


if __name__ == "__main__":
    # get_docs_in_dir("/Users/jamespurpura/Documents/UCI17-18/INF141/Assignments/simple-search-engine/WEBPAGES_RAW/0")
    # for d in get_all_docs("/Users/jamespurpura/Documents/UCI17-18/INF141/Assignments/simple-search-engine/WEBPAGES_RAW"):
    #     print(d)
    json_dict = read_json("/Users/jamespurpura/Documents/UCI17-18/INF141/Assignments/simple-search-engine/WEBPAGES_RAW/bookkeeping.json")
    for doc in make_document(json_dict, 10):
        print(doc)
    #
    # for k, v in read_json("/Users/jamespurpura/Documents/UCI17-18/INF141/Assignments/simple-search-engine/WEBPAGES_RAW/bookkeeping.json").items():
    #     print("{}: {}".format(k, v))
