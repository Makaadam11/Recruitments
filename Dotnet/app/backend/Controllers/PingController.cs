using Microsoft.AspNetCore.Mvc;
using System;
using System.Threading.Tasks;

namespace backend.Controllers
{
    [ApiController]
    public class PingController : ControllerBase
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public PingController(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        [HttpGet]
        [Route("apiping")]
        public async Task<IActionResult> apiPing()
        {
            try
            {
                string apiUrl = "https://infra.devskills.app/lookup/api/1.0.0/ping";


                // Make a HTTP request
                var response = await _httpClientFactory.GetResponse(apiUrl);

                if (response.IsSuccessStatusCode)
                {
                    string responseContent = await response.Content.ReadAsStringAsync();
                    return Ok(responseContent);
                }
                else
                {
                    return StatusCode((int)response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                // Log ex or provide a more informative error message
                return BadRequest("An error occurred: " + ex.Message);
            }
        }

    }
}
