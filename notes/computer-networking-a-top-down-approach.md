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
