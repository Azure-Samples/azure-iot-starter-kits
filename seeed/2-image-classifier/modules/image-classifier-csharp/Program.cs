namespace ImageClassifierCsharp
{
    using System;
    using Microsoft.AspNetCore;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.Extensions.Configuration;

    class Program
    {
        static void Main(string[] args)
        {
			BuildWebHost(args).Run();
        }

		public static IWebHost BuildWebHost(string[] args)
		{
			var config = new ConfigurationBuilder()
				.AddCommandLine(args)
				.Build();

			return WebHost.CreateDefaultBuilder(args)
				.UseKestrel()
				.UseConfiguration(config)
				.UseStartup<Startup>()
				.Build();
		}
    }
}
