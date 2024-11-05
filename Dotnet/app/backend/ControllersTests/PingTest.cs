using backend.Controllers;
using Microsoft.AspNetCore.Mvc;
using Moq;
using NUnit.Framework; // Dodaj referencję do biblioteki NUnit
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

namespace backend.ControllersTests
{
    public class PingControllerTests
    {
        [Test] // Zmieniamy atrybut [Fact] na [Test]
        public async Task Get_ShouldReturnOk()
        {
            // Arrange
            var mockHttpClientService = new Mock<IHttpClientService>();
            var controller = new PingController(mockHttpClientService.Object);

            mockHttpClientFactory
                .Setup(x => x.CreateClient(It.IsAny<string>()))
                .Returns(mockHttpClient.Object);

            var controller = new PingController(mockHttpClientFactory.Object);

            // Simulate a successful HTTP response
            mockHttpClient
                .Setup(x => x.GetAsync(It.IsAny<string>()))
                .ReturnsAsync(new HttpResponseMessage
                {
                    StatusCode = HttpStatusCode.OK,
                    Content = new StringContent("Service is up and running."),
                });

            // Act
            var result = await controller.Get();

            // Assert
            Assert.IsInstanceOf<OkObjectResult>(result); // Zmieniamy Assert.IsType na Assert.IsInstanceOf
            var okResult = result as OkObjectResult;
            Assert.AreEqual("Service is up and running.", okResult.Value);
        }
    }
}
