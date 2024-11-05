using backend.Controllers;
using Microsoft.AspNetCore.Mvc;
using Moq;
using System.Net;
namespace Test.nUnitTests
{

    [TestFixture]
    public class PingControllerTests
    {
        private Mock<backend.IHttpClientFactory> _httpClientFactory;
        private PingController _controller;

        [SetUp]
        public void Setup()
        {
            _httpClientFactory = new Mock<backend.IHttpClientFactory>();
            _controller = new PingController(_httpClientFactory.Object);
        }

        [Test]
        public async Task Ping_ReturnsOkResultWhenHttpClientSucceeds()
        {
            // Arrange
            var responseContent = "{ \"description\": \"The service is up and running.\" }";
            string apiUrl = $"https://infra.devskills.app/lookup/api/1.0.0/ping";

            _httpClientFactory.Setup(client => client.GetResponse(apiUrl))
                .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK)
                {
                    Content = new StringContent(responseContent),
                });

            // Act
            var result = await _controller.apiPing();

            // Assert
            var okResult = result as OkObjectResult;
            Assert.IsNotNull(okResult);
            Assert.AreEqual(responseContent, okResult.Value);
            Assert.AreEqual(200, okResult.StatusCode);
        }
        public class FakeHttpMessageHandler : HttpMessageHandler
        {
            private readonly HttpResponseMessage _response;

            public FakeHttpMessageHandler(HttpResponseMessage response)
            {
                _response = response;
            }

            protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
            {
                return Task.FromResult(_response);
            }
        }
    }
}
