"""
date: 20220723
author: Liu Qi
"""
import os
import re
import jieba
from pathlib import Path
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description="Clean word list")
# parser.add_argument("-f", "--file", default="raw/仙听为快雅思热词.txt", help="input file")
parser.add_argument("-f", "--file", default="raw/替换.txt", help="input file")


args = parser.parse_args()

class VocabularyParser:

    def simple_parse(self, file, save=True, save_dir=".", save_filename=None):
        words = []
        desps = []
        with open(file, "r", encoding="utf8") as fin:
            for i, line in enumerate(fin.readlines()):
                # print(line)
                # word_list = re.split(r"[\x00-\xFF][^\x00-\xFF]", line)
                # print(word_list)
                
                res = re.search(r"[\x00-\xFF][^\x00-\xFF]", line)
                # print(res)
                # print(res.group()) 
                # print(res.start())
                # print(res.span())
                # print(res.start())
                # print(res.end())
                
                print("---")
                word = line[:res.start()+1].strip().strip("\n")
                desp = line[res.start()+1:].strip().strip("\n")
                words.append(word)
                desps.append(desp)
                print(f"{i} ... {word},{desp}")
                
                # break
        data = {
            'word': words,
            'description': desps
        }
        df = pd.DataFrame(data)
        
        if save:
            if save_filename is None:
                fn = "{}/{}_formatted.csv".format(save_dir, Path(file).stem)
            else:
                fn = "{}/{}.csv".format(save_dir, save_filename)
            df.to_csv(fn, index=False)
            print(f"save to {fn}")
        return df
    
    def filter_english_words(self, file, save=True, save_dir=".", save_filename=None):
        # 修改jieba包init.py中正则表达式
        # jieba.re_han_default = re.compile(r'[\w]+')
        
        words = []
         # filter all words (length >= 2)
        c = re.compile(r"[\w]{2,}") 
        with open(file, "r", encoding="utf8") as fin:
            for i, line in enumerate(fin.readlines()):
                # res = re.match(r"[\w]+", line)
                # print(res)
                # print(res.group())
                
                # for w in jieba.cut(line):
                #     print(w)
                # chinese-character range \u4e00-\u9fa5 
                line_ = re.sub("[0-9\u4e00-\u9fa5]+", "", line)
                print(line_)
                res = c.findall(line_)
                print(res)
                
                # convert to lower case
                words+=list(map(lambda x: x.lower(), res))
                
                # break
        
        # unique
        # words = list(set(words))
        words_processed = sorted(set(words),  key=words.index)  # keep order
        
        if save:
            if save_filename is None:
                fn = "{}/{}_words_filtered.csv".format(save_dir, Path(file).stem)
            else:
                fn = "{}/{}.csv".format(save_dir, save_filename)
            
            with open(fn, "w", encoding="utf8") as fout:
                for word in words_processed:
                    fout.write(word+"\n")
            print(f"save to {fn}")
        
        return words_processed
        

vp = VocabularyParser()
# vp.simple_parse(file="raw/替换.txt", save=True, save_dir="output")
# vp.simple_parse(file="raw/仙听为快雅思热词.txt", save=True, save_dir="output")

# 20220723 - output all words
# vp.filter_english_words(file="raw/替换.txt", save=True, save_dir="output")
# vp.filter_english_words(file="raw/场景词汇.txt", save=True, save_dir="output")

vp.filter_english_words(file=args.file, save=True, save_dir="output")




