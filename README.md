[contributors-shield]: https://img.shields.io/github/contributors/PentW0lf/EdRemover.svg?style=for-the-badge
[contributors-url]: https://github.com/PentW0lf/EdRemover/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PentW0lf/EdRemover.svg?style=for-the-badge
[forks-url]: https://github.com/PentW0lf/EdRemover/network/members
[stars-shield]: https://img.shields.io/github/stars/PentW0lf/EdRemover.svg?style=for-the-badge
[stars-url]: https://github.com/PentW0lf/EdRemover/stargazers
[issues-shield]: https://img.shields.io/github/issues/PentW0lf/EdRemover.svg?style=for-the-badge
[issues-url]: https://github.com/PentW0lf/EdRemover/issues

# EdRemover
A simple tool designed to remove empty folders from Android devices, helping to free up space and keep your file system organized.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


## Usage: 
1) Install termux on your android:
You can find it here (<a href = "https://play.google.com/store/apps/details?id=com.termux">Click here to download</a>).

```bash 
pkg remove game-repo -y
```
 
```bash
pkg remove science-repo -y
```

```bash
pkg update -y```

```bash termux-setup-storage
```

```bash 
pkg install git -y
```

```bash
pkg install python -y
```

```bash
cd $HOME
```

```bash
git clone https://github.com/PentW0lf/EdRemover
```

```bash 
cd EdRemover
```

```bash
chmod +x edremover.py
```

```bash
python edremover.py
```
