# ![youtube-dl-firefox-addon](./add-on/icons/YTicon.png)Youtube-dl Firefox Addon
 Firefox extension to download videos/audio from Youtube and others using [youtube-dl](https://github.com/rg3/youtube-dl)

![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-green.svg)

## Table of Contents

 * [What Youtube Dl Firefox Addon does](#what-youtube-dl-firefox-addon-does)
 * [Prerequisites](#prerequisites)
 * [How to install Youtube Dl Firefox Addon](#how-to-install-youtube-dl-firefox-addon)
 * [How to use this addon](#how-to-use-this-addon)
 * [License](#license)

## What Youtube Dl Firefox Addon does

This is a firefox addon to which downloads youtube videos or audio using [youtube-dl](https://github.com/rg3/youtube-dl).

You can configure youtube-dl to download only audio, or convert into any desired format after installing, or even download full youtube playlists. These options are controlled via youtube-dl's own [configuration](https://github.com/ytdl-org/youtube-dl#configuration)

## Prerequisites

1. Needs [youtube-dl](https://github.com/rg3/youtube-dl) installed.
2. Needs [python](https://www.python.org/downloads/windows/) installed.
3. This has only been tested on Windows. Mac & Linux users might have to make some changes

## How to install Youtube Dl Firefox Addon

1. Clone this repo
2. Install the add on from [Firefox Addons Website](https://addons.mozilla.org/en-US/firefox/addon/youtube-dl-for-linux/). Or you can install the addon [command_runner-1.0-an+fx-linux.xpi](./command_runner-1.0-an+fx-linux.xpi?raw=true) from this repo to firefox by double-clicking.
3. Edit the file [firefox_command_runner.json](./app/firefox_command_runner.json) and edit the `path` to the location of the file `./app/firefox-command-runner.py` (i.e., where you cloned this repo to.).
4. Edit the [local youtube-dl config](config) to fit your needs or delete it to use youtube-dl's global configuration
5. Copy the file `firefox_command_runner.json` to the folder `/home/<username>/.mozilla/native-messaging-hosts/` (replace `<username>` wtih your own username. Create the folder if it does not exist).

## How to use this addon

1. Go to any youtube video page
1. Press the addon's logo in the toolbar once. (The logo looks like a YouTube icon).
1. The video will be downloaded automatically in the background.
1. After the download is finished, you will get a notification saying the download has finished. For the download locations, format, etc, please see youtube-dl's own [configuration](https://github.com/ytdl-org/youtube-dl#configuration)

## License

This program is Youtube Dl Firefox Addon
Copyright (C) 2020  Thibaut Decombe
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
