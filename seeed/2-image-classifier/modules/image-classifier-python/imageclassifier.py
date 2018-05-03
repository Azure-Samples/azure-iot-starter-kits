import numpy as np
from PIL import Image
import tensorflow as tf


class ImageClassifier(object):

    def __init__(self, FLAGS):
        self.FLAGS = FLAGS

        # Creates graph from saved GraphDef.
        self.create_graph()
        # Creates node id --> English label lookup.
        self.label_map = self.create_label_map()

    def run_inference_on_image(self, image):
        """
        Runs image recognition on a .jpg image.  The image is received in a
        Flask http request, converted to a numpy array, reshaped to the required
        input shape for the Tensorflow MobileNet model, and run through the model.

        The output of the model is an array of prediction confidences for each
        class the model was trained against. The top K predictions are converted
        to human-readable labels with their prediction scores.
        """
        image_data = self.get_image_data(image)

        with tf.Session() as sess:
            output_tensor = sess.graph.get_tensor_by_name('MobilenetV2/Predictions/Reshape_1:0')
            predictions = sess.run(output_tensor, {'input:0': image_data})
            predictions = np.squeeze(predictions)

            top_k = predictions.argsort()[-self.FLAGS.num_top_predictions:][::-1]

            results = []
            for node_id in top_k:
                prediction = {
                    'label': self.label_map[node_id],
                    'score': predictions[node_id].astype(float),
                }
                results.append(prediction)

            return results

    def get_image_data(self, image):
        """
        Converts an image from a Flask http request to a numpy array in the
        shape used by the Tensorflow MobileNet model.
        """
        img = np.array(Image.open(image).resize((224,224))).astype(np.float) / 128 - 1
        return img.reshape(1,224,224,3)

    def create_graph(self):
        """
        Creates a graph from frozen GraphDef file.
        """
        with tf.gfile.FastGFile(self.FLAGS.model_path, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

    def create_label_map(self):
        """
        Create a dict mapping label id to human readable string.
        Returns:
            labels_to_names: dictionary where keys are integers from to 1000
            and values are human-readable names.
        We retrieve a synset file, which contains a list of valid synset labels used
        by ILSVRC competition. There is one synset one per line, eg.
                #   n01440764
                #   n01443537
        We also retrieve a synset_to_human_file, which contains a mapping from synsets
        to human-readable names for every synset in Imagenet. These are stored in a
        tsv format, as follows:
                #   n02119247    black fox
                #   n02119359    silver fox
        We assign each synset (in alphabetical order) an integer, starting from 1
        (since 0 is reserved for the background class).
        Code is based on
        https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_imagenet_data.py#L463
        """

        synset_list = [s.strip() for s in open(self.FLAGS.label_path).readlines()]
        synset_to_human_list = open(self.FLAGS.label_metadata_path).readlines()

        synset_to_human = {}
        for s in synset_to_human_list:
            parts = s.strip().split('\t')
            assert len(parts) == 2
            synset = parts[0]
            human = parts[1]
            synset_to_human[synset] = human

        label_index = 1
        labels_to_names = {0: 'background'}
        for synset in synset_list:
            name = synset_to_human[synset]
            labels_to_names[label_index] = name
            label_index += 1

        return labels_to_names
