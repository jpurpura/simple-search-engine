from tokenize_document import TokenizeDocument
from reduce_index import ReduceIndex
from Document.get_document import read_json, make_document
from document_vector import DocumentVector
import os
from time import time
from datetime import timedelta
from add_index_to_db import dump_to_json_file, convert_to_json_objects
import pickle, json
import warnings


def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

    times = [time()]
    bookkeeping_path = os.path.join(os.getcwd(), 'WEBPAGES_RAW', "bookkeeping.json")
    docs = make_document(read_json(bookkeeping_path), 10000)
    times.append(time())
    print("(1 / 5) Made Documents. Tokenizing...")
    td_list = []
    for i, doc in enumerate(docs):
        td = TokenizeDocument(doc)
        td.parse()
        td_list.append(td)
        if i and not i % 1000:
            print("\t -> Tokenized {} Documents".format(i))
    times.append(time())
    print("(2 / 5) Tokenized Documents. Reducing...")
    red_index = ReduceIndex(td_list)
    red_index.reduce()
    times.append(time())
    print("(3 / 5) Reduced Index. Calculating...")
    red_index.tf_idf_champion_list()
    times.append(time())
    print("(4 / 5) TF IDF Calculated. Vectorizing...")
    dv_list = []
    for doc_id, terms in red_index.doc_terms.items():
        dv = DocumentVector(doc_id, terms)
        dv.make_vector_frame()
        # print(dv.vector_frame)
        dv.normalize()
        # print(dv.vector_frame)
        dv_list.append(dv)

    times.append(time())
    print("(5 / 5) Vector Space created.")

    for i in range(len(times) - 1):
        sub = times[i + 1] - times[i]
        print("Section {} took {} seconds.".format(i + 1, round(sub, 3)))
    seconds = round(times[-1] - times[0], 3)
    print("This process took {} seconds ({})".format(seconds,
                                                     timedelta(seconds=seconds)))
    # for term, d in red_index.reduced_terms.items():
    #     print("{}: {}".format(term, d))
    # start = time()
    # document_list = convert_to_json_objects(red_index.reduced_terms)
    # dump_to_json_file(document_list, 'index.json')
    # print("Time to dump to index.json was {} seconds".format(time() - start))
