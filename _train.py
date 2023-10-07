import pickle
from bertopic import BERTopic

def train(docs):

    topic_model = BERTopic()
    topics, probs = topic_model.fit_transform(docs)

    with open("./tmp_data/topic_model.pkl", "wb") as f_out:
        pickle.dump(topic_model, f_out)

    print(topics)
    return topics