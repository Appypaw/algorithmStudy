import collections
import hashlib

#매우 많은 수(수십억~수천억단위)의 문장으로 이루어진 텍스트에서 중복된 문장을 찾기.

d = collections.defaultdict(list)

with open('largetext.txt', 'r') as datafile:
    for line in datafile:
        # SHA-256 해쉬
        id = hashlib.sha256(line.encode()).digest()
        #line.encode()로 바이트 인코딩함. 해시 함수는 바이트 데이터를 입력으로 받기 때문에 line 문자열을 바이트로 인코딩함.
        #hashlib.sha256은 SHA-256 해시 객체로 생성
        #.digest()메소드로 최종 해시값을 얻어서 이걸 id 변수에 할당함.

        # 해쉬를 두 부분으로 나눔: 키 (처음 2바이트) 값 (남은 바이트들)
        k = id[:2]
        v = id[2:]

        # 키 k를 이용하여 v가 이미 존재하는지 확인함. 
        if v in d[k]:
            print("중복:", id)
        else:
            d[k].append(v)
        #그렇지 않으면 딕셔너리에 추가함.

#https://stackoverflow.com/questions/16347775/find-duplicate-records-in-large-text-file

#test