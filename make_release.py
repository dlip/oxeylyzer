from itertools import permutations
from os import path
import pathlib
import json
from glob import glob
from random import choice


def path_to_language(path: str):
    return path.split("\\")[-1].split(".")[0]


def load_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def doubles_for_lang(language: str):
    bigrams = load_json(f"static/language_data/{language}.json")['bigrams']
    res = 0
    for b, f in bigrams.items():
        if b[0] == b[1]:
            res += f
    return res * 100


def check_doubles(path: str):
    l = path_to_language(path)
    print(f"{l:-<16}: {doubles_for_lang(l)}%")


def main():
    for p in glob("static/language_data/*.json"):
        l = path_to_language(p)
        chars_count = len(load_json(p)['characters'])
        print(f"{l}: {chars_count} chars")
    


if __name__ == "__main__":
    main()