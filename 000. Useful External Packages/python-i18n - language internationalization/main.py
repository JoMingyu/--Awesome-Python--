# https://github.com/tuvistavie/python-i18n
# pip install python-i18n
import i18n
# python-i18n 은 파이썬에서 i18n 을 구현할 때 유용한 라이브러리이다.
# i18n 이란, internationalization 에서 첫 글자 i와 마지막 글자인 n을 그대로 쓰고 그 사이에 있는 18개 글자들은 숫자18로 줄인 말이다.
# internationalization(국제화) 는 이름 그대로, 다국어 시스템을 지원하여 각 나라 사람들이 자신들의 언어를 읽을 수 있게 하는 것이다.

# 다음은 가장 심플한 예제이다.
i18n.add_translation('사과', 'apple')
print(i18n.t('사과'))

# 다음처럼 placeholder 를 사용할 수도 있다.
i18n.add_translation('반가워', 'nice to meet you %{name} ~~')
print(i18n.t('반가워', name='Flouie'))

# python-i18n 은 YAML 과 JSON 파일 형식사용을 지원한다.
# 간단하게 하게 YAML 파일의 경로를 추가하고 번역할 수 있다.
# json 을 사용하고 싶으면 파일 포맷만 바꾸어 주면 된다
# i18n.set('file_format', 'json')
i18n.load_path.append('./')
print(i18n.t('foo.awesome python'))

# ROR 의 i18n 에 기반하여 Pluralization(다중화) 를 제공한다.
# 다중화는 사용할 때, 위의 예제와는 다르게 번역 값(t 함수에 키를 넣었을 때 반환되는 값) 을 딕셔너리로 하고, 딕셔너리 키가 한개 이상이어햐한다.
i18n.add_translation('awesome_python_issue', {
    'zero': 'There is no issue assigned to you.',
    'one': 'There is one issue assigned to you.',
    'few': 'There is %{count} issue assigned to you.',
    'many': 'There is %{count} issue assigned to you. hurry up!!'
})
print(i18n.t('awesome_python_issue', count=0))
print(i18n.t('awesome_python_issue', count=1))
print(i18n.t('awesome_python_issue', count=3))
print(i18n.t('awesome_python_issue', count=12))

# Fallback 을 지원하여, 키를 설정한 locale 에서 찾을 수 없을 때 유용하다
i18n.set('locale', 'jp')
i18n.set('fallback', 'en')
i18n.add_translation('foo', 'bar', locale='en')
print(i18n.t('foo'))
