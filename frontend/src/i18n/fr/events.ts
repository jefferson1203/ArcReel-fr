import type enEvents from '../en/events';

export default {
  "label.grid": 'Storyboard multi-grille « {{id}} »',
  "label.grid_split": 'Division du storyboard multi-grille « {{id}} »',
  "label.voice_sample": 'Aperçu vocal pour « {{id}} »',
  "label.asset_image_character": 'Image de ressource pour le personnage « {{id}} »',
  "label.asset_image_scene": 'Image de ressource pour le décor « {{id}} »',
  "label.asset_image_prop": 'Image de ressource pour l\'accessoire « {{id}} »',
  "label.asset_image_product": 'Image de ressource pour le produit « {{id}} »',
  "label.asset_image_character_derivative": 'Image de ressource pour la variante de personnage « {{id}} »',
  "label.skeleton_segments": 'Segment « {{id}} »',
  "label.skeleton_scenes": 'Scène « {{id}} »',
  "label.skeleton_shots": 'Plan « {{id}} »',
  "label.skeleton_video_units": 'Unité vidéo « {{id}} »',
  "label.narration_audio": 'Audio de narration « {{id}} »',
  "label.named_entity_character": 'Personnage « {{id}} »',
  "label.named_entity_scene": 'Scène « {{id}} »',
  "label.named_entity_prop": 'Accessoire « {{id}} »',
  "label.named_entity_product": 'Produit « {{id}} »',
  "label.named_entity_character_derivative": 'Variante de personnage « {{id}} »',
  "label.character_reference_audio": 'Audio de référence pour le personnage « {{id}} »',
  "label.project_settings": "Paramètres du projet",
  "label.overview": "Vue d'ensemble du projet",
  "label.episode": "{{episode_name}}",
  "label.draft_normalized_script": "Scénario normalisé pour {{episode_name}}",
  "label.draft_segment_splitting": "Découpage en segments pour {{episode_name}}",
  "label.draft_script_plan": "Brouillon de plan de script pour {{episode_name}}",
  "label.draft_prompt_authoring": "Brouillon de rédaction de prompts pour {{episode_name}}",

  "entity.project": "projets",
  "entity.character": "personnages",
  "entity.scene": "décors",
  "entity.prop": "accessoires",
  "entity.product": "produits",
  "entity.segment": "segments",
  "entity.drama_scene": "scènes",
  "entity.shot": "plans",
  "entity.reference_unit": "unités vidéo",
  "entity.episode": "épisodes",
  "entity.overview": "vues d'ensemble du projet",
  "entity.draft": "résultats du plan de script",
  "entity.grid": "storyboards multi-grilles",
  "entity.task": "tâches",
  "entity.fallback": "éléments",

  "noun.storyboard_image": "images de storyboard",
  "noun.video": "vidéos",
  "noun.grid": "storyboards multi-grilles",
  "noun.narration_audio": "audio de narration",
  "noun.voice_sample": "aperçus vocaux",

  "single.storyboard_ready": "L'image de storyboard pour {{label}} est prête",
  "single.video_ready": "La vidéo pour {{label}} est prête",
  "single.generated": "{{label}} est prêt",
  "single.completed": "{{label}} est terminé",
  "single.created": "{{label}} créé",
  "single.deleted": "{{label}} supprimé",
  "single.updated": "{{label}} mis à jour",

  "deferred.storyboard_ready":
    "L'IA vient de générer l'image de storyboard pour {{label}}. Cliquez pour afficher",
  "deferred.video_ready":
    "L'IA vient de générer la vidéo pour {{label}}. Cliquez pour afficher",
  "deferred.generated": "{{label}} est prêt",
  "deferred.completed": "{{label}} est terminé",
  "deferred.created": "L'IA vient d'ajouter {{label}}. Cliquez pour afficher",
  "deferred.deleted": "L'IA vient de supprimer {{label}}. Cliquez pour afficher",
  "deferred.updated": "L'IA vient de mettre à jour {{label}}. Cliquez pour afficher",

  "group.generated": "{{count}} {{entity}} généré(s) : {{summary}}",
  "group.created": "{{count}} {{entity}} ajouté(s) : {{summary}}",
  "group.deleted": "{{count}} {{entity}} supprimé(s) : {{summary}}",
  "group.updated": "{{count}} {{entity}} mis à jour : {{summary}}",

  "group_deferred.generated":
    "L'IA vient de générer {{count}} {{entity}} : {{summary}}. Cliquez pour afficher",
  "group_deferred.created":
    "L'IA vient d'ajouter {{count}} {{entity}} : {{summary}}. Cliquez pour afficher",
  "group_deferred.deleted":
    "L'IA vient de supprimer {{count}} {{entity}} : {{summary}}. Cliquez pour afficher",
  "group_deferred.updated":
    "L'IA vient de mettre à jour {{count}} {{entity}} : {{summary}}. Cliquez pour afficher",

  "list.separator": ", ",
  "list.more_suffix": " et plus",
} satisfies Record<keyof typeof enEvents, string> & Record<string, string>;

