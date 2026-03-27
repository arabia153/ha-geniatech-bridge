# Geniatech DTV Bridge AAC custom add-on

This Home Assistant add-on repo widens the profile schema so you can select:

- `pass`
- `fhd`
- `hd`
- `sd`
- `fhd_aac`
- `hd_aac`
- `sd_aac`

## Install

1. Unzip this repo somewhere you can edit.
2. Replace `YOUR_GITHUB_USERNAME` in:
   - `repository.yaml`
   - `geniatech_dtv_bridge_aac/config.yaml`
3. Push the repo to your own GitHub account.
4. In Home Assistant add-on store, add your GitHub repo as an add-on repository.
5. Install **Geniatech DTV Bridge AAC**.
6. Set:
   - `ip: 192.168.0.252`
   - `profile: fhd_aac`
7. Save and restart the add-on.

## Notes

- This add-on downloads the upstream bridge source during image build.
- Internet access is required the first time the add-on image is built.
- If `fhd_aac` is heavy or unstable, try `hd_aac`.
