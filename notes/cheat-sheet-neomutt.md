# Cheat Sheet Neomutt

## Key bindings

| Command | Description |
| ------ | ------ |
| `*`   | Move to last entry   |
| `/`   | Search  |


## Find email sent from myself

Use limits, like filter, by hitting `l` and enter a search query

`~f myemail@gmail.com`

## Find email where subject contains a word

`/ foo`, better if you first filter the emails with limits above

## Generate Gmail password for Neomutt

I need to do this because I have setup 2 Factor Auth for gmail.

- Log into Gmail
- Click on your photo in the top right corner
- Click on the button “My Account“
- In the left menu bar click on “Sign into Google“
- Under “Password & sign-in method” (first block on the right side) click on “App passwords“
- You are required to login again
- From the drop down list “Select App” select the option “Mail“
- From the drop down list “Select Device” select the option “Other (Custom name)“
- Enter a name for the server, for example “my-vps“
- Click the button “Generate“
- The application specific password is generated, write it down in a safe place as it will only be displayed once

from [link](https://nidkil.me/2018/01/18/setting-up-mutt-to-send-mail-using-gmail-with-2fa-set/)

See also my [neomutt config](https://github.com/ynotstartups/dotfiles/blob/main/.neomutt_config)


## Macro With Literal Space

Use URL encoding

`macro index ga "<change-folder>=[Gmail]/All%20Mail<enter>"`

Credit to [stackoverflow](https://stackoverflow.com/a/14779416)

## Tag multiple emails

`T` - enter pattern to select multiple emails

`t` - tag multiple mail one by one

## Send email from command line

`echo "" | neomutt -s 'SUBJECT' foo@bar.com` 
