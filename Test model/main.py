import argparse
import json
import time
from model import Model

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        description="Entry point for model")

    parser.add_argument("-d", "--data", dest="data",
        type=str, required=True,
        help="Test data input")

    parser.add_argument("-t", "--truth", dest="truth",
        type=str, required=True,
        help="Ground truth input")

    args = parser.parse_args()

    model = Model(
        file = args.data, ground_truth = args.truth)

    start_time = time.time()

    summary = model.run()
    result = summary[0]
    report = summary[1]
    run_time = time.time() - start_time
    report.update({'run_time': run_time})
    with open('report.json', 'w') as f:
        json.dump(report, f)
    with open('result.json', 'w') as f:
    	json.dump(result,f)
