class C:
    print('Class declared')
    if True:
        print('Still not over')
    # 클래스 레벨에서도 if statement같이 로직을 적용할 수 있다
    # 설정 데이터같은 것들을 클래스에서 관리할 때 유용하다
    # -> 'USE_LOCAL_DB'라는 환경 변수가 존재하면 mysql host를 localhost로 설정한다거나 하는 등
