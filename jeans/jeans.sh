#!/bin/bash

for ((i = 730; i <= 730; i++))
do
  url="https://api.tatadigital.com/api/v1/search/composite?limit=21&q=jeans&scope=Fashion&sort=relevance&currentPage=$i"

  response=$(curl  -H 'authority: api.tatadigital.com' \
                   -H 'accept: application/json, text/plain, */*' \
                   -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
                   -H 'accept-version: 4' \
                   -H 'anonymous_id: 298e7a7d-8dfc-436c-95aa-1ad13a2f78fd' \
                   -H 'authorization;' \
                   -H 'client_id: TCP-WEB-APP' \
                   -H 'client_secret: 6fe27bd7-658d-4d28-ab66-a71da9637529' \
                   -H 'ocp-apim-subscription-key: 354d9be9edce479fbd797edc71ebf50b' \
                   -H 'origin: https://www.tatadigital.com' \
                   -H 'referer: https://www.tatadigital.com/' \
                   -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
                   -H 'sec-ch-ua-mobile: ?0' \
                   -H 'sec-ch-ua-platform: "Linux"' \
                   -H 'sec-fetch-dest: empty' \
                   -H 'sec-fetch-mode: cors' \
                   -H 'sec-fetch-site: same-site' \
                   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
                   --compressed $url | jq '.results.products'  >> response.txt)
done
