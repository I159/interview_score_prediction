"""
Data architecture specific application

Data set column names, data transformations. Also exact learn and prediction
operation with exact data set file and incoming request data.
"""
from data_set_preprocessor import data_set_preprocessor as dpp
from model_builder import model_builder as mb


SCORE = 'score'
DATE = 'invitationDate'
APPLICATION_TIME = 'applicationTime'
IS_RETAKE = 'isRetake'
SPEACH = 'speechToText'
BOW_FIELD = 'name'

DATA_SET_FILE = 'application_data.csv'


def parse_data_set():
    data_set = dpp.parse_csv(DATA_SET_FILE)
    data_set = dpp.int_to_binary(data_set, SCORE)
    data_set = dpp.datetime_to_timestamp(data_set, DATE, APPLICATION_TIME)
    data_set = dpp.bool_to_num(data_set, IS_RETAKE)
    data_set = dpp.drop_unnamed(data_set)
    data_set = dpp.json_to_bag_of_words(data_set, SPEACH, BOW_FIELD)
    data_set = dpp.tag_words(data_set, SPEACH, SCORE)
    return data_set


def predict():
    data_set = parse_data_set()
    mb.learn(data_set, SPEACH)
    return
