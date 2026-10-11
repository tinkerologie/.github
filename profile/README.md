<div align="center">

<img src="https://avatars.githubusercontent.com/u/340790272?v=4" width="120" alt="Tinkerologie logo" />

# Tinkerologie

**Open-source tinkering for the smart home and the home lab.**

Home Assistant integrations · Homebridge plugins · Unraid plugins · async Python & Go libraries

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-integrations-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white)](#-home-assistant-integrations)
[![Homebridge](https://img.shields.io/badge/Homebridge-plugins-491F59?style=for-the-badge&logo=homebridge&logoColor=white)](#-homebridge-plugins)
[![Unraid](https://img.shields.io/badge/Unraid-plugins-F15A2C?style=for-the-badge&logo=unraid&logoColor=white)](#%EF%B8%8F-unraid-plugins)
[![Libraries](https://img.shields.io/badge/Libraries-Python%20%26%20Go-3776AB?style=for-the-badge&logo=python&logoColor=white)](#-libraries)

[![Sponsor](https://img.shields.io/github/sponsors/ruaan-deysel?style=flat-square&logo=githubsponsors&label=Sponsor&color=EA4AAA)](https://github.com/sponsors/ruaan-deysel)
![Location](https://img.shields.io/badge/Made%20in-Australia-00843D?style=flat-square)

</div>

---

## 👋 About

Tinkerologie is home to integrations, plugins and libraries that connect the devices and servers in your
home — so you can monitor and control them locally, from Home Assistant, Apple Home or your Unraid server.

- 🏠 **Local first** — talk to devices over your own network wherever the hardware allows.
- 🧩 **Built to fit together** — each integration sits on a typed, async client library you can reuse.
- 🧪 **Tested and maintained** — CI, coverage and automated dependency updates on every project.

---

## 🏠 Home Assistant integrations

Install through [HACS](https://hacs.xyz/). Integrations marked ![HACS](https://img.shields.io/badge/HACS-default-41BDF5?style=flat-square) are in the default store; add the others as a custom repository.

| Integration | What it does | |
| --- | --- | --- |
| [**ha-unraid**](https://github.com/tinkerologie/ha-unraid) | Monitor and control Unraid — system metrics, Docker, VMs, UPS and alerts ![HACS](https://img.shields.io/badge/HACS-default-41BDF5?style=flat-square) | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-unraid?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-unraid/stargazers) |
| [**ha-unraid-management-agent**](https://github.com/tinkerologie/ha-unraid-management-agent) | Home Assistant integration for the Unraid Management Agent ![HACS](https://img.shields.io/badge/HACS-default-41BDF5?style=flat-square) | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-unraid-management-agent?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-unraid-management-agent/stargazers) |
| [**ha-vault**](https://github.com/tinkerologie/ha-vault) | Monitor jobs and trigger backups from the Vault Unraid plugin | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-vault?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-vault/stargazers) |
| [**ha-unifi-insights**](https://github.com/tinkerologie/ha-unifi-insights) | UniFi Network and Protect monitoring and control via the official UniFi APIs ![HACS](https://img.shields.io/badge/HACS-default-41BDF5?style=flat-square) | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-unifi-insights?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-unifi-insights/stargazers) |
| [**ha-philips-airpurifier**](https://github.com/tinkerologie/ha-philips-airpurifier) | Local control of Philips air purifiers | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-philips-airpurifier?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-philips-airpurifier/stargazers) |
| [**ha-actronair-neo**](https://github.com/tinkerologie/ha-actronair-neo) | ActronAir Neo air conditioning climate control | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-actronair-neo?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-actronair-neo/stargazers) |
| [**ha-wattpilot**](https://github.com/tinkerologie/ha-wattpilot) | Control Fronius Wattpilot EV chargers | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-wattpilot?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-wattpilot/stargazers) |
| [**ha-globird**](https://github.com/tinkerologie/ha-globird) | GloBird energy integration | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-globird?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-globird/stargazers) |
| [**ha-translink**](https://github.com/tinkerologie/ha-translink) | Translink Queensland public transport | [![Stars](https://img.shields.io/github/stars/tinkerologie/ha-translink?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/ha-translink/stargazers) |

---

## 🍎 Homebridge plugins

Bring your devices into Apple Home. Install from the Homebridge UI or `npm`.

| Plugin | What it does | |
| --- | --- | --- |
| [**homebridge-actronair-neo**](https://github.com/tinkerologie/homebridge-actronair-neo) | ActronAir Neo air conditioning in HomeKit | [![npm](https://img.shields.io/npm/v/homebridge-actronair-neo?style=flat-square&logo=npm&label=)](https://www.npmjs.com/package/homebridge-actronair-neo) |
| [**homebridge-philips-airctrl**](https://github.com/tinkerologie/homebridge-philips-airctrl) | Philips air purifiers in HomeKit | [![npm](https://img.shields.io/npm/v/homebridge-philips-airctrl?style=flat-square&logo=npm&label=)](https://www.npmjs.com/package/homebridge-philips-airctrl) |
| [**homebridge-unifi-protect-api**](https://github.com/tinkerologie/homebridge-unifi-protect-api) | UniFi Protect via the official API | [![npm](https://img.shields.io/npm/v/homebridge-unifi-protect-api?style=flat-square&logo=npm&label=)](https://www.npmjs.com/package/homebridge-unifi-protect-api) |
| [**homebridge-ventair-ceiling-fan**](https://github.com/tinkerologie/homebridge-ventair-ceiling-fan) | Ventair Skyfan DC ceiling fans over your local network | [![npm](https://img.shields.io/npm/v/homebridge-ventair-ceiling-fan?style=flat-square&logo=npm&label=)](https://www.npmjs.com/package/homebridge-ventair-ceiling-fan) |

---

## 🖥️ Unraid plugins

Install from **Community Applications** using the [unraid-apps](https://github.com/tinkerologie/unraid-apps) repository.

| Plugin | What it does | |
| --- | --- | --- |
| [**unraid-management-agent**](https://github.com/tinkerologie/unraid-management-agent) | Monitor and control Unraid over REST, WebSocket, MCP, Prometheus and MQTT | [![Stars](https://img.shields.io/github/stars/tinkerologie/unraid-management-agent?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/unraid-management-agent/stargazers) |
| [**vault**](https://github.com/tinkerologie/vault) | Back up and restore containers, VMs, ZFS datasets, folders and plugins to disk, SFTP, SMB, NFS, WebDAV or S3 | [![Stars](https://img.shields.io/github/stars/tinkerologie/vault?style=flat-square&label=%E2%98%85)](https://github.com/tinkerologie/vault/stargazers) |
| [**unraid-apps**](https://github.com/tinkerologie/unraid-apps) | Community Applications templates for the plugins above | |

---

## 📚 Libraries

The building blocks behind the integrations — usable on their own.

| Library | What it does | |
| --- | --- | --- |
| [**unraid-api**](https://github.com/tinkerologie/unraid-api) | Async Python client for the Unraid GraphQL API | [![PyPI](https://img.shields.io/pypi/v/unraid-api?style=flat-square&logo=pypi&logoColor=white&label=)](https://pypi.org/project/unraid-api/) |
| [**unifi-official-api**](https://github.com/tinkerologie/unifi-official-api) | Async Python client for the UniFi Network and Protect APIs | [![PyPI](https://img.shields.io/pypi/v/unifi-official-api?style=flat-square&logo=pypi&logoColor=white&label=)](https://pypi.org/project/unifi-official-api/) |
| [**wattpilot-api**](https://github.com/tinkerologie/wattpilot-api) | Async Python client for Fronius Wattpilot wallboxes | [![PyPI](https://img.shields.io/pypi/v/wattpilot-api?style=flat-square&logo=pypi&logoColor=white&label=)](https://pypi.org/project/wattpilot-api/) |
| [**philips-airctrl**](https://github.com/tinkerologie/philips-airctrl) | Async Python library and CLI for Philips air purifiers over encrypted CoAP | [![PyPI](https://img.shields.io/pypi/v/philips-airctrl?style=flat-square&logo=pypi&logoColor=white&label=)](https://pypi.org/project/philips-airctrl/) |

---

## 🧩 How it fits together

```mermaid
flowchart LR
    subgraph Unraid["🖥️ Unraid server"]
        UMA["unraid-management-agent"]
        VAULT["vault"]
        GQL["Unraid GraphQL API"]
    end
    subgraph Libraries["📚 Libraries"]
        UAPI["unraid-api"]
        WATT["wattpilot-api"]
        PHIL["philips-airctrl"]
    end
    subgraph HA["🏠 Home Assistant"]
        HAU["ha-unraid"]
        HAUMA["ha-unraid-management-agent"]
        HAV["ha-vault"]
        HAUI["ha-unifi-insights"]
        HAW["ha-wattpilot"]
        HAP["ha-philips-airpurifier"]
    end
    GQL --> UAPI --> HAU
    UMA --> HAUMA
    VAULT --> HAV
    WATT --> HAW
    PHIL --> HAP
```

---

## 🧰 Also here

- [**recyclarr-config**](https://github.com/tinkerologie/recyclarr-config) — Recyclarr configuration built on the TRaSH Guides.

---

<div align="center">

### 💬 Get involved

Found a bug or have an idea? Open an issue on the relevant repository.
Pull requests are welcome — check the repository's `CONTRIBUTING.md` to get started.

If these projects save you time, consider [**sponsoring**](https://github.com/sponsors/ruaan-deysel) ❤️

<sub>Tinkerologie is an independent project. Not affiliated with Home Assistant, Homebridge, Unraid, Ubiquiti, Philips, ActronAir, Fronius, Ventair, GloBird or Translink.</sub>

</div>
