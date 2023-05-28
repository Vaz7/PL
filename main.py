import projeto_PL_parser as parser
import sys
import json
import utils

if len(sys.argv) < 3:
    print("Not enough arguments provided")
else:
    result = None
    with open(sys.argv[1],"r") as f:
        result = parser.parser.parse(f.read())

    with open(sys.argv[2], 'w') as f:
        if result:
            json.dump(result, f, indent=4, separators=(',', ': '), ensure_ascii=False)
        else:
            print("Something went wrong")
    if result:
        utils.validate_json_file(sys.argv[2])