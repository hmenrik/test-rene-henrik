<!DOCTYPE html>
<?php
function get_client_ip()
{
    // Header that is used by the proxy to refer to
    // the original IP
    $proxy_header = "HTTP_X_FORWARDED_FOR";

    // Get IP of the client behind proxy
    if (array_key_exists($proxy_header, $_SERVER)) {

        // Header can contain multiple IP-s of proxies that are passed through.
        // Only the IP added by the last proxy (last IP in the list) can be trusted.
        $client_ip = trim(end(explode(",", $_SERVER[$proxy_header])));

        return $client_ip;
    }
    // else {
    //     return "error"
    // }
}


<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Capio S:t Görans Sjukhus - IPTest</title>
    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/site.css" />
</head>
<body>
    <header>
    </header>
    <div class="container">
        <main role="main" class="pb-3">
            
<div class="jumbotron mt-4">
    <h1>Din IP-adress är:</h1>
    <h1 class="display-3">print get_client_ip();</h1>
</div>
<blockquote class="blockquote text-center">
    <p class="mb-0">
    Even the darkest night will end and the sun will rise
    </p>
    <footer class="blockquote-footer">
    Les Mis&#xE9;rables</footer>
</blockquote>
        </main>
    </div>


    
</body>
</html>


?>