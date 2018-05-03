namespace ImageClassifierCsharp
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using TensorFlow;

    /// <summary>
    /// Tensorflow image classifier.  Input is an image (as jpg encoded bytes) and
    /// runs it thorugh a Tensorflow image classification model to predict labels.
    /// </summary>
    public class ImageClassifier
    {
        private readonly TFGraph _graph;
        private readonly Dictionary<int, string> _labelMap;
        private readonly string _inputName;
        private readonly string _outputName;
        private readonly int _width;
        private readonly int _height;
        private readonly float _mean;
        private readonly float _scale;

        public ImageClassifier(
            string modelFile,
            string labelFile,
            string metadataFile,
            string input,
            string output,
            int width,
            int height,
            float mean,
            float scale)
        {
            // Load Tensorflow model.
            _graph = new TFGraph();
            _graph.Import(File.ReadAllBytes(modelFile));

            // Load labels.
            _labelMap = CreateLabelMap(labelFile, metadataFile);

            // Model parameters.
            _inputName = input ?? throw new ArgumentNullException(nameof(input));
            _outputName = output ?? throw new ArgumentNullException(nameof(output));
            _width = width;
            _height = height;
            _mean = mean;
            _scale = scale;
        }

        /// <summary>
        /// Classifies the image (jpg encoded bytes).  Returns the top 2 predicted labels along with their prediction confidences.
        /// </summary>
        public ImageClassification[] Classify(string name, byte[] image)
        {
            // Decode the jpg image bytes.
            using (var tensor = CreateTensorFromImage(image))
            using (var session = new TFSession(_graph))
            {
                // Configure Tensorflow session.
                var runner = session.GetRunner()
                    .AddInput(_graph[_inputName][0], tensor)
                    .Fetch(_graph[_outputName][0]);

                // Run classifier.
                var output = runner.Run();
                var result = (float[,])(output[0].GetValue());

                // Return top predicted labels.
                return GetPredictions(name, result);
            }
        }

        private ImageClassification[] GetPredictions(string name, float[,] scores)
        {
            // Join labels with predictions.
            var predictions = new ImageClassification[_labelMap.Count];
            for (int i = 0; i < predictions.Length; i++)
            {
                predictions[i] = new ImageClassification { Label = _labelMap[i], Score = scores[0, i] };
            }

            // Return the top 3 label predictions.
            return predictions.OrderByDescending(p => p.Score).Take(3).ToArray();
        }

        private TFTensor CreateTensorFromImage(byte[] contents, TFDataType dataType = TFDataType.Float)
        {
            // DecodeJpeg uses a scalar String-valued tensor as input.
            using (var tensor = TFTensor.CreateString(contents))
            using (var graph = ConstructGraphToNormalizeImage(out TFOutput input, out TFOutput output, dataType))
            using (var session = new TFSession(graph))
            {
                var normalized = session.Run(
                    inputs: new[] { input },
                    inputValues: new[] { tensor },
                    outputs: new[] { output });

                return normalized[0];
            }
        }

        // The inception model takes as input the image described by a Tensor in a very
        // specific normalized format (a particular image size, shape of the input tensor,
        // normalized pixel values etc.).
        //
        // This function constructs a graph of TensorFlow operations which takes as
        // input a JPEG-encoded string and returns a tensor suitable as input to the
        // inception model.
        private TFGraph ConstructGraphToNormalizeImage(out TFOutput input, out TFOutput output, TFDataType destinationDataType = TFDataType.Float)
        {
            var graph = new TFGraph();
            input = graph.Placeholder(TFDataType.String);

            output = graph.Cast(
                graph.Div(
                    x: graph.Sub(
                        x: graph.ResizeBilinear(
                            images: graph.ExpandDims(
                                input: graph.Cast(
                                    graph.DecodeJpeg(contents: input, channels: 3), DstT: TFDataType.Float),
                                dim: graph.Const(0, "make_batch")),
                            size: graph.Const(new int[] { _width, _height }, "size")),
                        y: graph.Const(_mean, "mean")),
                    y: graph.Const(_scale, "scale")), destinationDataType);

            return graph;
        }

        /// <summary>
        /// Create a dict mapping label id to human readable string.
        /// Returns:
        ///    labels_to_names: dictionary where keys are integers from to 1000
        ///    and values are human-readable names.
        /// We retrieve a synset file, which contains a list of valid synset labels used
        /// by ILSVRC competition. There is one synset one per line, eg.
        ///    #   n01440764
        ///    #   n01443537
        /// We also retrieve a synset_to_human_file, which contains a mapping from synsets
        /// to human-readable names for every synset in Imagenet. These are stored in a
        /// tsv format, as follows:
        ///    #   n02119247    black fox
        ///    #   n02119359    silver fox
        /// We assign each synset (in alphabetical order) an integer, starting from 1
        /// (since 0 is reserved for the background class).
        /// Code is based on
        /// https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_imagenet_data.py#L463
        /// </summary>
        private Dictionary<int, string> CreateLabelMap(string labelFile, string metadataFile)
        {
            var synset_list = File.ReadAllLines(labelFile);
            var synset_to_human_list = File.ReadAllLines(metadataFile);

            var synset_to_human = new Dictionary<string, string>();
            foreach (var s in synset_to_human_list)
            {
                var parts = s.Trim().Split('\t');
                var synset = parts[0];
                var human = parts[1];
                synset_to_human[synset] = human;
            }

            int label_index = 1;
            var labels_to_names = new Dictionary<int, string> { { 0, "background" } };
            foreach (var synset in synset_list)
            {
                var name = synset_to_human[synset];
                labels_to_names[label_index] = name;
                label_index++;
            }

            return labels_to_names;
        }
    }
}
