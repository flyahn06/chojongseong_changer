import hgtk
import re

# 한글 판별을 위한 정규식을 컴파일합니다.
regex = re.compile("[가-힣]")

def decompose_string(string):
    # 모아쓰기를 풀어쓰기로 바꿔줍니다.
    # 2차원 배열을 돌려줍니다.

    # 단어를 각각 풀어줍니다.
    string = list(string)
    result = []

    for letter in string:
        # 정규식을 사용하여 글자가 한글인지 판별합니다.
        if regex.findall(letter):
            # 한글일 시 풀어주고
            result.append(list(hgtk.letter.decompose(letter)))
        else:
            # 아닐 시 그대로 들어갑니다.
            result.append(letter)
    
    return result

def swipe(letter):
    # 초성과 종성을 바꾸어 1차원 배열을 돌려줍니다.
    cho = letter[0]
    jung = letter[1]
    jong = letter[2]

    return [jong, jung, cho]

def change(letters):
    # letters -> 2차원 배열

    result = []

    for letter in letters:
        # 종성이 있는지 판별합니다.
        try:
            assert letter[2]
        except:
            # 없다면 그대로 입력하고
            result.append(letter)
        else:
            # 있다면 초성과 종성을 바꾸어 입력합니다.
            swiped_letter = swipe(letter)
            result.append(swiped_letter)
    
    return result

def compose(letters):
    result = []

    for letter in letters:
        # 글자가 한글이 아닌 경우입니다.
        if len(letter) == 1:
            result.append(letter)
        else:
            # 1차원 배열을 풀어서 함수에 넘겨줍니다.
            result.append(hgtk.letter.compose(*tuple(letter)))
    
    # 완전한 문자열을 돌려줍니다.
    return "".join(result)

while True:
    word = input("> ")
    print(compose(change(decompose_string(word))))
