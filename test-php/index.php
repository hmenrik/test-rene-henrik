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
    else {
        return "error"
    }
}

print get_client_ip();