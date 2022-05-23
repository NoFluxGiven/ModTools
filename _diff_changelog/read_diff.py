from unidiff import PatchSet
from pprint import pprint
import re
from pathlib import Path
from kvparser import Parse
import os

def kv_to_dict(input):
    dt = {}
    for item in input:
        m = re.findall(r"\"(?P<key>[^\"]+)\"\s*\"(?P<value>[^\"]+)\"", item)

        if not m: continue
        key = m[0][0]
        value = m[0][1]

        dt[key] = value
        # if not m: continue
        # key = m.group('key')
        # value = m.group('value')
        # print(f"{key}: {value}")

    return dt

def dict_comparison_pairs(d1,d2):
    new_dict = {}
    for k in d1.keys():
        if k in d2:
            new_dict[k] = (d1[k], d2[k])

    return new_dict

replacers = {
    "Ability": "",
    "Attribute": "",
    "Unit": "",
    "hp": "HP",
    "mp": "MP"
}

def replace_from_dict(val, d):
    for k,v in d.items():
        val = val.replace(k, v)

    return val

def build_comparison_string(oldVal, newVal, key, tooltips, type):
    oStr = oldVal.replace(" ","/")
    nStr = newVal.replace(" ","/")

    tooltip_ref = 'DOTA_Tooltip_'+type+key

    if not tooltip_ref in tooltips:
        kStr = replace_from_dict(key,replacers)

        kStr = re.sub(r"(?P<letter>[A-Z]+)", " \g<letter>", kStr).strip()
        kStr = kStr[0].upper() + kStr[1:].replace("_"," ").lower()
    else:
        kStr = tooltips[tooltip_ref]

        kStr = kStr[0] + kStr.lower()[1:].replace(":","")

        if "%" in kStr:
            oStr = oStr+"%"
            nStr = nStr+"%"
            kStr.replace("%","")

    qualifier = "rescaled"

    try:
        oNum = [float(x) for x in oldVal.split(" ")]
        nNum = [float(x) for x in newVal.split(" ")]

        lesser = [len(oNum) ]

    except ValueError:
        oNum = [0]
        nNum = [0]
        qualifier = "changed"

    if sum(oNum) > sum(nNum): qualifier = "reduced"
    if sum(oNum) < sum(nNum): qualifier = "increased"

    return f"* {kStr} {qualifier} from **{oStr}** to **{nStr}**."


output = []

with open("../../game/resource/addon_english.txt", 'r') as f:
    fileString = f.read()

tooltips = Parse(fileString)

tooltips = tooltips["lang"]["Tokens"]

# with open("changelog_2.14_to_current.diff", "r") as f:
#     file = f.read()

patch = PatchSet.from_filename("changelog_2.14_to_current.diff", encoding="utf-16-le")
# added_hunks = [hunk.target for hunk in patch[0]]
# removed_hunks = [hunk.source for hunk in patch[0]]
for file in patch:
    added_hunks = []
    removed_hunks = []

    filename = file.path

    ref = Path(filename).stem
    full_path = Path(filename)
    type = filename.split("/")[-2]

    if type == "abilities": type = "DOTA_Tooltip_ability_"
    if type == "items": type = "DOTA_Tooltip_ability_"
    if type == "heroes": type = ""
    if type == "units": type = ""

    tooltip_ref = type+ref

    title = tooltips.get(tooltip_ref, ref)

    output.append("")
    output.append("---")
    output.append("")
    output.append(f'## {title}')
    output.append("")

    for hunk in file:
        a = [line[1:].replace("\n","").replace("\t","") for line in hunk.target if line.count("\"") == 4]
        r = [line[1:].replace("\n","").replace("\t","") for line in hunk.source if line.count("\"") == 4]
        added_hunks.extend(a)
        removed_hunks.extend(r)

    # Parse the data

    rmv = kv_to_dict(removed_hunks)
    add = kv_to_dict(added_hunks)

    compared = dict_comparison_pairs(rmv, add)
    
    # output.append(compared)

    for k,v in compared.items():
        output.append(build_comparison_string(v[0],v[1],k, tooltips, type))

    with open("output.md", 'w+') as f:
        f.write("\n".join(output))