#!/usr/bin/env bash
# ==============================================================================
# ArcReel - Script de démarrage du Studio Vidéo 100% Local
# Lance et vérifie tous les moteurs d'IA locaux pour ArcReel
# ==============================================================================

set -e

BOLD="\033[1m"
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
CYAN="\033[0;36m"
RED="\033[0;31m"
RESET="\033[0m"

echo -e "${BOLD}${CYAN}======================================================${RESET}"
echo -e "${BOLD}${CYAN}   🚀 Démarrage du Studio ArcReel 100% Local          ${RESET}"
echo -e "${BOLD}${CYAN}======================================================${RESET}\n"

# 1. Vérification de Docker
echo -e "${BOLD}[1/4] Vérification de Docker...${RESET}"
if ! docker info >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker n'est pas démarré. Veuillez lancer Docker Desktop puis relancer ce script.${RESET}"
    exit 1
fi
echo -e "${GREEN}✓ Docker est opérationnel.${RESET}\n"

# 2. Démarrage et vérification d'Ollama
echo -e "${BOLD}[2/4] Vérification d'Ollama (Scénarios & Dialogues)...${RESET}"
if curl -s http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Ollama est déjà actif sur le port 11434.${RESET}"
else
    echo -e "${YELLOW}Démarrage d'Ollama avec écoute sur 0.0.0.0:11434...${RESET}"
    export OLLAMA_HOST="0.0.0.0:11434"
    nohup ollama serve >/dev/null 2>&1 &
    sleep 3
    if curl -s http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Ollama a démarré avec succès.${RESET}"
    else
        echo -e "${YELLOW}⚠️ Impossible de démarrer Ollama automatiquement. Lancez 'OLLAMA_HOST=0.0.0.0:11434 ollama serve' manuellement.${RESET}"
    fi
fi
echo ""

# 3. Démarrage de Kokoro-TTS
echo -e "${BOLD}[3/4] Vérification de Kokoro-TTS (Voix off française)...${RESET}"
if docker ps --format '{{.Names}}' | grep -q '^kokoro-tts$'; then
    echo -e "${GREEN}✓ Le conteneur Kokoro-TTS est déjà en cours d'exécution sur le port 8880.${RESET}"
else
    if docker ps -a --format '{{.Names}}' | grep -q '^kokoro-tts$'; then
        echo -e "${YELLOW}Démarrage du conteneur kokoro-tts existant...${RESET}"
        docker start kokoro-tts >/dev/null
    else
        echo -e "${YELLOW}Création et lancement du conteneur kokoro-tts...${RESET}"
        docker run -d --name kokoro-tts -p 8880:8880 --restart unless-stopped ghcr.io/remsky/kokoro-fastapi-cpu:latest >/dev/null
    fi
    echo -e "${CYAN}Attente de l'initialisation du modèle Kokoro en mémoire (environ 5 secondes)...${RESET}"
    sleep 5
    echo -e "${GREEN}✓ Kokoro-TTS est prêt sur le port 8880.${RESET}"
fi
echo ""

# 4. Vérification de ComfyUI
echo -e "${BOLD}[4/4] Vérification de ComfyUI (Images & Vidéos)...${RESET}"
if curl -s http://127.0.0.1:8188/system_stats >/dev/null 2>&1; then
    echo -e "${GREEN}✓ ComfyUI est déjà actif sur le port 8188.${RESET}"
else
    if [ -d "/Applications/Comfy Desktop.app" ]; then
        echo -e "${YELLOW}Lancement de Comfy Desktop...${RESET}"
        open "/Applications/Comfy Desktop.app"
        echo -e "${GREEN}✓ Comfy Desktop lancé.${RESET}"
    else
        echo -e "${YELLOW}⚠️ Comfy Desktop non trouvé dans /Applications. Assurez-vous qu'il est lancé sur le port 8188.${RESET}"
    fi
fi
echo ""

# 5. Démarrage d'ArcReel
echo -e "${BOLD}[ArcReel] Vérification du serveur ArcReel...${RESET}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ -d "$PROJECT_ROOT/deploy/production" ]; then
    cd "$PROJECT_ROOT/deploy/production"
    if ! docker compose ps --services --filter "status=running" | grep -q "arcreel"; then
        echo -e "${YELLOW}Démarrage des conteneurs ArcReel...${RESET}"
        docker compose up -d
    else
        echo -e "${GREEN}✓ ArcReel est déjà actif.${RESET}"
    fi
fi

echo -e "\n${BOLD}${GREEN}======================================================${RESET}"
echo -e "${BOLD}${GREEN}   🎉 Tous vos services locaux sont opérationnels !   ${RESET}"
echo -e "${BOLD}${GREEN}======================================================${RESET}"
echo -e "  🌐 ${BOLD}Interface ArcReel :${RESET}   http://localhost:1241"
echo -e "  ✍️  ${BOLD}Ollama (LLM) :${RESET}       http://host.docker.internal:11434/v1"
echo -e "  🎨 ${BOLD}ComfyUI (Images) :${RESET}   http://host.docker.internal:8188"
echo -e "  🎙️  ${BOLD}Kokoro (Voix off) :${RESET}  http://host.docker.internal:8880/v1"
echo -e "  🎬 ${BOLD}ComfyUI (Vidéos) :${RESET}   http://host.docker.internal:8188"
echo -e "${CYAN}------------------------------------------------------${RESET}\n"
