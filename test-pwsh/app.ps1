# Import the necessary modules
Import-Module Net.Http
Import-Module System.Net.HttpListener

# Create a new web server
$webServer = New-Object System.Net.HttpListener

# Add a request handler that returns a simple HTML page
$webServer.AddPrefix("http://localhost:8080/")
$webServer.Prefixes.Add("http://localhost:8080/").RequestReceived += {
    $response = New-Object System.Net.Http.HttpResponseMessage
    $response.Content = New-Object System.Net.Http.StringContent("Hello from PowerShell on Linux!", "text/html")
    $response.StatusCode = HttpStatusCode.OK
    $webServer.Context.Response = $response
}

# Start the web server
$webServer.Start()

# Display a message to the user
Write-Host "Web server is running on http://localhost:8080/"

# Wait for the user to press Enter
Read-Host -Prompt "Press Enter to stop the web server..."

# Stop the web server
$webServer.Stop()
