# Cheat Sheet Docker

## Notes - Docker In Action

Docker builds containers using 10 major system features.

1. PID namespace - Process identifiers and capabilities
1. UTS namespace - Host and domain name
1. MNT namespace - Filesystem access and structure
1. IPC namespace - Process communication over shared memory
1. USR namespace - Use names and identifiers
1. chroot syscall - Controls the location of the filesystem root
1. cgroups - Resource protection
1. CAP drop - operating system feature restrictions
1. Security modules - Mandatory access controls
