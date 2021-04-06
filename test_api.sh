#! /bin/bash

$ curl --request POST \
       --url http://localhost:1313/predict \
       --header 'content-type: application/json' \
       --data '{"alc": 14.23, "malic": 1.71, "ash": 2.43, "alcash": 15.6, "mag": 127, "tphen": 2.8, "flav": 3.06, "nflav": 0.28, "poran": 2.29, "color": 5.64, "hue": 1.04, "dil": 3.92, "proline": 1065}'