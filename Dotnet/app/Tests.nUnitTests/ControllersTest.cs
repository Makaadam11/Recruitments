
using backend.Controllers;
using Microsoft.AspNetCore.Mvc;
using Moq;
using System.Net;

namespace Tests.nUnitTests
{
    [TestFixture]
    public class CreditDataControllersTests
    {
        private Mock<backend.IHttpClientFactory> _httpClientFactory;
        private CreditDataControllers _controller;

        [SetUp]
        public void Setup()
        {
            _httpClientFactory = new Mock<backend.IHttpClientFactory>();
            _controller = new CreditDataControllers(_httpClientFactory.Object);
        }

        [Test]
        public async Task GetCreditData_ReturnsOkResult()
        {
            // Arrange
            string ssn = "424-11-9327";
            string apiUrl = $"https://infra.devskills.app/lookup/api/1.0.0/credit-data/{ssn}";
            string responseContent = @"
            'CreditDataEmma': {
                'value': {
                    'first_name': 'Emma',
                    'last_name': 'Gautrey',
                    'address': '09 Westend Terrace',
                    'assessed_income': 60668,
                    'balance_of_debt': 11585,
                    'complaints': true
                }
            }    
            ";


            _httpClientFactory.Setup(client => client.GetResponse(apiUrl))
                .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK)
                {
                    Content = new StringContent(responseContent),
                });

            // Act
            var result = await _controller.GetCreditData(ssn);

            // Assert
            var okResult = (OkObjectResult)result;
            Assert.IsNotNull(okResult);
            Assert.AreEqual(responseContent, okResult.Value);
            Assert.AreEqual(200, okResult.StatusCode);
        }

        [Test]
        public async Task GetCreditData_ValidSsn_ReturnsOkResult()
        {
            // Arrange
            string ssn = "424-11-9327";
            string apiUrl = $"https://infra.devskills.app/api/credit-data/personal-details/{ssn}";
            string responseContent = @"
            'PersonalDetailsEmma': {
                'value': {
                    'first_name': 'Emma',
                    'last_name': 'Gautrey',
                    'address': '09 Westend Terrace'
                }
            }    
            ";


            _httpClientFactory.Setup(client => client.GetResponse(apiUrl))
                .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK)
                {
                    Content = new StringContent(responseContent),
                });

            // Act
            var result = await _controller.GetPersonalDetails(ssn);

            // Assert
            var okResult = (OkObjectResult)result;
            Assert.IsNotNull(okResult);
            Assert.AreEqual(responseContent, okResult.Value);
            Assert.AreEqual(200, okResult.StatusCode);
        }

        [Test]
        public async Task GetCreditData_DebtDetails_ReturnsOkResult()
        {
            // Arrange
            string ssn = "424-11-9327";
            string apiUrl = $"https://infra.devskills.app/api/credit-data/debt/{ssn}";
            string responseContent = @"
            'DebtDetailsEmma': {
                'value': {
                    'balance_of_debt': 11585,
                    'complaints': true
                }
            }
            ";

            _httpClientFactory.Setup(client => client.GetResponse(apiUrl))
                .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK)
                {
                    Content = new StringContent(responseContent),
                });

            // Act
            var result = await _controller.GetDebtDetails(ssn);

            // Assert
            var okResult = (OkObjectResult)result;
            Assert.IsNotNull(okResult);
            Assert.AreEqual(responseContent, okResult.Value);
            Assert.AreEqual(200, okResult.StatusCode);
        }
        [Test]
        public async Task GetCreditData_AssesedIncome_ReturnsOkResult()
        {
            // Arrange
            string ssn = "424-11-9327";
            string apiUrl = $"https://infra.devskills.app/api/credit-data/assessed-income/{ssn}";
            string responseContent = @"
            'AssessedIncomeDetailsEmma': {
                'value': {
                    'assessed_income': 60668
                }
            }
            ";

            _httpClientFactory.Setup(client => client.GetResponse(apiUrl))
                .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK)
                {
                    Content = new StringContent(responseContent),
                });

            // Act
            var result = await _controller.GetAssessedIncome(ssn);

            // Assert
            var okResult = (OkObjectResult)result;
            Assert.IsNotNull(okResult);
            Assert.AreEqual(responseContent, okResult.Value);
            Assert.AreEqual(200, okResult.StatusCode);
        }
    }
}
