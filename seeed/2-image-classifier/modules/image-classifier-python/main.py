import argparse
import imageclassifier
from flask import Flask, request, jsonify


classifier = None

# Start web server
application = Flask(__name__)

@application.route('/classify', methods=['POST'])
def classify_image():
    file = request.files['image']
    result = classifier.run_inference_on_image(file)
    return jsonify(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_path',
        type=str,
        default='/model/mobilenet_v2_1.0_224_frozen.pb',
        help='Path to frozen GraphDef model'
    )
    parser.add_argument(
        '--label_path',
        type=str,
        default='/model/imagenet_lsvrc_2015_synsets.txt',
        help='Path to labels (node ids) used in the model.'
    )
    parser.add_argument(
        '--label_metadata_path',
        type=str,
        default='/model/imagenet_metadata.txt',
        help='Path to file with node ids -> human readable string.'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port for http server to listen on.'
    )
    parser.add_argument(
        '--num_top_predictions',
        type=int,
        default=3,
        help='Return this many predictions.'
    )
    FLAGS, unparsed = parser.parse_known_args()

    # Create MobileNet image classifier.
    classifier = imageclassifier.ImageClassifier(FLAGS)

    application.run(host='0.0.0.0', port=FLAGS.port)
