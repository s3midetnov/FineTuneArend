import json
import random
import pathFile

def parse_concatenated_json(path):
    objects = []
    buffer = []
    brace_level = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            # Count opening/closing braces not inside strings
            brace_level += line.count("{")
            brace_level -= line.count("}")

            buffer.append(line)

            # When brace level drops to zero we have a complete JSON object
            if brace_level == 0 and buffer:
                block = "".join(buffer).strip()
                if block:
                    objects.append(json.loads(block))
                buffer = []

    return objects

# Code that transforms Arend lib samples into trainable data, version 1
def simplify_jsonl(entry : dict) -> dict:
    two_field_dict = dict()
    two_field_dict['prompt'] = str(entry['Context']) + "<<<break>>>" + str(entry['Premises']) + "<<<break>>>" + entry['Expected type']
    two_field_dict['completion'] = entry['Expression']
    return two_field_dict