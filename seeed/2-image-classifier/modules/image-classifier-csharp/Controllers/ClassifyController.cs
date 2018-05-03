namespace ImageClassifierCsharp
{
    using System;
    using System.IO;
    using System.Linq;
    using System.Net;
    using System.Net.Http;
    using System.Text;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Http;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.Logging;

    [Route("[controller]")]
    public class ClassifyController : Controller
    {
        private readonly ImageClassifier _classifier;
        private readonly ILogger _logger;

        public ClassifyController(ImageClassifier classifier, ILogger logger)
        {
            _classifier = classifier;
            _logger = logger;
        }

        // POST classify
        [HttpPost]
        public async Task<IActionResult> Classify([FromForm] IFormFile image)
        {
            try
            {
                using (var stream = new MemoryStream((int)image.Length))
                {
                    await image.CopyToAsync(stream);
                    var imageBytes = stream.GetBuffer();

                    // Classify image.
                    var predictions = _classifier.Classify(image.FileName, imageBytes);

                    // Display the prediction.
                    var prediction = predictions.First();
                    Console.WriteLine($"[{DateTimeOffset.UtcNow.ToString("u")}] Classification prediction: {prediction.Label} with probability {prediction.Score:0.00}");

                    // Return response.
                    return Ok(predictions);
                }
            }
            catch (Exception e)
            {
                _logger.LogError($"Unexpected exception: {e}");
                return StatusCode((int)HttpStatusCode.InternalServerError, e.Message);
            }
        }
    }
}
