# How Browser Works When You Enter a URL and Press Enter

There are 7 stages in this flow.

## Quick Map

1. Browser cache
2. OS cache / host file
3. DNS resolution
4. TCP handshake
5. TLS handshake
6. HTTP request and response
7. Rendering in the browser

<details>
<summary>Stage 1: Browser Cache</summary>

When you hit Enter on a URL, before making a request, the browser first searches its browser cache.
It checks whether you have visited `xyz.com` before and whether a cached response is still valid.

That is why a second visit often feels faster.

</details>

<details>
<summary>Stage 2: OS Cache / Host File</summary>

If the browser cache misses, it checks the OS cache and then the host file.
The host file usually contains manually mapped domain names and IP addresses.

</details>

<details>
<summary>Stage 3: DNS Resolution</summary>

If the OS cache also misses, DNS resolution starts.
It is a chain of 4 processes.

First, your browser asks the DNS resolver you are using for `google.com`, usually provided by your ISP or another DNS service.

Then the resolver asks the root server about the domain.
The root server replies with `.com`.
It only knows about TLD, which means Top-Level Domain.

Then it asks which server knows the Google IP.
The authoritative server for Google replies with the IP address of the site.

Now the resolver caches the result based on TTL, which means Time-to-Live.
Then it passes the result to the OS and finally to your browser.

</details>

<details>
<summary>Stage 4: TCP Handshake</summary>

It is a 3-way process.
First, a SYN packet is sent to say, hey, I want to connect to `google.com` or some other site.
Then the server sends a SYN-ACK message.
And then the client sends an ACK message.

Important: TCP is a transport layer protocol.
It mainly makes sure that data is delivered reliably and in order.

It does not know who we are talking to, and communications are not encrypted.
For that, TLS is used.

</details>

<details>
<summary>Stage 5: TLS Handshake</summary>

Google uses HTTPS, not HTTP, so after the TCP connection there is another encryption layer called TLS.

In this step, the server shares its SSL certificate.
"SSL certificates prove that yes, I am this site."

Then your OS checks whether the certificate is signed by a trusted CA, which means Certificate Authority.
If both sides agree, a session key is created and further communication becomes encrypted.

Browsers have built-in CA checks by default.

</details>

<details>
<summary>Stage 6: HTTP Request and Response</summary>

After the secure connection is ready, the browser sends the HTTP request.
The server responds with the frontend code files and other required data.

</details>

<details>
<summary>Stage 7: Rendering in the Browser</summary>

Now the browser processes the frontend code.
Then the result is shown to us in the form of the website we needed.

</details>


## Security Notes From an Attacker's Perspective

<details>
<summary>DNS Flooding</summary>

DNS flooding tries to overload the DNS server with too many requests.

</details>

<details>
<summary>Host File Poisoning / Prevention</summary>

One protection is checking whether the SSL certificate is signed by a trusted authority.
If it is not trusted, the request should be blocked.

</details>

<details>
<summary>SYN Flooding Based DDoS Attacks</summary>

In a SYN flooding attack, lakhs of SYN packets are pushed to the server but the final ACK message never arrives.
Because of this, the server allocates memory for half-open connections and can become overloaded.

</details>