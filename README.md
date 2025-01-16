<a id="readme-top"></a>
<p align="center">
  <a href="https://theblockheads.net">
    <img alt="The Blockheads" src="https://github.com/user-attachments/assets/8f162932-0a4d-429d-9f3e-bd97d980e893">
  </a>
</p>
<div align="center">
  <h1 align="center">The Blockheads Game Server
  
  [![CI Workflow](https://img.shields.io/github/actions/workflow/status/JonCastaway/BHS/cicd.yml?branch=main&label=CI&logo=github)](https://github.com/JonCastaway/BHS/actions/workflows/cicd.yml)

</h3>
<div align="center">
  <h2> 
    <a href="https://www.apple.com/macos/" target="_blank" rel="noopener noreferrer" title="MacOS" style="color: #000000;">
      <img src="https://img.shields.io/badge/MacOS-999999.svg?logo=apple&logoColor=white" alt="MacOS">
    </a>
    <a href="https://www.debian.org/" target="_blank" rel="noopener noreferrer" title="Debian" style="color: #A81D33;">
      <img src="https://img.shields.io/badge/Debian-A81D33.svg?logo=debian&logoColor=white" alt="Debian">
    </a>
    <a href="https://ubuntu.com/" target="_blank" rel="noopener noreferrer" title="Ubuntu" style="color: #E95420;">
      <img src="https://img.shields.io/badge/Ubuntu-E95420.svg?logo=ubuntu&logoColor=white" alt="Ubuntu">
    </a>
    <a href="https://archlinux.org/" target="_blank" rel="noopener noreferrer" title="Arch Linux" style="color: #1793D1;">
      <img src="https://img.shields.io/badge/Arch%20Linux-1793D1.svg?logo=arch-linux&logoColor=white" alt="Arch Linux">
    </a>
    <a href="https://pop.system76.com/" target="_blank" rel="noopener noreferrer" title="Pop!_OS" style="color: #48B9C7;">
      <img src="https://img.shields.io/badge/Pop!__OS-48B9C7.svg?logo=pop_os&logoColor=white" alt="Pop!_OS">
    </a>
    <a href="https://www.linuxmint.com/" target="_blank" rel="noopener noreferrer" title="Linux Mint" style="color: #87CF3E;">
      <img src="https://img.shields.io/badge/Linux%20Mint-87CF3E.svg?logo=linux-mint&logoColor=white" alt="Linux Mint">
    </a>
    <a href="https://elementary.io/" target="_blank" rel="noopener noreferrer" title="elementary OS" style="color: #64BAFF;">
      <img src="https://img.shields.io/badge/elementary%20OS-64BAFF.svg?logo=elementary&logoColor=white" alt="elementary OS">
    </a>
    <a href="https://www.kali.org/" target="_blank" rel="noopener noreferrer" title="Kali Linux" style="color: #557C94;">
      <img src="https://img.shields.io/badge/Kali%20Linux-557C94.svg?logo=kali-linux&logoColor=white" alt="Kali Linux">
    </a>
  </h2>
</div> 
</h3>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<p align="center">This repository contains the server files for running a Blockheads multiplayer server.</p>
<div align="left"><b>Warning:</b></div>
<div align="left">Running curl to bash scripts from the internet can be risky. It's always recommended to review the code before executing it to ensure it is safe and does not contain any malicious content.</div><p></p>
<a href="https://github.com/JonCastaway/BHS/wiki"><strong>Explore the Wiki</strong></a>
<br />
<br />

<a href="https://github.com/JonCastaway/BHS/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
·
<a href="https://github.com/JonCastaway/BHS/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
<summary>Table of Contents</summary>
<ol>
    <li><a href="#1-installation--linux">Linux Install</a></li>
    <li><a href="#2-installation--macos">MacOS Install</a></li>
    <li><a href="#3-original-binaries--manual-install">Manual Install</a></li>
    <li><a href="#4-The-Blockheads--Android-APK">The Android Apps</a></li>
    <li><a href="#5-roadmap">Roadmap</a></li>
    <li><a href="#6-contributing">Contributing</a></li>
    <li><a href="#7-license">License</a></li>
    <li><a href="#8-contact">Contact</a></li>
    <li><a href="#9-Acknowledgments">Acknowledgments</a></li>
</ol>


# The Blockheads Game Server for Linux and MacOS

## Getting Started

![GettingStarted](https://github.com/user-attachments/assets/181856ca-8597-43d3-97c4-cf13a99c924d)

### 1. Installation | Linux

Follow the instructions below to install and set up the Blockheads server on your system.

Download and run the server script:
```bash
curl -sL https://raw.githubusercontent.com/JonCastaway/BHS/main/start.sh | bash -s -
```

Create Your server:
```bash
./blockheads_server171 -n MyFirstServer
```

For more options and help use:
```bash
./blockheads_server171 -h
```

Configure Your server:
`You'll need to replace the WORLD_ID and PORT inside the run.sh script.`

```bash
nano run.sh
```

`Replace the placeholders with your WORLD_ID and PORT. You can find your WORLD_ID by typing:`

```bash
./blockheads_server171 -l
```

`Save and exit the file by pressing CTRL+X, then Y, and ENTER.`

### 2. Installation | MacOS

Download the Blockheads Server App

[Download from App Store](https://apps.apple.com/us/app/blockheadsserver/id662633568)

### 3. Original Server Binaries | Manual Install

You can download the original server binaries from the links below

- [Download The Blockheads Server Binary - archive.org](https://archive.org/download/BHSv171/blockheads_server171.tar.gz)
- [Download The Blockheads Server Binary - majicdave.com](https://majicdave.com/share/blockheads_server171.tar.gz)

### 4. The Blockheads | Android APK

If version 1.76 does not launch, try an earlier version such as 1.75 or 1.74

- [Download The Original Blockheads Android APK v1.76 - Noodlecake](https://noodlecake.com/wp-content/uploads/2021/02/theblockheads1.7.6.apk)
  
- [Download The Original Blockheads Android APK v1.76 - archive.org](https://archive.org/download/theblockheads1.7.6/theblockheads1.7.6.apk)
- [Download The Original Blockheads Android APK v1.75 - archive.org](https://archive.org/download/theblockheads1.7.6/The%20Blockheads_1.7.5_APKPure.apk)
- [Download The Original Blockheads Android APK v1.74 - archive.org](https://archive.org/download/theblockheads1.7.6/The%20Blockheads_1.7.4_APKPure.apk)

### 5. Roadmap
![roadmap](https://github.com/user-attachments/assets/9a17a313-51d8-49f5-9f0c-ada12de1ced5)

Exlore our advancement towards significant [milestones](<[url](https://github.com/Joncastaway/BHS/milestones)>), and delve into the [wiki](https://github.com/Joncastaway/BHS/wiki/Roadmap). Here's a general outline of some key features we're considering:

-   [ ] Web-based User Interface
-   [ ] World Configuration Editor

Additionally, review the [open issues](https://github.com/Joncastaway/BHS/issues) for a comprehensive list of suggested features (as well as known issues).

### 6. Contributing

![contributing](https://github.com/user-attachments/assets/5059e3bc-ea8c-4965-96c4-c6c500d0ba06)

Contributions are welcome! Feel free to fork this repository and submit pull requests.

#### Contributors
<a href="https://github.com/JonCastaway/BHS/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JonCastaway/BHS&t=1" />
</a>

### 7. License

This project is Licensed under the GPL-3.0 License. See the [License](https://github.com/JonCastaway/BHS/blob/main/LICENCE) file for details.

### 8. Contact

![contact](https://github.com/user-attachments/assets/2b40e187-309b-4a58-be5f-fc71d045298a)

For any questions or support, please reach out or open an issue on GitHub.

[contributors-shield]: https://img.shields.io/github/contributors/JonCastaway/BHS.svg?style=for-the-badge
[contributors-url]: https://github.com/JonCastaway/BHS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JonCastaway/BHS.svg?style=for-the-badge
[forks-url]: https://github.com/JonCastaway/BHS/network/members
[stars-shield]: https://img.shields.io/github/stars/JonCastaway/BHS.svg?style=for-the-badge
[stars-url]: https://github.com/JonCastaway/BHS/stargazers
[issues-shield]: https://img.shields.io/github/issues/JonCastaway/BHS.svg?style=for-the-badge
[issues-url]: https://github.com/JonCastaway/BHS/issues

### 9. Acknowledgments

<!-- - [NAME](URL) --> Projects we're inspired by and obtained valuable information:

-   [Majic Jungle | Dave Frampton](https://majicjungle.com)
-   [The Internet Archive](https://archive.org)
-   [Discord | Sapiens](https://discord.gg/ZHwMWruM)
-   [Reddit | r/blockheads](https://www.reddit.com/r/blockheads/)
-   [Wiki GG | Blockheads](https://theblockheads.wiki.gg/wiki/The_Blockheads_Wiki)
-   [Fandom | The Blockheads](https://theblockheads.fandom.com/wiki)
