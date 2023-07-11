# Cheat Sheet Mitm

## Process of testing preview

- in terminal run `mitm-mobile-api` or `mitm-mobile-api-preview XXXX` (XXXX is the preview number)
  - preview would require vpn access
- update http proxy on iphone
  - with server ip `ip-local`
  - with port number 8081

## hotkeys

| key  | function        |
| ---- | --------------- |
| `e`  | export flow     |
| `zz` | clear all flows |

## export flow

1. use hotkey `e`
1. pick `raw` format which includes both request and response
