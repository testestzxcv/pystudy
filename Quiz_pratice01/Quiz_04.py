# 문제4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
import re
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

def remove_tag(s):
    cleaner = re.compile('<.*?>')   # 이 함수의 원리는 뭐지, /는 없는데 왜 지워지지
    cleantext = re.sub(cleaner, '', s)
    return cleantext

print(remove_tag(s))