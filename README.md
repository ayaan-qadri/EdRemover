[contributors-shield]: https://img.shields.io/github/contributors/PentW0lf/EdRemover.svg?style=for-the-badge
[contributors-url]: https://github.com/PentW0lf/EdRemover/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PentW0lf/EdRemover.svg?style=for-the-badge
[forks-url]: https://github.com/PentW0lf/EdRemover/network/members
[stars-shield]: https://img.shields.io/github/stars/PentW0lf/EdRemover.svg?style=for-the-badge
[stars-url]: https://github.com/PentW0lf/EdRemover/stargazers
[issues-shield]: https://img.shields.io/github/issues/PentW0lf/EdRemover.svg?style=for-the-badge
[issues-url]: https://github.com/PentW0lf/EdRemover/issues

# EdRemover
This tool is made to remove empty folders from android phones.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


## Usage: 
1) Install termux on your android:
You can find it here (<a href = "https://play.google.com/store/apps/details?id=com.termux%22%3E">Click here to download</a>).
```sh
 pkg remove game-repo -y
 pkg remove science-repo -y
 pkg update -y
 termux-setup-storage
 pkg install git -y
 pkg install python -y
 cd $HOME
 git clone https://github.com/PentW0lf/EdRemover
 cd EdRemover
 chmod +x edremover.py
 python edremover.py
```
