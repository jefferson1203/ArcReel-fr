"""French translations for provider registry metadata."""

MESSAGES: dict[str, str] = {
    # Provider display names
    "provider_name_gemini-aistudio": "AI Studio",
    "provider_name_gemini-vertex": "Vertex AI",
    "provider_name_ark": "Volcengine Ark",
    "provider_name_ark-agent-plan": "Volcengine Ark Agent Plan",
    "provider_name_grok": "Grok",
    "provider_name_openai": "OpenAI",
    "provider_name_vidu": "Vidu",
    "provider_name_dashscope": "Alibaba Model Studio",
    "provider_name_minimax": "MiniMax",
    "provider_name_kling": "Kling",
    "provider_name_agnes": "Agnes",
    # Fournisseurs supprimés
    "deleted_provider_display_name": "Fournisseur supprimé",
    "deleted_agent_provider_display_name": "Fournisseur d'Agent supprimé",
    # Descriptions des fournisseurs
    "provider_desc_gemini-aistudio": "IDE basé sur le web développé par Google pour prototyper des applications avec des modèles d'IA générative.",
    "provider_desc_gemini-vertex": "Service d'apprentissage automatique proposé par Google Cloud, renommé Gemini Enterprise Agent Platform.",
    "provider_desc_ark": "Plateforme de services de grands modèles (MaaS) de Volcengine (ByteDance), offrant affinage, évaluation et inférence de modèles pour les entreprises.",
    "provider_desc_ark-agent-plan": "Forfait de modèles sur abonnement de Volcengine Ark pour les utilisateurs individuels, facturé en crédits.",
    "provider_desc_grok": "L'API Grok de SpaceX Super Intelligence (anciennement xAI), hébergeant la famille de modèles d'IA générative Grok.",
    "provider_desc_openai": "Plateforme d'API d'OpenAI, proposant la série GPT et d'autres modèles génératifs d'IA.",
    "provider_desc_vidu": "Plateforme d'API Vidu de ShengShu Technology dédiée à la génération vidéo par IA.",
    "provider_desc_dashscope": "Plateforme de modèles d'Alibaba Cloud, proposant Qwen et d'autres modèles avec accès API, affinage et déploiement.",
    "provider_desc_minimax": "Plateforme ouverte de MiniMax, société d'IA basée à Shanghai, proposant ses modèles multimodaux et la génération vidéo Hailuo. Se connecte par défaut au site chinois ; configurez base_url sur le site international pour un accès mondial.",
    "provider_desc_kling": "Plateforme ouverte de Kling AI, le service d'IA générative de Kuaishou. L'authentification par clé d'API fonctionne avec tous les modèles ; la paire Access Key + Secret Key (JWT) ne supporte que les versions 3.0 et antérieures.",
    "provider_desc_agnes": "Plateforme IA multimodale d'Agnes AI, proposant ses modèles d'IA générative via une API unifiée.",
    # Notes de préréglages d'agent
    "preset_notes_deepseek": "Point de terminaison officiel compatible Anthropic de DeepSeek ; requiert une clé débutant par sk-.",
    "preset_notes_xiaomi_mimo": "Xiaomi MiMo n'accepte que des noms de modèles connus ; aucune liste publique de modèles.",
    "preset_notes_ark_coding_plan": "Volcengine Ark Coding Plan ; pas de liste de modèles via API — sélectionnez un modèle suggéré activé dans la console Ark.",
    "preset_notes_ark_agent_plan": "Volcengine Ark Agent Plan ; pas de liste de modèles via API — sélectionnez un modèle suggéré inclus dans votre formule.",
}

