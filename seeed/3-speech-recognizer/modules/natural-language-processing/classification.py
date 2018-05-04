import sys
if sys.version_info < (3,0):
    import urllib as decoder
else:
    import urllib.parse as decoder

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config

import intent

class Classification(object):
    def __init__(self, training_data_file = "training_data.json",
                 config_file = "training_config.json"):
        training_data = load_data(training_data_file)        
        trainer = Trainer(config.load(config_file))
        self.interpreter = trainer.train(training_data)
        self.confidence_threshold = 0.7

        # Create supported intents
        context = { 'confidence_threshold': self.confidence_threshold }
        self.intents = {
                "greet"     : intent.HelloIntent(self, context),
                "get_time"  : intent.GetTimeIntent(self, context),
                "ask_joke"  : intent.JokeIntent(self, context),
                "unknown"   : intent.UnKnownIntent(self, context)
            }
        
    
    def handle(self, message):
        """
        Handles incoming message using trained NLU model and prints response to
        the system out
        Arguments:
            message the message from user to be handled with known intents 
            (greet, add_item, clear_list, show_items, _num_items)
        """
        intent = ""
        confidence = ""
        message = decoder.unquote(message)
        nlu_data = self.interpreter.parse(message)
        if 'intent' in nlu_data:
            if 'name' in nlu_data['intent']:
                intent = nlu_data['intent']['name']
                confidence = nlu_data['intent']['confidence']
        if confidence < self.confidence_threshold:
            return "I'm sorry! Could you please paraphrase?"
        if intent in self.intents:
            return self.intents[intent].execute(nlu_data)
