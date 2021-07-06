import os
import sys
import jsonschema2md
import json

parser = jsonschema2md.Parser() 
object_path = 'report_objects'
report_objects = os.listdir(object_path)

for r in report_objects:
    file_name = object_path + '/' + r
    if file_name.endswith('.json'):
        with open(file_name) as json_file:
            data = json.load(json_file)
            parser = jsonschema2md.Parser()
            md_lines = parser.parse_schema(data)
            f = open("demofile3.md", "a")
            f.writelines(md_lines)
            f.close()


text = ''
for header, data in js_data.items():
    if "link" not in header:
        text += f'## {header}\n'
        if len(data) >= 0:
            for content in data:
                if type(content) == dict:
                    for k, v in content.items():
                        text += f'**{k}**: {v}\n\n'
                    text += '\n'
                elif type(content) != dict:  # case of object properties as single string, not list
                    text += f'{content}'
print(text)

f = open("demofile3.md", "a")
f.writelines(md_lines)
f.close()