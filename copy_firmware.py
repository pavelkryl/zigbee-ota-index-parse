#!/usr/bin/python

import json
import sys
import shutil
from typing import Optional
from pydantic import BaseModel, BaseConfig

class PydanticConfig(BaseConfig):
    # pydantic configuration to allow extra elements
    allow_extra = True


class FirmwareEntry(BaseModel):
    """a single entry in index.json"""
    url: str
    path: Optional[str] = None

    class Config(PydanticConfig):
        pass


def parse_index_copy_firmware_files(zigbee_ota_dir: str, destination_dir: str):
    """"
    parses index.json in the given [zigbee_ota_dir], each entry which has 'path' field,
    determines firmware file to be copied into [destination_dir].

    this actualy flattens the nested hierarchy of firmware files so that they are
    easily observable with zigpy
    """
    with open(f"{zigbee_ota_dir}/index.json", 'r') as file:
        json_data = json.load(file)
        firmware_entries = [FirmwareEntry(**item) for item in json_data]
        for entry in [e for e in firmware_entries if e.path is not None ]:
            print(f"copying {zigbee_ota_dir}/{entry.path}")
            shutil.copy(f"{zigbee_ota_dir}/{entry.path}", destination_dir)
        print("done")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""expecting two arguments:
              [1] - source directory where contents of zigbee-OTA is checked out
              [2] - destination directory where to put the firmware files
              """)
        sys.exit(2)
    else:
        parse_index_copy_firmware_files(sys.argv[1], sys.argv[2])
