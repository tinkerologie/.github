<div align="center">

<img src="https://avatars.githubusercontent.com/u/340790272?v=4" width="120" alt="Tinkerologie logo" />

# Tinkerologie

**Open-source tinkering for the smart home and the home lab.**

Integrations, plugins and libraries that connect the devices and servers in your home,
so you can monitor and control them locally.

[![🏠 Home Assistant integrations](https://img.shields.io/badge/%F0%9F%8F%A0%20Home%20Assistant-integrations-41BDF5?style=for-the-badge)](#-home-assistant-integrations)
[![🍎 Homebridge plugins](https://img.shields.io/badge/%F0%9F%8D%8E%20Homebridge-plugins-491F59?style=for-the-badge)](#-homebridge-plugins)
[![🖥️ Unraid plugins](https://img.shields.io/badge/%F0%9F%96%A5%EF%B8%8F%20Unraid-plugins-F15A2C?style=for-the-badge)](#%EF%B8%8F-unraid-plugins)
[![📚 Python and Go libraries](https://img.shields.io/badge/%F0%9F%93%9A%20Libraries-Python%20%26%20Go-3776AB?style=for-the-badge)](#-libraries)

[![Total stars across Tinkerologie repositories](https://img.shields.io/github/stars/tinkerologie?style=flat-square&label=stars&color=F5C518)](https://github.com/orgs/tinkerologie/repositories?sort=stargazers)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/ruaan-deysel?style=flat-square&logo=githubsponsors&label=sponsors&color=EA4AAA)](https://github.com/sponsors/ruaan-deysel)
![Made in Australia](https://img.shields.io/badge/made%20in-Australia-00843D?style=flat-square)

</div>

---

## 👋 About

- 🏠 **Local first.** Talk to devices over your own network wherever the hardware allows.
- 🧩 **Built to fit together.** Integrations sit on typed, async client libraries you can reuse on their own.
- 🧪 **Tested and maintained.** CI and automated dependency updates on every project, with coverage
  tracked on the core libraries and integrations.

---

## 🏠 Home Assistant integrations

Install through [HACS](https://hacs.xyz/). Integrations marked **HACS default** are in the default store;
add the others as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories/).
Install counts come from [Home Assistant analytics](https://analytics.home-assistant.io/custom_integrations) (opt-in, so a lower bound).

| Integration | What it does | |
| --- | --- | --- |
| [**ha-unraid**](https://github.com/tinkerologie/ha-unraid)<br><sub>HACS default</sub> | Monitor and control Unraid: system metrics, Docker, VMs, UPS and alerts | [![ha-unraid stars](https://img.shields.io/github/stars/tinkerologie/ha-unraid?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-unraid/stargazers) [![ha-unraid active installs](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.unraid.total&label=installs&style=flat-square&color=41BDF5)](https://analytics.home-assistant.io/custom_integrations) |
| [**ha-unraid-management-agent**](https://github.com/tinkerologie/ha-unraid-management-agent)<br><sub>HACS default</sub> | Full Unraid control through the Unraid Management Agent, with real-time WebSocket updates | [![ha-unraid-management-agent stars](https://img.shields.io/github/stars/tinkerologie/ha-unraid-management-agent?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-unraid-management-agent/stargazers) [![ha-unraid-management-agent active installs](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.unraid_management_agent.total&label=installs&style=flat-square&color=41BDF5)](https://analytics.home-assistant.io/custom_integrations) |
| [**ha-unifi-insights**](https://github.com/tinkerologie/ha-unifi-insights)<br><sub>HACS default</sub> | UniFi Network and Protect monitoring and control via the official UniFi APIs | [![ha-unifi-insights stars](https://img.shields.io/github/stars/tinkerologie/ha-unifi-insights?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-unifi-insights/stargazers) [![ha-unifi-insights active installs](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.unifi_insights.total&label=installs&style=flat-square&color=41BDF5)](https://analytics.home-assistant.io/custom_integrations) |
| [**ha-philips-airpurifier**](https://github.com/tinkerologie/ha-philips-airpurifier) | Local control of Philips air purifiers over encrypted CoAP | [![ha-philips-airpurifier stars](https://img.shields.io/github/stars/tinkerologie/ha-philips-airpurifier?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-philips-airpurifier/stargazers) |
| [**ha-actronair-neo**](https://github.com/tinkerologie/ha-actronair-neo) | ActronAir Neo air conditioning: zones, modes and setpoints | [![ha-actronair-neo stars](https://img.shields.io/github/stars/tinkerologie/ha-actronair-neo?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-actronair-neo/stargazers) [![ha-actronair-neo active installs](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.actronair_neo.total&label=installs&style=flat-square&color=41BDF5)](https://analytics.home-assistant.io/custom_integrations) |
| [**ha-wattpilot**](https://github.com/tinkerologie/ha-wattpilot) | Monitor and control Fronius Wattpilot EV chargers | [![ha-wattpilot stars](https://img.shields.io/github/stars/tinkerologie/ha-wattpilot?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-wattpilot/stargazers) |
| [**ha-vault**](https://github.com/tinkerologie/ha-vault) | Monitor jobs and trigger backups from the Vault Unraid plugin | [![ha-vault stars](https://img.shields.io/github/stars/tinkerologie/ha-vault?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-vault/stargazers) |
| [**ha-globird**](https://github.com/tinkerologie/ha-globird) | GloBird Energy electricity and gas accounts: balances, invoices and smart-meter usage | [![ha-globird stars](https://img.shields.io/github/stars/tinkerologie/ha-globird?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-globird/stargazers) |
| [**ha-translink**](https://github.com/tinkerologie/ha-translink) | Translink Queensland real-time departures, journey planning and live vehicle tracking | [![ha-translink stars](https://img.shields.io/github/stars/tinkerologie/ha-translink?style=flat-square&label=stars)](https://github.com/tinkerologie/ha-translink/stargazers) |

---

## 🍎 Homebridge plugins

Bring your devices into the Apple Home app. Install from the Homebridge UI or with `npm`.

| Plugin | What it does | |
| --- | --- | --- |
| [**homebridge-actronair-neo**](https://github.com/tinkerologie/homebridge-actronair-neo) | ActronAir Neo air conditioning in HomeKit | [![homebridge-actronair-neo npm version](https://img.shields.io/npm/v/homebridge-actronair-neo?style=flat-square&label=npm)](https://www.npmjs.com/package/homebridge-actronair-neo) [![homebridge-actronair-neo monthly downloads](https://img.shields.io/npm/dm/homebridge-actronair-neo?style=flat-square&label=downloads)](https://www.npmjs.com/package/homebridge-actronair-neo) |
| [**homebridge-ventair-ceiling-fan**](https://github.com/tinkerologie/homebridge-ventair-ceiling-fan) | Ventair Skyfan DC ceiling fans over your local network | [![homebridge-ventair-ceiling-fan npm version](https://img.shields.io/npm/v/homebridge-ventair-ceiling-fan?style=flat-square&label=npm)](https://www.npmjs.com/package/homebridge-ventair-ceiling-fan) [![homebridge-ventair-ceiling-fan monthly downloads](https://img.shields.io/npm/dm/homebridge-ventair-ceiling-fan?style=flat-square&label=downloads)](https://www.npmjs.com/package/homebridge-ventair-ceiling-fan) |
| [**homebridge-philips-airctrl**](https://github.com/tinkerologie/homebridge-philips-airctrl) | Philips air purifiers in HomeKit | [![homebridge-philips-airctrl npm version](https://img.shields.io/npm/v/homebridge-philips-airctrl?style=flat-square&label=npm)](https://www.npmjs.com/package/homebridge-philips-airctrl) [![homebridge-philips-airctrl monthly downloads](https://img.shields.io/npm/dm/homebridge-philips-airctrl?style=flat-square&label=downloads)](https://www.npmjs.com/package/homebridge-philips-airctrl) |
| [**homebridge-unifi-protect-api**](https://github.com/tinkerologie/homebridge-unifi-protect-api) | UniFi Protect cameras, HomeKit Secure Video and sensors via the official API | [![homebridge-unifi-protect-api npm version](https://img.shields.io/npm/v/homebridge-unifi-protect-api?style=flat-square&label=npm)](https://www.npmjs.com/package/homebridge-unifi-protect-api) [![homebridge-unifi-protect-api monthly downloads](https://img.shields.io/npm/dm/homebridge-unifi-protect-api?style=flat-square&label=downloads)](https://www.npmjs.com/package/homebridge-unifi-protect-api) |

---

## 🖥️ Unraid plugins

Install from **Community Applications** using the [unraid-apps](https://github.com/tinkerologie/unraid-apps) templates.

| Plugin | What it does | |
| --- | --- | --- |
| [**unraid-management-agent**](https://github.com/tinkerologie/unraid-management-agent) | Monitor and control Unraid over REST, WebSocket, MCP, Prometheus and MQTT | [![unraid-management-agent stars](https://img.shields.io/github/stars/tinkerologie/unraid-management-agent?style=flat-square&label=stars)](https://github.com/tinkerologie/unraid-management-agent/stargazers) [![unraid-management-agent latest release](https://img.shields.io/github/v/release/tinkerologie/unraid-management-agent?style=flat-square&label=release)](https://github.com/tinkerologie/unraid-management-agent/releases/latest) |
| [**vault**](https://github.com/tinkerologie/vault) | Back up and restore containers, VMs, ZFS datasets, folders and plugins to disk, SFTP, SMB, NFS, WebDAV or S3 | [![vault stars](https://img.shields.io/github/stars/tinkerologie/vault?style=flat-square&label=stars)](https://github.com/tinkerologie/vault/stargazers) [![vault latest release](https://img.shields.io/github/v/release/tinkerologie/vault?style=flat-square&label=release)](https://github.com/tinkerologie/vault/releases/latest) |

---

## 📚 Libraries

The building blocks behind the integrations, usable on their own.

| Library | What it does | |
| --- | --- | --- |
| [**unraid-api**](https://github.com/tinkerologie/unraid-api) | Async Python client for the Unraid GraphQL API | [![unraid-api PyPI version](https://img.shields.io/pypi/v/unraid-api?style=flat-square&label=pypi)](https://pypi.org/project/unraid-api/) [![unraid-api monthly downloads](https://img.shields.io/pypi/dm/unraid-api?style=flat-square&label=downloads)](https://pypistats.org/packages/unraid-api) |
| [**philips-airctrl**](https://github.com/tinkerologie/philips-airctrl) | Async Python library and CLI for Philips air purifiers over encrypted CoAP | [![philips-airctrl PyPI version](https://img.shields.io/pypi/v/philips-airctrl?style=flat-square&label=pypi)](https://pypi.org/project/philips-airctrl/) [![philips-airctrl monthly downloads](https://img.shields.io/pypi/dm/philips-airctrl?style=flat-square&label=downloads)](https://pypistats.org/packages/philips-airctrl) |
| [**wattpilot-api**](https://github.com/tinkerologie/wattpilot-api) | Async Python client for Fronius Wattpilot wallboxes | [![wattpilot-api PyPI version](https://img.shields.io/pypi/v/wattpilot-api?style=flat-square&label=pypi)](https://pypi.org/project/wattpilot-api/) [![wattpilot-api monthly downloads](https://img.shields.io/pypi/dm/wattpilot-api?style=flat-square&label=downloads)](https://pypistats.org/packages/wattpilot-api) |
| [**unifi-official-api**](https://github.com/tinkerologie/unifi-official-api) | Async Python client for the official UniFi Network and Protect APIs | [![unifi-official-api PyPI version](https://img.shields.io/pypi/v/unifi-official-api?style=flat-square&label=pypi)](https://pypi.org/project/unifi-official-api/) [![unifi-official-api monthly downloads](https://img.shields.io/pypi/dm/unifi-official-api?style=flat-square&label=downloads)](https://pypistats.org/packages/unifi-official-api) |

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
        UNIFI["unifi-official-api"]
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
    UNIFI -. vendored .-> HAUI
    WATT --> HAW
    PHIL --> HAP
```

<sub>The Homebridge plugins talk to their devices directly and don't depend on these libraries.</sub>

---

<details>
<summary><b>🧰 Also here</b></summary>

<br>

- [**recyclarr-config**](https://github.com/tinkerologie/recyclarr-config): Recyclarr configuration built on the TRaSH Guides.
- [**coderabbit**](https://github.com/tinkerologie/coderabbit): shared CodeRabbit review configuration for every repository.

</details>

---

<div align="center">

### 💬 Get involved

Found a bug or have an idea? Open an issue on the relevant repository using its bug or enhancement template.<br>
Pull requests are welcome. Read the [contribution governance](https://github.com/tinkerologie/.github/blob/main/GOVERNANCE.md)
and the repository's `CONTRIBUTING.md` first.

If these projects save you time, consider [**sponsoring**](https://github.com/sponsors/ruaan-deysel) ❤️

<sub>Tinkerologie is an independent project, not affiliated with or endorsed by Home Assistant, the Open Home Foundation,
Homebridge, Apple, Lime Technology (Unraid), Ubiquiti, Philips, ActronAir, Fronius, Ventair, GloBird or Translink.
Apple, Apple Home and HomeKit are trademarks of Apple Inc. All other trademarks belong to their respective owners.</sub>

</div>
