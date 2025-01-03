#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RESET='\033[0m'

cleanup() {
    pkill -f "python3 web_app.py"
    killall cloudflared
    pkill -f "tunnelmole tunnel"
}

trap cleanup SIGINT

banner1() {
    echo -e "${GREEN}========================================="
    echo -e "${YELLOW}         Welcome to the Tunnel App       "
    echo -e "${GREEN}=========================================${RESET}"
}

check_dependencies() {
    if ! command -v cloudflared &> /dev/null; then
        echo -e "${YELLOW}Cloudflared is not installed. Installing...${RESET}"
        if [ -d "/data/data/com.termux" ]; then
            wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O $PREFIX/bin/cloudflared
        else
            wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /usr/local/bin/cloudflared
        fi
        chmod +x ${PREFIX:-/usr/local/bin}/cloudflared
        echo -e "${GREEN}Cloudflared installed successfully.${RESET}"
    fi

    if ! command -v tunnelmole &> /dev/null; then
        echo -e "${YELLOW}Tunnelmole is not installed. Installing...${RESET}"
        curl -O https://install.tunnelmole.com/t357g/install && sudo bash install
        echo -e "${GREEN}Tunnelmole installed successfully.${RESET}"
    fi

    if ! command -v jq &> /dev/null; then
        echo -e "${YELLOW}jq is not installed. Installing...${RESET}"
        if [ -d "/data/data/com.termux" ]; then
            pkg update -y && pkg install -y jq
        else
            sudo apt-get update -y && sudo apt-get install -y jq
        fi
        echo -e "${GREEN}jq installed successfully.${RESET}"
    fi
}

clear
banner1
check_dependencies

echo -e "\n${YELLOW}    Select the method!"
echo -e "-------------------  "
echo -e "1-${GREEN} localhost${YELLOW}       |"
echo -e "-------------------"
echo -e "2-${GREEN} cloudflared${YELLOW}     |"
echo -e "-------------------"
echo -e "3-${GREEN} tunnelmole${YELLOW}      |"
echo -e "-------------------"

read -p "Choose: " choose

clear
banner1

case $choose in
    1)
        python3 web_app.py &
        sleep 2
        clear
        banner1
        echo -e "${GREEN}-URL:\nhttp://127.0.0.1:8080${RESET}"
        ;;

    2)
        python3 web_app.py &
        sleep 2
        clear
        banner1
        cloudflared tunnel --no-autoupdate --metrics localhost:55555 --url http://localhost:8080 2>/dev/null &
        echo -e "${YELLOW}Cloudflared starting...."
        sleep 4
        result=$(curl -s http://localhost:55555/quicktunnel)
        if [[ -n "$result" ]]; then
            url=$(echo "$result" | jq -r '.hostname')
            echo -e "${YELLOW} \nURLs: "
            echo -e "------------------------------------------------"
            echo -e "${GREEN}https://${url}${YELLOW}"
            echo -e "------------------------------------------------"
        else
            echo -e "${RED}Error: Empty response or invalid JSON format${RESET}"
            cleanup
        fi
        ;;

    3)
        python3 web_app.py &
        sleep 2
        clear
        banner1
        tunnelmole tunnel --url http://localhost:8080 &
        echo -e "${YELLOW}Tunnelmole starting...."
        sleep 4
        echo -e "${GREEN}Tunnelmole is active. Check your Tunnelmole dashboard for the URL.${RESET}"
        ;;

    *)
        echo -e "${RED}Please enter a valid number!${RESET}"
        ;;
esac

while true; do
    sleep 1
done
