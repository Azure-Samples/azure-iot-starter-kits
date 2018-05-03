namespace ImageClassifierCsharp
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Logging;
    using Microsoft.Extensions.Options;

    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();

            var logger = CreateLogger();
            services.AddSingleton(logger);

            var classifier = CreateClassifier();
            services.AddSingleton(classifier);
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseMvc();
        }

        private ILogger CreateLogger()
        {
            return new LoggerFactory()
                .AddConsole()
                .CreateLogger("image-classifier-csharp");
        }

        private ImageClassifier CreateClassifier()
        {
            return new ImageClassifier(
                modelFile: "/model/mobilenet_v2_1.0_224_frozen.pb",
                labelFile: "/model/imagenet_lsvrc_2015_synsets.txt",
                metadataFile: "/model/imagenet_metadata.txt",
                input: "input",
                output: "MobilenetV2/Predictions/Reshape_1",
                width: 224,
                height: 224,
                mean: 1,
                scale: 128);
        }
    }
}
