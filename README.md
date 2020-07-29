# ![youtube-dl-firefox-addon](./add-on/icons/YT_icon48.png) Youtube-dl Firefox Addon
 Firefox extension to download videos/audio from Youtube and others video websites using [youtube-dl](https://github.com/rg3/youtube-dl)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

 * [Description](#Description)
 * [Prerequisites](#prerequisites)
 * [Installation](#Installation)
 * [How to use this addon](#how-to-use-this-addon)
 * [Contributing](#Contributing)
 * [License](#license)

## Description

This is a firefox addon helping you downloads youtube videos or audio using [youtube-dl](https://github.com/rg3/youtube-dl).
Simply use the addon while browsing youtube to download the audio or video.

You can configure youtube-dl to download only audio, or convert into any desired format (mp3,wav,...) using FFMPEG, or download full video in any available quality, or even download full youtube playlists. 

The addon only display most commun format : m4a (Native audio format for YT), mp3(classical audio compression format) and mp4 (native vidéo format for YT)

## Prerequisites

1. Needs [python](https://www.python.org/downloads/windows/) installed. 
2. Needs [youtube-dl](https://github.com/rg3/youtube-dl) installed.
3. Needs [FFMPEG](https://ffmpeg.zeranoe.com/builds/) installed (needed to do mp3 conversion)
4. This has only been tested on Windows. Mac & Linux users might have to make some changes

## Installation

1. Clone this repo
2. Install the add on from [Firefox Addons Website](https://addons.mozilla.org/en-US/firefox/addon/youtube-dl-for-linux/). Or you can install the addon [command_runner-1.0-an+fx-linux.xpi](./command_runner-1.0-an+fx-linux.xpi?raw=true) from this repo to firefox by double-clicking.
3. Edit the file [firefox_command_runner.json](./app/firefox_command_runner.json) and edit the `path` to the location of the file `./app/firefox-command-runner.py` (i.e., where you cloned this repo to.).
4. Add a registry entry `firefox_command_runner.json` to the folder `/home/<username>/.mozilla/native-messaging-hosts/` (replace `<username>` wtih your own username. Create the folder if it does not exist).

## How to use this addon

1. Go to any youtube video page
1. Press the addon's logo in the toolbar once. (The logo looks like a YouTube icon).
1. The video will be downloaded automatically in the background.
1. After the download is finished, you will get a notification saying the download has finished. For the download locations, format, etc, please see youtube-dl's own [configuration](https://github.com/ytdl-org/youtube-dl#configuration)

## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## License

This program is Youtube Dl Firefox Addon
Copyright (C) 2020  Thibaut Decombe
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
