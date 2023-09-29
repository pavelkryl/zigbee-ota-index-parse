# zigbee-ota-index-parse

Simple and straightforward tool to extract all firmware files from https://github.com/Koenkk/zigbee-OTA/ repository.

Parses `index.json` from the given **source directory** (where you have checked out the sources from zigbee-OTA) and copies all the declared firmware files into given **target directory** - usually declared as `zha.zigpy_config.ota.otau_directory` in your Home Assistant config.
