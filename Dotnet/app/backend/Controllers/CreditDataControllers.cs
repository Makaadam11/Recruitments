using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace backend.Controllers
{
    [ApiController]
    public class CreditDataControllers : ControllerBase
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public CreditDataControllers(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        [HttpGet("credit-data/{ssn}")]
        public async Task<IActionResult> GetCreditData(string ssn)
        {
            try
            {
                // URL address of the Lookup Service
                string apiUrl = $"https://infra.devskills.app/lookup/api/1.0.0/credit-data/{ssn}";

                // Send a GET request
                HttpResponseMessage response = await _httpClientFactory.GetResponse(apiUrl);

                // Check if the response is successful (status 200 OK)
                if (response.IsSuccessStatusCode)
                {
                    // Get the response content as text
                    string responseContent = await response.Content.ReadAsStringAsync();
                    return Ok(responseContent);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    return NotFound();
                }
                else
                {
                    return StatusCode((int)response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                return BadRequest(ex.Message);
            }
        }

        [HttpGet("personal-details/{ssn}")]
        public async Task<IActionResult> GetPersonalDetails(string ssn)
        {
            try
            {
                // URL address of the Credit Data API
                string apiUrl = $"https://infra.devskills.app/api/credit-data/personal-details/{ssn}";

                // Send a GET request to Personal Details
                HttpResponseMessage response = await _httpClientFactory.GetResponse(apiUrl);

                // Check if the response is successful (status 200 OK)
                if (response.IsSuccessStatusCode)
                {
                    // Get the response content as text
                    string responseContent = await response.Content.ReadAsStringAsync();
                    return Ok(responseContent);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    return NotFound();
                }
                else
                {
                    return StatusCode((int)response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                return BadRequest(ex.Message);
            }
        }

        [HttpGet("assessed-income/{ssn}")]
        public async Task<IActionResult> GetAssessedIncome(string ssn)
        {
            try
            {
                // URL address of the Credit Data API
                string apiUrl = $"https://infra.devskills.app/api/credit-data/assessed-income/{ssn}";

                // Send a GET request to Assessed Income Details
                HttpResponseMessage response = await _httpClientFactory.GetResponse(apiUrl);

                // Check if the response is successful (status 200 OK)
                if (response.IsSuccessStatusCode)
                {
                    // Get the response content as text
                    string responseContent = await response.Content.ReadAsStringAsync();
                    return Ok(responseContent);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    return NotFound();
                }
                else
                {
                    return StatusCode((int)response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                return BadRequest(ex.Message);
            }
        }

        [HttpGet("debt/{ssn}")]
        public async Task<IActionResult> GetDebtDetails(string ssn)
        {
            try
            {
                // URL address of the Credit Data API
                string apiUrl = $"https://infra.devskills.app/api/credit-data/debt/{ssn}";

                // Send a GET request to Debt Details
                HttpResponseMessage response = await _httpClientFactory.GetResponse(apiUrl);

                // Check if the response is successful (status 200 OK)
                if (response.IsSuccessStatusCode)
                {
                    // Get the response content as text
                    string responseContent = await response.Content.ReadAsStringAsync();
                    return Ok(responseContent);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    return NotFound();
                }
                else
                    return StatusCode((int)response.StatusCode);
            }
            catch (Exception ex)
            {
                return BadRequest(ex.Message);
            }
        }
    }
}

