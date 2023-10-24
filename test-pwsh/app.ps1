$b =  New-Object System.Net.HttpListener
$b.Prefixes.Add("http://+:8080/")
while ($true) {
 $b.Start()
 $c = $b.GetContext()

 $c.Request.HttpMethod
 $c.Request.Url
 $out =  $c.Request.Headers.ToString()

 $c.Response.StatusCode = 200
 $c.Response.ContentType = 'text'

 $response = ((($out).Split("`n") | Select-String -Pattern 'x-forwarded-for:') -split ':')[1].Trim()
 $responseBytes = [System.Text.Encoding]::UTF8.GetBytes($response)
 $c.Response.OutputStream.Write($responseBytes, 0, $responseBytes.Length)
 $c.Response.Close()
}

