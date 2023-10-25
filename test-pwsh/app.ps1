# web server
# requires admin rights
#requires -RunAsAdministrator
Try {
    $b =  New-Object System.Net.HttpListener
    $b.Prefixes.Add("http://+:8080/")
    [int]$nr = 0
    $b.Start()
    if ($b.IsListening) {'web server is running...'} else {break}
    while ($true) {
        $c = $b.GetContext()

        $out =  $c.Request.Headers.ToString()

        $c.Response.StatusCode = 200
        $c.Response.ContentType = 'text'

        $response = ((($out).Split("`n") | Select-String -Pattern 'x-forwarded-for:') -split ':')[1].Trim()
        # logga i console 
        write-host "loop:$nr ip:$response"
        
        # titta på alla headers jag kompletterar
        # $headers = $out -split "`r`n"
        # foreach ($header in $headers) {
        #     Write-Host $header
        # }

        # svara
        $responseBytes = [System.Text.Encoding]::UTF8.GetBytes($response)
        $c.Response.OutputStream.Write($responseBytes, 0, $responseBytes.Length)
        $c.Response.Close()
        $nr++
    }
} Catch {
    Write-Host "Error: $($_.Exception.Message)"
}
