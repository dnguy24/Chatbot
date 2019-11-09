from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Interpreter, Trainer
from rasa_nlu import config
import json
from rasa_nlu.test import run_evaluation


def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'nlu_model')
    return model_directory


model_directory =  train("data/nlu.md", "config.yml", 'models/nlu')
#
#
# def ask_question(text):
#     print(text)
#     interpreter = Interpreter.load(model_directory)
#     t = interpreter.parse(text)
#     print(json.dumps(t, indent=2))
#
#
# ask_question("How do I get to Douglass")


result = run_evaluation("./data/nlu.md", model_directory, confmat_filename="trainresult.png")

# print(result["intent_evaluation"]['report'])
