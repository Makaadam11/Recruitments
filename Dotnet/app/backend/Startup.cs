using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Text;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Diagnostics.HealthChecks;
using Microsoft.AspNetCore.Http;

namespace backend
{
    public interface IHttpClientFactory
    {
        HttpClient CreateClient();
        Task<HttpResponseMessage> GetResponse(string url);
    }

    public class HttpClientFactory : IHttpClientFactory
    {
        private readonly HttpClient _httpClient;

        public HttpClientFactory(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<HttpResponseMessage> GetResponse(string url)
        {
            return await _httpClient.GetAsync(url);
        }

        public HttpClient CreateClient()
        {
            return new HttpClient();
        }
    }

    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method is called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddHttpClient();
            services.AddScoped<IHttpClientFactory, HttpClientFactory>();

            // Add controller handling
            services.AddControllers();
        }

        // This method is called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                // If we're in development mode, you can add additional settings, such as error handling.
                app.UseDeveloperExceptionPage();
            }
            else
            {
                // In production mode, you can add general error handling for the application.
                app.UseExceptionHandler("/Home/Error");
                app.UseHsts();
            }

            // Use routing
            app.UseRouting();

            // For the /ping endpoint
            app.Run(async (context) =>
            {
                if (context.Request.Path == "/ping")
                {
                    await context.Response.WriteAsync("The service is up and running.");
                }
            });

            // Add endpoint handling for controllers
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home},{action=Index}/{id?}");
                endpoints.MapControllerRoute(
                    name: "debt",
                    pattern: "/debt/424-11-9327");
                endpoints.MapControllerRoute(
                    name: "personal-details",
                    pattern: "/personal-details/424-11-9327");
                endpoints.MapControllerRoute(
                    name: "assessed-income",
                    pattern: "/assessed-income/424-11-9327");
            });

            // For the /apiping endpoint
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "ping",
                    pattern: "/apiping");
            });

            // For the /credit-data endpoint
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "credit-data",
                    pattern: "/credit-data/424-11-9327");
            });
        }
    }
}
