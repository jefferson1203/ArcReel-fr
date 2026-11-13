"""Validation and archive diagnostic messages (French)."""

MESSAGES = {
    # ---- passthrough ----
    "val_literal": "{text}",
    # ---- generic field shape ----
    "val_missing_field": "Champ obligatoire manquant : {field}",
    "val_missing_field_at": "{prefix} : champ obligatoire manquant {field}",
    "val_field_type_string": "Erreur de type de champ : {field} doit être une chaîne de caractères",
    "val_field_type_bool": "Erreur de type de champ : {field} doit être un booléen",
    "val_field_type_integer": "Erreur de type de champ : {field} doit être un entier",
    "val_field_type_number": "Erreur de type de champ : {field} doit être un nombre",
    "val_field_out_of_range": "La valeur {value} du champ {field} est hors limites ; elle doit être comprise entre {min} et {max}",
    "val_field_must_be_string": "{field} doit être une chaîne de caractères",
    "val_field_must_be_string_typed": "{field} doit être une chaîne de caractères, obtenu {actual}",
    "val_field_must_be_array": "{field} doit être un tableau",
    "val_field_must_be_nonempty_array": "{field} doit être un tableau non vide",
    "val_field_must_be_nonempty_string": "{field} doit être une chaîne non vide",
    "val_field_must_be_object": "{field} doit être un objet",
    "val_field_invalid": "{field} est invalide : {detail}",
    "val_ledger_source_file_not_relative": "source_file doit être un chemin POSIX relatif au projet",
    "val_ledger_source_file_escapes": "source_file ne doit pas être un chemin absolu ni contenir ..",
    "val_ledger_start_after_end": "start ne peut pas être supérieur à end",
    "val_field_bad_timestamp": "{field} n'est pas un horodatage ISO8601 valide : {value}",
    "val_item_must_be_object": "{prefix} : doit être un objet",
    "val_item_format_object": "{prefix} : format de données incorrect, objet attendu",
    # ---- path references ----
    "val_path_empty": "{field} : le chemin ne peut pas être vide",
    "val_path_traversal": "{field} : le chemin de référence sort du projet : {path}",
    "val_path_outside_dir": "{field} : le chemin de référence doit se trouver sous {dir}/ : {path}",
    "val_path_missing": "{field} : le fichier référencé n'existe pas : {path}",
    "val_path_must_be_relative": "{field} doit être un chemin relatif au projet : {path}",
    # ---- project-level fields ----
    "val_content_mode_invalid": "content_mode invalide : '{value}', doit être l'un de {allowed}",
    "val_source_kind_invalid": "{prefix} : source_kind invalide '{value}', doit être l'un de {allowed}",
    "val_generation_mode_invalid": "generation_mode invalide : '{value}', doit être l'un de {allowed}",
    "val_deprecated_clues": (
        "project.json contient le champ obsolète clues ; attendez la migration automatique ou redémarrez le service"
    ),
    "val_deprecated_field_removable": "Le champ {field} est obsolète (calculé à la lecture) et peut être supprimé en toute sécurité",
    "val_cannot_load_project_json": "Impossible de charger project.json : {path}",
    "val_cannot_load_script": "Impossible de charger le fichier de scénario : {path}",
    "val_unrecognized_entry": "Fichier ou répertoire supplémentaire non reconnu détecté : {name}",
    "val_novel_must_be_object": "Le champ novel doit être un objet",
    # ---- episode entries and ledger ----
    "val_ledger_status_type": "{prefix} : ledger_status doit être une chaîne, obtenu : {value}",
    "val_source_origin_invalid": "{prefix} : source_origin invalide '{value}', doit être l'un de {allowed}",
    "val_source_range_requires_whole_source": "{prefix} : seul un épisode extrait de la source complète (source_origin whole_source) peut avoir source_range",
    "val_whole_source_file_invalid": "whole_source_files[{index}] doit être un objet avec source_file pointant vers un fichier .txt ou .md directement sous source/",
    "val_episode_missing_num_at": "{prefix} : champ obligatoire manquant episode (entier)",
    "val_episode_missing_title_at": "{prefix} : champ obligatoire manquant title (chaîne, peut être vide)",
    "val_episode_missing_num": "Champ obligatoire manquant : episode (entier)",
    # ---- ad / short-film projects ----
    "val_ad_only_field": "{field} est uniquement disponible pour les projets de publicité/court-métrage (content_mode=ad)",
    "val_ad_missing_target_duration": (
        "Champ obligatoire manquant : target_duration (durée totale cible en secondes pour les projets publicitaires)"
    ),
    "val_ad_target_duration_invalid": "target_duration invalide : {value}, doit être un nombre entier positif de secondes",
    "val_ad_no_default_duration": (
        "Les projets de publicité/court métrage ne possèdent pas de default_duration "
        "(la durée des plans est calculée par plan en fonction de target_duration)"
    ),
    "val_ad_no_episode_target_duration": (
        "Les projets de publicité/court métrage ne possèdent pas de episode_target_duration "
        "(la durée globale est calculée selon target_duration)"
    ),
    "val_ad_no_grid_storyboard": "Les projets de publicité/court métrage ne supportent pas les storyboards multi-grilles (grid_storyboard)",
    "val_ad_episodes_single": "Les projets de publicité/court métrage doivent toujours contenir exactement un épisode (épisode 1)",
    "val_ad_shots_missing": "Le scénario publicitaire ne contient pas le tableau de plans shots",
    "val_ad_duration_drift": (
        "La durée totale du scénario {total}s s'écarte de target_duration {target}s de {delta:.0%}, "
        "dépassant le seuil d'observation de {threshold:.0%} (informatif uniquement, l'enregistrement n'est pas bloqué)"
    ),
    # ---- asset catalogs ----
    "val_asset_format_object": "{asset_type} '{name}' a un format incorrect, un objet était attendu",
    "val_asset_field_must_be_object": "{asset_type} '{name}'.{field} doit être un objet",
    "val_asset_field_must_be_string": "{asset_type} '{name}'.{field} doit être une chaîne, obtenu {actual}",
    "val_asset_field_bad_timestamp": "{asset_type} '{name}'.{field} n'est pas un horodatage ISO8601 valide : {value}",
    "val_asset_field_must_be_string_list": "{asset_type} '{name}'.{field} doit être une liste de chaînes, obtenu {actual}",
    "val_asset_field_item_must_be_string": "{asset_type} '{name}'.{field}[{index}] doit être une chaîne, obtenu {actual}",
    "val_asset_name_duplicate": (
        "Nom de ressource de projet en double : {duplicate_type} '{duplicate_name}' entre en conflit avec "
        "{first_type} '{first_name}' après normalisation Unicode NFC"
    ),
    # ---- item-level references ----
    "val_refs_unregistered": "{prefix} : {field} référence des entrées {asset_type} absentes de project.json : {names}",
    "val_missing_defaults_empty_array": "{prefix} : {field} est manquant, valeur par défaut tableau vide",
    # ---- generic item checks ----
    "val_id_format": "{prefix} : format de {field} invalide '{value}', attendu E{{n}}S{{nn}}",
    "val_missing_duration_default": "{prefix} : duration_seconds est manquant, valeur par défaut {default}",
    "val_duration_invalid": "{prefix} : duration_seconds invalide '{value}', doit être un entier positif",
    # ---- drama utterances ----
    "val_utterance_must_be_object": "{prefix} doit être un objet",
    "val_utterance_kind_invalid": "Le genre de {prefix} doit être dialogue ou voiceover",
    "val_utterance_text_invalid": "Le texte de {prefix} doit être une chaîne non vide",
    "val_utterance_speaker_type": "Le locuteur de {prefix} doit être une chaîne ou null",
    "val_utterance_dialogue_speaker": "Un dialogue de {prefix} doit obligatoirement avoir un locuteur non vide",
    "val_utterance_voiceover_speaker": "Une voix off de {prefix} ne doit pas comporter de locuteur",
    "val_scene_speech_overflow": (
        "{prefix} : le dialogue estimé dure {spoken:.1f}s, dépassant la durée de scène de {duration}s de plus de "
        "{tolerance:.0%} (plafond de tolérance {budget:.1f}s) ; un dialogue trop long risque d'être précipité "
        "(informatif uniquement, l'enregistrement n'est pas bloqué)"
    ),
    # ---- ad shots ----
    "val_shot_duration_missing_zero": "{prefix} : duration_seconds est manquant, comptabilisé 0 dans le total",
    "val_shot_duration_out_of_range": (
        "{prefix} : duration_seconds invalide '{value}', le mode reference_video requiert un entier "
        "compris entre {low} et {high}"
    ),
    "val_shot_missing_voiceover_text": (
        "{prefix} : champ obligatoire manquant voiceover_text (texte de voix off, peut être une chaîne vide)"
    ),
    # ---- reference-video units ----
    "val_unit_id_missing": "{prefix} : unit_id est manquant",
    "val_unit_id_missing_required": "{prefix} : champ obligatoire manquant unit_id",
    "val_unit_id_duplicate": "{prefix} : unit_id en double '{value}'",
    "val_video_units_missing": "Le scénario reference_video ne contient pas le tableau video_units",
    "val_unit_duration_range": "{prefix} : duration_seconds doit être un entier compris entre {low} et {high}",
    # ---- skeleton / route mismatch ----
    "val_skeleton_noun_segments": "segments",
    "val_skeleton_noun_scenes": "scènes",
    "val_skeleton_noun_shots": "plans",
    "val_skeleton_noun_video_units": "unités vidéo",
    "val_route_reference_video": "vidéo de référence (reference_video)",
    "val_route_storyboard": "storyboard vers vidéo (storyboard)",
    "val_skeleton_mismatch_reference_known": (
        "La structure du scénario ne correspond pas au mode de génération : le mode actuel est {route}, "
        "qui requiert la structure {expected} ({expected_noun}), mais ce scénario utilise {actual} ({actual_noun}). "
        "Appelez generate_script_plan pour découper à nouveau cet épisode, puis régénérez le scénario. "
        "Le scénario reste consultable, modifiable et exportable."
    ),
    "val_skeleton_mismatch_reference_none": (
        "La structure du scénario ne correspond pas au mode de génération : le mode actuel est {route}, "
        "qui requiert la structure {expected} ({expected_noun}), mais ce scénario ne comporte aucun tableau de structure. "
        "Appelez generate_script_plan pour découper à nouveau cet épisode, puis régénérez le scénario. "
        "Le scénario reste consultable, modifiable et exportable."
    ),
    "val_skeleton_mismatch_storyboard_known": (
        "La structure du scénario ne correspond pas au mode de génération : le mode actuel est {route}, "
        "qui requiert la structure {expected} ({expected_noun}), mais ce scénario utilise {actual} ({actual_noun}). "
        "Relancez le découpage (script_plan) pour cet épisode, puis régénérez le scénario. "
        "Le scénario reste consultable, modifiable et exportable."
    ),
    "val_skeleton_mismatch_storyboard_none": (
        "La structure du scénario ne correspond pas au mode de génération : le mode actuel est {route}, "
        "qui requiert la structure {expected} ({expected_noun}), mais ce scénario ne comporte aucun tableau de structure. "
        "Relancez le découpage (script_plan) pour cet épisode, puis régénérez le scénario. "
        "Le scénario reste consultable, modifiable et exportable."
    ),
    # ---- reference-video duration consolidation migration ----
    "val_unit_duration_clamped": (
        "La durée de l'unité {unit_id} ({target}s) est hors de la plage raisonnable {low}-{high}s ; ramenée à {clamped}s"
    ),
    "val_unit_duration_slotted": (
        "La durée de l'unité {unit_id} ({duration}s) ne correspond à aucune option du modèle ({durations}) ; "
        "ajustée au palier {slot}s"
    ),
    # ---- archive repair and import/export diagnostics ----
    "arch_source_encoding_unconverted": (
        "L'encodage du fichier source n'a pas pu être détecté et n'a pas été converti en UTF-8 : source/{name} "
        "(la planification d'épisodes ne pourra pas lire ce fichier)"
    ),
    "arch_provider_asset_links_not_restored": (
        "Le projet a été importé, mais {count} liaisons de bibliothèque de ressources n'ont pas pu être enregistrées ; "
        "la génération enverra ces images comme contenu brut. Téléversez-les à nouveau si nécessaire"
    ),
    "arch_non_standard_entry_excluded": "Le fichier ou dossier non standard de premier niveau '{entry}' a été exclu de l'export",
    "arch_invalid_project_json": "Impossible d'analyser {file} : {path}",
    "arch_version_history_malformed": "{location} : l'historique des versions n'est pas au format attendu",
    "arch_version_snapshot_path_unmanaged": "{location} : le chemin de capture d'une version est en dehors du répertoire de son type de ressource",
    "arch_script_file_repaired": "{location} : réparé automatiquement vers {path}",
    "arch_missing_script_file_pending": "{location} : scénario pas encore généré : {path}",
    "arch_missing_script_file": "{location} : le fichier référencé n'existe pas : {path}",
    "arch_invalid_script_json": "Impossible d'analyser le fichier de scénario : {path}",
    "arch_deprecated_source_file_removed": "Le champ novel.source_file est obsolète et a été supprimé",
    "arch_deprecated_field_removed": "Le champ {field} est obsolète (calculé à la lecture) et a été supprimé",
    "arch_deprecated_clue_field_removed": (
        "{items_key}[{index}] : le champ obsolète {field} a été supprimé (utilisez scenes/props à la place)"
    ),
    "arch_missing_field_filled": "{items_key}[{index}] : champ manquant renseigné : {field}",
    "arch_unit_unresolved_mentions": (
        "video_units[{index}] : le corps mentionne des noms de ressources absents de project.json : {names} ; "
        "ils ne produiront pas d'images de référence"
    ),
    "arch_generated_assets_defaults": "{label}[{index}].generated_assets : champs par défaut renseignés {fields}",
    "arch_missing_generated_assets": "{label}[{index}] : champ manquant renseigné generated_assets",
    "arch_invalid_generated_assets": (
        "{label}[{index}] : generated_assets est malformé ({actual}) et a été réinitialisé à la structure par défaut"
    ),
    "arch_placeholder_character_added": "Ajout automatique de la définition de personnage manquante : {name}",
    "arch_placeholder_asset_added": "Ajout automatique de la définition {asset_type} manquante : {name}",
    "arch_canonical_path_normalized": "{location} : normalisé vers {path}",
    "arch_current_asset_materialized": "{location} : fichier actuel {target} restauré depuis {source}",
    "arch_current_asset_restored_from_version": "{location} : fichier actuel {target} restauré depuis {source}",
    # ---- archive import errors ----
    "arch_invalid_conflict_policy": "Politique de conflit invalide",
    "arch_conflict_policy_unsupported": "conflict_policy ne supporte que prompt, rename ou overwrite ; obtenu : {value}",
    "arch_import_validation_failed": "Échec de validation du paquet d'importation",
    "arch_artifact_activation_failed": "L'état des artefacts du projet importé est incohérent : {reason}",
    "arch_project_migration_failed": "Les données du projet dans l'archive ne peuvent pas être mises à niveau vers la version actuelle : {reason}",
    "arch_import_confirmation_required": "La mise à niveau de l'archive a modifié certains contenus. Confirmez avant d'importer",
    "arch_not_a_zip": "Le fichier téléversé n'est pas une archive ZIP valide",
    "arch_zip_encrypted_entry": "Le ZIP contient une entrée chiffrée et ne peut pas être importé : {name}",
    "arch_zip_absolute_path_entry": "Le ZIP contient une entrée avec chemin absolu : {name}",
    "arch_zip_traversal_entry": "Le ZIP contient une entrée d'échappement de chemin : {name}",
    "arch_zip_symlink_entry": "Le ZIP contient un lien symbolique : {name}",
    "arch_zip_unparsable_member": "Impossible d'analyser {label} : {path}",
    "arch_multiple_manifests": (
        "Le ZIP contient plusieurs fichiers arcreel-export.json ; la racine du projet ne peut pas être déterminée"
    ),
    "arch_manifest_missing_project_json": "Le paquet d'export officiel ne contient pas project.json",
    "arch_no_project_json": "Aucun fichier project.json trouvé dans le ZIP",
    "arch_multiple_project_json": "Le ZIP contient plusieurs fichiers project.json ; la racine du projet ne peut pas être déterminée",
    "arch_extract_path_traversal": "Le chemin d'extraction sort du répertoire cible : {path}",
    "arch_conflict_detected": "Conflit d'identifiant de projet détecté",
    "arch_project_name_conflict": (
        "L'identifiant de projet '{name}' existe déjà. Choisissez d'écraser le projet existant ou d'importer sous un nouveau nom."
    ),
    # ---- Custom endpoint definition validation ----
    "val_ce_missing_field": "Champ obligatoire manquant : {field}",
    "val_ce_unknown_field": "Champ inconnu : {field}",
    "val_ce_removed_field": "Champ retiré du format : {field} - {reason}",
    "val_ce_invalid_type": "Type incorrect ; attendu {expected}",
    "val_ce_invalid_enum_value": "Valeur non autorisée ici ; autorisées : {allowed}",
    "val_ce_invalid_value": "La valeur ne correspond pas au format : {detail}",
    "val_ce_schema_violation": "Ne correspond pas au format de définition : {detail}",
    "val_ce_schema_minimum_constraint": "Minimum autorisé : {limit}",
    "val_ce_schema_maximum_constraint": "Maximum autorisé : {limit}",
    "val_ce_schema_format_constraint": "Format requis non respecté : {constraint}",
    "val_ce_schema_forbidden_constraint": "La valeur correspond à une contrainte interdite",
    "val_ce_schema_generic_constraint": "Contrainte de définition non satisfaite ({keyword})",
    "val_ce_removed_reason_request_query": (
        "les paramètres de requête statiques et dynamiques doivent figurer dans le modèle d'url, et l'authentification dans auth.query"
    ),
    "val_ce_removed_reason_status_codes": (
        "la gestion des codes HTTP relève du comportement d'exécution : 2xx réussit, 429 et 5xx réessayent, le reste échoue"
    ),
    "val_ce_removed_reason_polling_policy": "l'intervalle d'interrogation et le délai d'expiration relèvent de la politique d'exécution, pas de la définition",
    "val_ce_removed_reason_extract_source": "l'extraction commence toujours au corps de la réponse ; le code HTTP n'est pas un chemin",
    "val_ce_removed_reason_extract_usage_keys": "la consommation se configure désormais sous poll.extract.usage",
    "val_ce_removed_reason_mime_types": "les formats de ressources ne sont pas sur liste blanche ; le fournisseur rejette ce qu'il ne prend pas en charge",
    "val_ce_removed_reason_comfyui_capabilities": (
        "un point de terminaison ComfyUI déduit ses capacités des liaisons de nœuds, aucune déclaration n'est requise dans la définition"
    ),
    "val_ce_malformed_placeholder": (
        "{fragment} n'est pas un espace réservé valide : seules les variables simples sont supportées "
        "(comme prompt ou inputs.first_frame) — pas de filtres, d'index ou d'expressions, "
        "et chaque accolade ouvrante doit être fermée"
    ),
    "val_ce_undeclared_variable": "L'espace réservé {name} fait référence à une variable non déclarée",
    "val_ce_api_key_outside_auth": (
        "api_key ne peut apparaître que dans la section auth : les identifiants restent hors du corps et de l'URL, "
        "et hors des définitions que vous partagez"
    ),
    "val_ce_auth_without_api_key": (
        "La section auth n'est pas vide mais ne référence jamais api_key : laissez-la vide pour une API sans identifiant, "
        "sinon utilisez la clé"
    ),
    "val_ce_auth_header_conflict": (
        "{header} entre en conflit avec auth.headers (insensible à la casse) : seule la section auth peut définir les en-têtes d'authentification"
    ),
    "val_ce_header_name_duplicate": (
        "{header} ne diffère de {first} dans la même table que par la casse : les noms d'en-tête HTTP sont insensibles à la casse"
    ),
    "val_ce_auth_query_conflict": (
        "L'URL contient déjà le paramètre de requête {param} déclaré dans auth.query : "
        "seule la section auth peut écrire les paramètres d'authentification"
    ),
    "val_ce_auth_query_reserved": "L'entrée auth.query {param} entre en conflit avec un paramètre du téléchargement d'artefact ; choisissez un autre nom",
    "val_ce_task_id_out_of_scope": "task_id est uniquement disponible dans les sections poll et result",
    "val_ce_result_id_out_of_scope": "result_id est uniquement disponible dans la section result",
    "val_ce_result_id_without_extract": "result_id est référencé mais poll.extract ne déclare pas result_id",
    "val_ce_input_out_of_scope": (
        "La ressource {name} ne peut être référencée que depuis submit : les requêtes poll et result ne transportent pas de ressources"
    ),
    "val_ce_list_input_requires_each": "{name} est une ressource de type liste ; déployez-la avec $each au lieu de l'interpoler",
    "val_ce_each_in_not_list_input": "$each.in pointe vers {name}, qui n'est pas une ressource de liste déclarée",
    "val_ce_each_shape_invalid": (
        "$each prend soit item pour étaler les éléments d'un tableau, soit key et value pour étaler les entrées d'un objet ; "
        "les deux formes ne peuvent pas être mélangées"
    ),
    "val_ce_each_position_mismatch": (
        "La forme de $each ne correspond pas à sa position : utilisez item dans un tableau et key avec value dans un objet"
    ),
    "val_ce_each_alias_reserved": (
        "{name} est une variable réservée dans le corps de la boucle et ne peut pas servir d'alias d'élément pour $each"
    ),
    "val_ce_when_unknown_input": "$when pointe vers {name}, qui n'est pas une ressource déclarée",
    "val_ce_input_not_referenced": (
        "La ressource est déclarée mais jamais référencée dans submit : elle n'est jamais envoyée et ne peut pas justifier une capacité"
    ),
    "val_ce_enum_map_variable_not_allowed": "{variable} ne peut pas être mise en correspondance ; variables autorisées : {allowed}",
    "val_ce_default_variable_not_allowed": "{variable} ne peut pas avoir de valeur par défaut ; variables autorisées : {allowed}",
    "val_ce_default_value_type_invalid": "La valeur par défaut pour {variable} doit être de type {expected}",
    "val_ce_default_value_not_in_enum_map": "La valeur par défaut {value} pour {variable} n'est pas dans enum_maps ; valeurs possibles : {allowed}",
    "val_ce_status_map_target_invalid": "Le statut {target} est hors de {allowed} ; mappez l'expiration sur failed",
    "val_ce_capability_declared_without_input": (
        "{capability} est déclarée mais submit ne référence aucune ressource {source}"
    ),
    "val_ce_capability_input_without_declaration": (
        "submit référence une ressource {source} sans déclarer {capability}, la ressource serait envoyée alors que l'interface masque la capacité"
    ),
    "val_ce_capability_incoherent": "La capacité {capability} entre en conflit avec son groupe ; requis : {requirement}",
    "val_ce_capability_not_declared": "Déclarez au moins une capacité comme true dans capabilities : {allowed}",
    "val_ce_media_type_field_not_allowed": "{name} n'est pas disponible pour une définition dont le type de média est {media_type}",
    "val_ce_artifact_extract_missing": "Aucun chemin d'extraction d'artefact ; indiquez au moins l'une des clés : {keys}",
    "val_ce_jsonpath_not_a_string": "Un chemin d'extraction doit être une chaîne : {path_expression}",
    "val_ce_jsonpath_surrounding_whitespace": "Un chemin d'extraction ne doit pas contenir d'espaces au début ou à la fin : {path_expression}",
    "val_ce_jsonpath_missing_root": "Un chemin d'extraction doit commencer par $ : {path_expression}",
    "val_ce_jsonpath_recursive_descent": (
        "La descente récursive n'est pas autorisée dans les chemins d'extraction (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_union": (
        "Les sélecteurs d'union ne sont pas autorisés dans les chemins d'extraction (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_slice_step": (
        "Les pas de découpage ne sont pas autorisés dans les chemins d'extraction (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_function_extension": (
        "Les extensions de fonction ne sont pas autorisées dans les chemins d'extraction (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_filter_root_reference": (
        "Un filtre ne peut pas faire référence au nœud racine (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_filter_non_singular": (
        "Un filtre ne peut utiliser que des requêtes singulières (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_regex_operator": (
        "L'opérateur regex n'est pas autorisé dans les chemins d'extraction (au caractère {position}) : {path_expression}"
    ),
    "val_ce_jsonpath_syntax": "Erreur de syntaxe dans le chemin d'extraction (au caractère {position}) : {path_expression}",
    "val_ce_jsonpath_evaluation_failed": "Impossible d'évaluer le chemin d'extraction : {path_expression}",
    "val_ce_template_render_failed": "Impossible de restituer le modèle de requête : {detail}",
    "val_ce_auth_literal_credential": (
        "Cette valeur semble contenir une véritable clé secrète : référencez l'identifiant avec l'espace réservé api_key "
        "pour éviter qu'elle soit exposée lors du partage de la définition"
    ),
    "val_ce_template_url_not_string": "Le modèle d'URL doit produire une chaîne de caractères",
    "val_ce_unknown_asset_encoding": "Encodage de ressource inconnu : {encoding}",
    "val_ce_enum_map_value_missing": "enum_maps.{name} n'a pas d'entrée pour '{value}'",
    "val_ce_template_text_variable_null": "La variable {name} est nulle et ne peut pas être insérée dans le texte",
    "val_ce_each_value_not_list": "$each.in pointe vers {name}, dont la valeur n'est pas une liste",
    "val_ce_each_key_duplicate": "La forme objet $each a produit la clé {field}, déjà utilisée dans le même objet",
    # ---- ComfyUI endpoint: node bindings and import routing ----
    "val_ce_comfyui_binding_required": (
        "{binding_key} doit être relié à un nœud avant que ce point de terminaison puisse être enregistré : "
        "le prompt définit ce qui est dessiné, et la sortie détermine le fichier récupéré"
    ),
    "val_ce_comfyui_binding_key_not_allowed": (
        "Un point de terminaison {media_type} ne possède pas de liaison {binding_key} ; clés valides : {allowed}"
    ),
    "val_ce_comfyui_node_not_found": (
        "Le workflow ne possède pas de nœud {node} : les identifiants de nœuds changent lors de l'édition du workflow, "
        "veuillez réimporter et confirmer les liaisons"
    ),
    "val_ce_comfyui_input_not_found": "Le nœud {node} n'a pas d'entrée nommée {input}",
    "val_ce_comfyui_input_is_link": (
        "L'entrée {input} du nœud {node} est reliée à un nœud amont et serait écrasée à l'exécution ; "
        "liez un champ littéral à la place"
    ),
    "val_ce_comfyui_target_collision": (
        "L'entrée {input} du nœud {node} est déjà la cible de {owner}, {binding_key} ne peut donc pas écrire dans le même champ"
    ),
    "val_ce_comfyui_class_type_mismatch": (
        "L'entrée enregistrait le nœud {node} comme {class_type}, mais le workflow contient désormais {actual} ; "
        "réimportez et confirmez les liaisons"
    ),
    "val_ce_comfyui_consumer_not_fed": (
        "Le flux provenant du nœud de référence {node} n'atteint jamais l'entrée {input} du nœud {consumer}"
    ),
    "val_ce_comfyui_fps_conflict": (
        "La fréquence d'images provient de plusieurs sources conflictuelles ({values}) ; ne conservez qu'une seule valeur"
    ),
    "val_ce_comfyui_ui_format_workflow": (
        "Il s'agit d'un workflow ComfyUI au format UI qui ne peut pas être soumis ; exportez-le avec Export (API) dans ComfyUI"
    ),
    # ---- ComfyUI endpoint: node binding inference signals and hints ----
    "val_ce_infer_manual_binding": "Liaison de nœud enregistrée ; la cible déjà confirmée par l'utilisateur est conservée",
    "val_ce_infer_title_marker": "Le titre du nœud porte un marqueur ARCREEL:",
    "val_ce_infer_external_node_family": "Un nœud de paramètre {family} déclarant le paramètre {parameter}",
    "val_ce_infer_sampler_port_trace": "Remonté depuis le port de conditionnement {port} du nœud {node}",
    "val_ce_infer_alias_with_class_type": "{class_type} porte couramment cette sémantique",
    "val_ce_infer_alias_only": "Le nom d'entrée {input} est courant pour cette sémantique",
    "val_ce_infer_link_trace": "Sa sortie alimente l'entrée {input} du nœud {consumer}",
    "val_ce_infer_class_type_tier": "{class_type} est le vecteur le plus fiable parmi les candidats",
    "val_ce_infer_output_chain": "Se situe sur la chaîne produisant le résultat final",
    "val_ce_infer_title_polarity": "Le titre du nœud « {title} » indique cette polarité",
    "val_ce_infer_note_reference_consumer_unknown": (
        "Les images de référence alimentent l'entrée {input} du nœud {node} ({class_type}) ; "
        "la dernière image est répétée pour combler les emplacements restants"
    ),
    "val_ce_infer_note_batch_size_above_one": (
        "L'entrée {input} du nœud {node} ({class_type}) vaut {value}, donc une soumission génère plusieurs images ; "
        "ArcReel ne modifie pas cette valeur"
    ),
    "val_ce_infer_note_manual_only_node": (
        "Le nœud {node} est un {class_type} ; les liaisons {binding_keys} qu'il porte ne peuvent pas être déduites, liez-les manuellement"
    ),
    "val_ce_infer_note_computed_source": (
        "Le candidat {binding_key} arrive sur l'entrée {input} du nœud {node}, mais sa valeur est calculée en amont ; définissez-la manuellement"
    ),
    "val_ce_infer_note_rematched": "Les entrées {binding_key} ont été réassociées au nœud {nodes}",
    "val_ce_infer_note_binding_lost": (
        "Les entrées {binding_key} n'ont aucune cible dans le nouveau workflow (précédemment nœud {nodes}) ; "
        "l'inférence a été réexécutée, veuillez confirmer"
    ),
    "val_ce_infer_note_target_taken": (
        "Le candidat {binding_key} cible l'entrée {input} du nœud {node}, sur laquelle {others} écrit également ; "
        "il a été retiré des candidats {binding_key}"
    ),
    "val_ce_poll_without_task_id": "La requête d'interrogation ne fait jamais référence à task_id ; confirmez que cela est intentionnel",
    "val_ce_jsonpath_wildcard_order": (
        "{path_expression} utilise un joker : seul le premier élément est retenu"
    ),
    # ---- market source checks ----
    "val_market_index_unreadable": "Impossible de lire le fichier d'index : {detail}",
    "val_market_unsupported_schema_version": "schema_version {version} de l'index est plus récente que la version supportée {supported}",
    "val_market_missing_field": "Champ obligatoire manquant : {field}",
    "val_market_invalid_type": "Type incorrect ; attendu {expected}",
    "val_market_invalid_value": "La valeur viole la contrainte {keyword} : {constraint}",
    "val_market_slug_invalid": (
        'Identifiant slug invalide "{value}" : utilisez des lettres minuscules, chiffres et tirets, '
        "débutez par une lettre ou un chiffre, 64 caractères maximum"
    ),
    "val_market_slug_duplicate": 'Le slug "{slug}" est utilisé plusieurs fois dans cette source de marché',
    "val_market_slug_directory_mismatch": 'Le slug "{slug}" ne correspond pas au répertoire de définition "{directory}"',
    "val_market_path_not_relative": (
        '"{value}" doit être un chemin relatif à la source de marché : '
        "pas de / initial, pas de .., et ne doit pas pointer hors de la source"
    ),
    "val_market_file_missing": "Le fichier référencé n'existe pas : {value}",
    "val_market_symlink_not_allowed": (
        '"{value}" est un lien symbolique non supporté : utilisez un fichier ou répertoire standard'
    ),
    "val_market_icon_format_invalid": "L'icône doit être un fichier PNG, WebP ou SVG lisible dont l'extension correspond au contenu",
    "val_market_icon_too_large": "L'icône pèse {size} octets, dépassant la limite de {limit} octets",
    "val_market_icon_not_square": "L'icône doit être carrée ; dimensions actuelles : {width}×{height}",
    "val_market_icon_ambiguous": "Un répertoire d'entrée ne doit contenir qu'un seul fichier d'icône ; trouvés : {icons}",
    "val_market_definition_unreadable": "Impossible de lire la définition : {detail}",
    "val_market_definition_invalid": "La définition a échoué à la validation ({code}) : {detail}",
    "val_market_projection_mismatch": (
        'Le champ d\'index {field} vaut "{index_value}", différent de "{definition_value}" dans les métadonnées'
    ),
    "val_market_min_app_version_invalid": 'min_app_version "{value}" n\'est pas au format semver (x.y.z)',
    "val_market_detail_meta_not_object": "La définition ne contient pas d'objet meta",
    "val_market_cli_check_passed": "Vérification de la source de marché réussie : {directory}",
    "val_market_cli_check_failed": "Vérification de la source de marché échouée avec {count} problème(s)",
    "val_market_cli_generate_written": "{path} écrit ({count} entrées)",
    "val_market_cli_generate_failed": "Impossible de générer l'index : {count} problème(s)",
    # Draft diagnostics
    "draft_violation_source_text_empty": "{label} : source_text est vide. Copiez le passage original utilisé par cette unité vidéo.",
    "draft_violation_source_text_not_verbatim": "{label} : source_text n'est pas un passage verbatim : {excerpt}. Copiez l'original sans réécrire ni traduire.",
    "draft_violation_fullwidth_braces": "{label} : accolades pleine chasse dans {excerpt}. Utilisez des accolades ASCII pour le dialogue et la voix off.",
    "draft_violation_malformed_mention": "{label} : référence de ressource incorrecte {excerpt}. Utilisez `@[nom de ressource]` avec crochets fermés.",
    "draft_violation_dialogue_line_syntax": "{label} : syntaxe de dialogue invalide dans {excerpt}. Utilisez une référence de locuteur suivie du dialogue entre accolades ASCII.",
    "draft_violation_unclosed_brace": "{label} : accolade non fermée dans {excerpt}. Fermez chaque paire d'accolades ASCII.",
    "draft_violation_braces_in_description": "{label} : accolades dans la description visuelle {excerpt}. Les accolades sont réservées aux dialogues et voix off.",
    "draft_violation_empty_text": "{label} : le texte est vide. Ajoutez une description visuelle et les dialogues requis.",
    "draft_violation_blank_description": "{label} : description visuelle manquante. Les dialogues et la voix off seuls ne suffisent pas à composer une scène visuelle.",
    "draft_violation_unregistered_asset": "{label} : {field} référence des ressources non enregistrées : {names}. Utilisez des noms enregistrés ou ajoutez-les dans new_assets.",
    "draft_violation_unregistered_speaker": "{label} : les locuteurs ne sont pas des personnages enregistrés : {names}. Les locuteurs sélectionnent l'audio de référence et doivent être enregistrés.",
    "draft_violation_unregistered_speaker_derivative": "{label} : variantes de locuteur non enregistrées : {names}. Enregistrez la variante ou utilisez le personnage de base.",
    "draft_violation_refs_over_limit": "{label} : {count} images de référence dépassent la limite de {limit}. Décrivez les personnages secondaires sans référence `@`.",
    "draft_violation_speakers_over_limit": "{label} : {count} locuteurs dépassent la limite audio du modèle de {limit}. Découpez les plans par personnage.",
    "draft_violation_dialogue_overload": "{label} : le dialogue nécessite environ {spoken}s, dépassant {duration}s (tolérance {tolerance}, plafond {budget}s). Rallongez le plan ou raccourcissez le dialogue.",
    "draft_violation_dialogue_line_count_changed": "{label} : le nombre de lignes de dialogue a changé de {before} à {after}. La rédaction de prompt doit conserver le dialogue à l'identique.",
    "draft_violation_dialogue_rewritten": "{label} : le dialogue {index} a été réécrit ({before} → {after}). La rédaction de prompt doit conserver le texte verbatim.",
    "draft_violation_duration_off_tier": "{label} : la durée de {duration}s est hors des paliers supportés {tiers}. Choisissez une durée supportée.",
    "draft_violation_invalid_segment_id": "{label} : segment_id doit utiliser le format E{episode}S## et correspondre au numéro d'épisode.",
    "draft_violation_duplicate_segment_id": "Valeurs de segment_id en double : {ids}. Chaque identifiant de plan doit être unique dans l'épisode.",
    "draft_violation_blank_novel_text": "{label} : novel_text est vide. Chaque plan doit contenir la narration copiée mot à mot de l'original.",
    "draft_violation_novel_text_coverage": "Le texte novel_text ne couvre pas l'original mot à mot, intégralement et dans l'ordre. Source : {source}.",
    "draft_violation_schema_invalid": "Le brouillon {path} ne correspond pas à la structure attendue : {detail}.",
    # Draft schema reasons
    "draft_schema_missing": "champ obligatoire manquant",
    "draft_schema_extra_forbidden": "ce champ n'est pas supporté",
    "draft_schema_literal_error": "doit être l'un de : {expected}",
    "draft_schema_less_than_equal": "doit être au maximum {le}",
    "draft_schema_greater_than_equal": "doit être au minimum {ge}",
    "draft_schema_less_than": "doit être inférieur à {lt}",
    "draft_schema_greater_than": "doit être supérieur à {gt}",
    "draft_schema_string_too_short": "longueur minimale : {min_length}",
    "draft_schema_string_too_long": "longueur maximale : {max_length}",
    "draft_schema_too_short": "nombre minimum d'éléments : {min_length}",
    "draft_schema_too_long": "nombre maximum d'éléments : {max_length}",
    "draft_schema_string_pattern_mismatch": "doit correspondre au motif {pattern}",
    "draft_schema_string_type": "doit être une chaîne de caractères",
    "draft_schema_int_type": "doit être un entier",
    "draft_schema_int_parsing": "doit être un entier",
    "draft_schema_int_from_float": "doit être un entier",
    "draft_schema_bool_type": "doit être un booléen",
    "draft_schema_bool_parsing": "doit être un booléen",
    "draft_schema_list_type": "doit être un tableau",
    "draft_schema_model_type": "doit être un objet",
    "draft_schema_dict_type": "doit être un objet",
    "draft_schema_non_empty_list": "doit être un tableau non vide",
    "draft_schema_prompt_authoring_unreadable": "impossible de lire le résultat de rédaction de prompt",
    "draft_schema_with_value": "{reason} (valeur actuelle : {value})",
    "draft_schema_choice_separator": ", ",
    "draft_violation_formal_revision_conflict": "Le contenu officiel a changé pendant la génération. Le résultat est enregistré comme brouillon. Fusionnez le contenu avant promotion.",
    "draft_violation_draft_revision_conflict": "Un brouillon est en attente ou a changé. Promeuvez, ignorez ou fusionnez le brouillon existant avant de réessayer.",
    "draft_violation_unit_count_changed": "La rédaction de prompt a produit {actual} unités vidéo ; attendu {expected}. Ne modifiez pas le nombre d'unités à cette étape.",
    "draft_violation_formal_revision_missing": "Le brouillon n'a pas de référence de scénario officiel et ne peut pas être promu en toute sécurité. Générez un nouveau brouillon.",
    "draft_violation_new_asset_invalid": "{label} : structure invalide. Vérifiez le tableau, les champs obligatoires et la décision.",
    "draft_violation_new_asset_name_invalid": "{label} : nom de {field} invalide : {name}. Utilisez un nom de ressource valide.",
    "draft_violation_new_asset_name_taken": "{label} : le nom {name} entre en conflit avec {existing} ({asset_type}). Choisissez un autre nom.",
    "draft_violation_new_asset_derivative_not_character": "{label} : seuls les personnages peuvent avoir des variantes.",
    "draft_violation_new_asset_merge_cycle": "{label} : cycle de fusion : {chain}. Corrigez la cible ou utilisez register / skip.",
    "draft_violation_new_asset_target_unresolved": "{label} : la cible {target} n'est pas une ressource enregistrée du même type ({asset_type}).",
    "draft_violation_new_asset_base_unresolved": "{label} : la base {target} n'est pas un personnage enregistré.",
    "draft_violation_mixed_speech": "{label} ({location}) : Les dialogues et la voix off ne peuvent pas être mélangés. Découpez l'unité vidéo.",
    "draft_violation_needs_replan": "{label} ({location}) : La combinaison vocale nécessite une replanification. Découpez l'unité vidéo.",
    "draft_violation_parse_failed": "{label} ({location}) : La voix n'a pas pu être analysée. Corrigez le format d'entrée.",
    "draft_violation_empty_speaker": "{label} ({location}) : Le dialogue n'a pas de locuteur. Attribuez un personnage.",
}

