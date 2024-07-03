def get_user_search_fields(request_args):
    return [
        {
            'type': 'text',
            'name': 'name',
            'id': 'name',
            'label': '이름',
            'value': request_args.get('name', '')
        },
        {
            'type': 'select',
            'name': 'gender',
            'id': 'gender',
            'label': '성별',
            'options': [
                {'value': '', 'label': '', 'selected': request_args.get('gender', '') == ''},
                {'value': '여성', 'label': '여성', 'selected': request_args.get('gender', '') == '여성'},
                {'value': '남성', 'label': '남성', 'selected': request_args.get('gender', '') == '남성'}
            ]
        },
        {
            'type': 'number',
            'name': 'age',
            'id': 'age',
            'label': '나이',
            'value': request_args.get('age', '')
        }
    ]

def get_item_search_fields(request_args):
    return [
        {
            'type': 'text',
            'name': 'name',
            'id': 'name',
            'label': '상품명',
            'value': request_args.get('name', '')
        },
        {
            'type': 'select',
            'name': 'type',
            'id': 'type',
            'label': '종류',
            'options': [
                {'value': '', 'label': '', 'selected': request_args.get('gender', '') == ''},
                {'value': '커피', 'label': '커피', 'selected': request_args.get('gender', '') == '커피'},
                {'value': '주스', 'label': '주스', 'selected': request_args.get('gender', '') == '주스'},
                {'value': '케이크', 'label': '케이크', 'selected': request_args.get('gender', '') == '케이크'}
            ]
        }
    ]

def get_store_search_fields(request_args):
    return [
        {
            'type': 'text',
            'name': 'name',
            'id': 'name',
            'label': '매장명',
            'value': request_args.get('name', '')
        },
                {
            'type': 'select',
            'name': 'type',
            'id': 'type',
            'label': '브랜드 타입',
            'options': [
                {'value': '', 'label': '', 'selected': request_args.get('gender', '') == ''},
                {'value': '스타벅스', 'label': '스타벅스', 'selected': request_args.get('gender', '') == '스타벅스'},
                {'value': '투썸', 'label': '투썸', 'selected': request_args.get('gender', '') == '투썸'},
                {'value': '이디야', 'label': '이디야', 'selected': request_args.get('gender', '') == '이디야'},
                {'value': '커피빈', 'label': '커피빈', 'selected': request_args.get('gender', '') == '커피빈'}
            ]
        }
    ]
