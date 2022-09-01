# Computer Networking A Top Down Approach

## 15

End systems are connected together by a network of communication links and
packet switches. We’ll see in Section 1.2 that there are many types of
communication links, which are made up of different types of physical
media, including coaxial cable, copper wire, optical fiber, and radio
spectrum.

Packet Switch taks a packet arriving on one of its incoming communication links and forwards that packet on one of its outgoing communication links.

Two most prominent types are routers and link-layer switches.

## 20

A protocol defines the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.

## 23

Access network, the network that physically connects an end system (phone, PC) to the first router ("edge router") on a path from the end system to any other distance end system.

## 36

**Packet Loss** - congestion in the network, arriving packet find the output buffer/output queue completely full, then the arriving packet or one of the already-queued packets will be dropped.

## 41

Q: With packet switching, the probability that a specific user is active is 0.1
(that is, 10 percent). If there are 35 users, the probability that there are
11 or more simultaneously active users is approximately 0.0004.

A: binomial distribution with probability 0.1, number of trials 35, we want the probability of x>=11

```python
>>> from scipy.stats import binom
>>> sum([binom.pmf(i, 35, 0.1) for i in range(11, 36)])
0.0004242975954508265
```

## 109 - persistent tcp connection v.s. non-persistent

should each request/response pair be sent over a separate TCP connection, or should all of the requests and their corresponding responses be sent over the same TCP connection? In the former approach, the application is said to use **non-persistent connections**; and in the latter approach, **persistent connections**.

## 124 - Goal For HTTP/2

The primary goals for HTTP/2 are to reduce user-perceived latency by enabling request and response multiplexing over a *single* TCP connection, provide request prioritization and server push, and provide efficient compression of HTTP header fields. HTTP/2 does not change HTTP methods, status code, URLs, or header fields. Instead, HTTP/2 changes how the data is formatted and transported between the client and server.

## 126 - break down HTTP message to frames

The ability to break down an HTTP message into independent frames, interleave them, and then reassemble them on the other end is the single most important enhancement of HTTP/2. The framing is done by the framing sub-layer of the HTTP/2 protocol. When a server wants to send an HTTP response, the response is processed by the framing sub-layer, where it is broken down into frames. The header field of the response becomes one frame, and the body of the message is broken down into one for more additional frames. The frames of the response are then interleaved by the framing sub-layer in the server with the frames of other responses and sent over the single persistent TCP connection. As the frames arrive at the client, they are first reassembled into the original response messages at the framing sub-layer and then processed by the browser as usual. Similarly, a client’s HTTP requests are broken into frames and interleaved.  In addition to breaking down each HTTP message into independent frames, the framing sublayer also binary encodes the frames. Binary protocols are more efficient to parse, lead to slightly smaller frames, and are less error-prone.

## 197 - IP network-layer protocol v.s UDP and TCP Transport Layer

**IP**

IP deliver segments between communicating hosts.

**UDP and TCP**

- the fundamental respectabilities of UDP and TCP is to extend IP's delivery service between two end systems to a delivery service between two processes running on the end systems.
- UDP and TCP also provide integrity checking by including error-detection fields in their segments’ headers.

These two minimal transport-layer services,
1\. process-to-process data delivery
2\. error checking
are the only two services that UDP provides!

TCP also provides reliable **data transfer**, **congestion control**

## 198 - Demultiplexing vs Multiplexing

**Demultiplexing**

This job of delivering the data in a transport-layer segment to the correct
socket is called demultiplexing.

**Multiplexing**

The job of gathering data chunks at the source host from different sockets,
encapsulating each data chunk with header information (that will later be used
in demultiplexing) to create segments, and passing the segments to the network
layer is called multiplexing.

## 206 - Some applications are better suited for UDP

- finer application-level control over what data is sent, and when
  - TCP has congestion-control mechanism can throttles TCP sender when congested
  - TCP continue resend a segment until receipt of the segments has been acknowledged
  - real time applications do not want overly delay segment transmission
  - and can tolerate some data loss
- No connection establishment
  - TCL uses a three-way handshake before it starts to transfer data
  - UDP dpesn not introduce any delay to establish a connection
- No connection state
  - TCP maintains connection state in the end systems, including receive and send buffers, congestion-control parameters, and sequence and acknowledgment number parameters.
  - For this reason, server can support more active clients when the application runs over UDP rather than TCP
- Small packet header overhead
  - The TCP segment has 20 bytes of header overhead in every segment, whereas UDP has only 8 bytes of overhead.
