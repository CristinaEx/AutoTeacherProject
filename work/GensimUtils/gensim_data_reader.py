import gensim
from gensim.models.keyedvectors import KeyedVectors

GENSIM_DATA_PATH = ''


def getGensimModel(file_path = GENSIM_DATA_PATH):
    """
    制作model，使用已经训练好的数据
    """
    model = KeyedVectors.load_word2vec_format(file_path, binary=False)  # C text format
    return model

if __name__ == '__main__':
    model = getGensimModel(GENSIM_DATA_PATH)
    # print(model.most_similar(['\c\en\Latin']))