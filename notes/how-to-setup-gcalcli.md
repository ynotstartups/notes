# How To Setup gcalcli

1. `sudo apt-get install gcalcli`
1. try `gcalcli list` to invoke default oauth2 but failed
1. create [my own Calendar API instead](https://github.com/insanum/gcalcli#login-information)
1. create `~/.gcalclirc` with `--client-secret` and `--client-id`
1. add `--default-calendar` to select only my calendar in `~/.gcalclirc`
