from homework3.task3 import make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     },
     {
        "type": "person", "name": "Bill"
     }
]


def test_one_position_correct():
    """If find one correct position"""
    assert make_filter(name='polly', type='bird').apply(sample_data) == [
        {'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}
    ]


def test_all_correct_position():
    """If one and more position correct filter"""
    assert make_filter(type='person', name='Bill').apply(sample_data) == [
        {'name': 'Bill', 'last_name': 'Gilbert', 'occupation': 'was here',
         'type': 'person'}, {'type': 'person', 'name': 'Bill'}
    ]


def test_change_arguments():
    assert make_filter(name='Bill', type='person').apply(sample_data) == [
        {'name': 'Bill', 'last_name': 'Gilbert', 'occupation': 'was here',
         'type': 'person'}, {'type': 'person', 'name': 'Bill'}
    ]


def test_negative():
    assert make_filter(name='Jack', kind='R').apply(sample_data) == []
