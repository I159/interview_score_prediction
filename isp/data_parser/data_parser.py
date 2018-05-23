import os

from pandas import read_csv


def parse_data_set():
    """docstring for parse_data_set"""
    path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)),
        'application_data.csv')
    res = read_csv(
        path,
        delimiter=',',
        names=[
            'applicationId',
            'candidateId',
            'invitationDate',
            'isRetake',
            'speechToText',
            'applicationTime',
            'videoLength',
            'score'
        ]
    )
    __import__('pdb').set_trace()
    return res
