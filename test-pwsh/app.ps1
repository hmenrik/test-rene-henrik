$b =  New-Object System.Net.HttpListener
$b.Prefixes.Add("http://+:8088/")
while ($true) {
 $b.Start()
 $c = $b.GetContext()

 $c.Request.HttpMethod
 $c.Request.Url
 $out =  $c.Request.Headers.ToString()

 $c.Response.StatusCode = 200
 $c.Response.ContentType = 'text'

 $responseJson = "$($out -match 'x-forwarder-for')"
 $responseBytes = [System.Text.Encoding]::UTF8.GetBytes($responseJson)
 $c.Response.OutputStream.Write($responseBytes, 0, $responseBytes.Length)
 $c.Response.Close()
}
#$b.stop()
