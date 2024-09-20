import os
import re
from collections import defaultdict, Counter
import subprocess
import sys

# KoNLPy 설치
def install_konlpy():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "konlpy"])

install_konlpy()

from konlpy.tag import Okt

# 테스트 파일 경로
test_file_path = 'C:\\Users\\ssmma\\Documents\\신성민\\서재\\IT\\교양\\누구나 쉽게 읽을 수 있는 IT 과학 이야기 블록 체인.md'

# 키워드 파일 저장 경로
keyword_folder = 'C:\\Users\\ssmma\\Documents\\인공회로 버전 2\\키워드'
important_keywords_file = os.path.join(keyword_folder, 'important_keywords.txt')
general_keywords_file = os.path.join(keyword_folder, 'general_keywords.txt')

okt = Okt()

def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

def classify_sentences(sentences):
    important_sentences = []
    general_sentences = []

    for sentence in sentences:
        user_input = input(f"'{sentence}'가 중요한 문장입니까? (y/n): ")
        if user_input.lower() == 'y':
            important_sentences.append(sentence)
        else:
            general_sentences.append(sentence)

    return important_sentences, general_sentences

def extract_keywords(sentences):
    words = []
    for sentence in sentences:
        words.extend(okt.nouns(sentence))  # 명사만 추출
    return words

def group_similar_keywords(keywords):
    keyword_groups = defaultdict(list)
    for keyword in keywords:
        keyword_groups[keyword].append(keyword)
    grouped_keywords = {group: group for group in keyword_groups.keys()}
    return list(grouped_keywords.values())

# 파일에서 문장 읽기
sentences = read_sentences_from_file(test_file_path)

# 문장 분류
important_sentences, general_sentences = classify_sentences(sentences)

# 키워드 추출
important_keywords = extract_keywords(important_sentences)
general_keywords = extract_keywords(general_sentences)

# 키워드 빈도 계산
important_keywords_counter = Counter(important_keywords)
general_keywords_counter = Counter(general_keywords)

# 중요 키워드 선정 기준: 중요 문장에서 자주 나오고 일반 문장에서 자주 나오지 않는 단어
selected_important_keywords = [word for word, freq in important_keywords_counter.items() if freq > 1 and general_keywords_counter[word] < freq]

# 키워드 그룹화
important_keywords = group_similar_keywords(selected_important_keywords)
general_keywords = group_similar_keywords(list(general_keywords_counter.keys()))

# 키워드 파일 저장 폴더 생성
os.makedirs(keyword_folder, exist_ok=True)

# 그룹화된 키워드 저장
with open(important_keywords_file, 'w', encoding='utf-8') as file:
    for keyword in important_keywords:
        file.write(keyword + "\n")

with open(general_keywords_file, 'w', encoding='utf-8') as file:
    for keyword in general_keywords:
        file.write(keyword + "\n")

print("그룹화된 중요 키워드:", important_keywords)
print("그룹화된 일반 키워드:", general_keywords)
