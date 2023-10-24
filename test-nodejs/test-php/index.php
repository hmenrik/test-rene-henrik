function get_client_ip()
{

    // Header that is used by the trusted proxy to refer to
    // the original IP
    $proxy_header = "HTTP_X_FORWARDED_FOR";

    // Get IP of the client behind proxy
    if (array_key_exists($proxy_header, $_SERVER)) {

        // Header can contain multiple IP-s of proxies that are passed through.
        // Only the IP added by the last proxy (last IP in the list) can be trusted.
        $client_ip = trim(end(explode(",", $_SERVER[$proxy_header])));

        // Validate just in case
        if (filter_var($client_ip, FILTER_VALIDATE_IP)) {
            return $client_ip;
        } else {
            // Validation failed - beat the guy who configured the proxy or
            // the guy who created the trusted proxy list?
            // TODO: some error handling to notify about the need of punishment
        }
    }

}

print get_client_ip();