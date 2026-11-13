import type enOnboarding from '../en/onboarding';

export default {
  // Étapes de la visite guidée
  'welcome_title': 'Bienvenue sur [[brand]]',
  'welcome_body': '[[brand]] transforme un roman ou un scénario en vidéos courtes. La production est prise en charge par l\'Agent, et chaque étape peut être affinée à la main. Cette visite présente l\'interface principale et le flux de production.',
  'lobby_create_title': 'Créer un projet',
  'lobby_create_body': 'Créez un projet ici, puis définissez ses informations clés, ses paramètres de génération et son style visuel. Pour ouvrir un projet exporté précédemment, choisissez « Importer un ZIP » dans le menu déroulant à droite.',
  'lobby_settings_title': 'Paramètres',
  'lobby_settings_body': 'Deux éléments doivent être configurés avant de lancer la production. Un point rouge sur le bouton indique que des champs requis sont encore vacants.',
  'settings_providers_title': 'Configurer les fournisseurs',
  'settings_providers_body': 'Les modèles de texte, d\'image, de vidéo et de voix proviennent de ces fournisseurs. Configurez au moins un fournisseur : saisissez votre clé d\'API, puis cliquez sur « Tester » pour valider la connexion.',
  'settings_agent_title': 'Configurer l\'Agent [[brand]]',
  'settings_agent_body': 'L\'Agent [[brand]] peut réaliser l\'ensemble des tâches de production. Ajoutez ici un fournisseur pour l\'Agent et saisissez sa clé d\'API.',
  'lobby_demo_title': 'Projet de démonstration',
  'lobby_demo_body': 'Cliquez sur la carte pour ouvrir le projet de démonstration et explorer l\'interface de travail.',
  'workbench_overview_title': 'Vue d\'ensemble du projet',
  'workbench_overview_body': 'Voici le synopsis, le genre, le thème et l\'univers extraits automatiquement du texte source, modifiables directement. Vous retrouvez en dessous l\'avancement des images et les coûts ; l\'état de chaque épisode est consultable dans la barre latérale.',
  'workbench_agent_title': 'Agent',
  'workbench_agent_body': 'Le panneau de l\'Agent se trouve à droite. Confiez-lui vos tâches dans le fil de discussion : il les exécute et vous rend compte de sa progression. Le bouton « Agent » en haut permet de replier ou déployer ce volet.',
  'workbench_lorebook_title': 'Personnages, décors et accessoires',
  'workbench_lorebook_body': 'Les personnages, décors et accessoires sont gérés dans le menu latéral. Ouvrez une fiche pour ajuster sa description ou générer une image de référence. Ces visuels garantissent la continuité graphique lors du storyboarding et de la création vidéo.',
  'workbench_timeline_title': 'Plans',
  'workbench_timeline_body': 'Chaque épisode propose trois vues : Plan de script, Plans, et Montage. Dans la vue Plans, chaque séquence dispose d\'un prompt, d\'une image de storyboard et d\'une vidéo : validez d\'abord l\'image de storyboard avant de générer la vidéo finale.',
  'workbench_export_title': 'Exporter le projet',
  'workbench_export_body': 'Utilisez « Exporter le projet » dans la barre supérieure pour télécharger l\'intégralité du projet au format ZIP. Le montage final et les brouillons Jianying s\'exportent depuis l\'onglet Montage de chaque épisode. Le projet démo ne peut pas être exporté.',
  'finish_title': 'Lancez votre premier projet',
  'finish_body': 'Créez un projet, téléversez un roman ou un scénario, et laissez l\'Agent piloter la création. Vous pouvez rejouer cette visite guidée à tout moment dans Paramètres → Général.',

  // Contrôles de la visite
  'next': 'Suivant',
  'prev': 'Précédent',
  'done': 'Terminé',
  'skip': 'Passer',
  'close': 'Fermer la visite',
  'progress': 'Étape {{current}} sur {{total}}',

  // Section du projet de démonstration
  'demo_section_title': 'Exemple de projet',
  'demo_section_note': 'Visible uniquement pendant la visite guidée',
  'demo_project_title': 'Les Aventures d\'Alice au pays des merveilles',
  'demo_project_style': 'Illustration aquarelle de livre de contes',

  // Projet démo en lecture seule
  'demo_badge': 'Démo · Lecture seule',
  'demo_badge_hint': 'Vous consultez un projet de démonstration. L\'édition, la génération, le téléversement et l\'export sont désactivés.',
  'demo_action_unavailable': 'Indisponible dans la démo',
  'demo_episode_placeholder': 'La démonstration s\'arrête à l\'épisode {{position}} : celui-ci possède un titre mais aucun script ni plan.',

  // Conversation statique démo
  'demo_chat_user_start': 'Démarrer la production',
  'demo_chat_agent_progress': 'Les images de personnages et de décors sont prêtes. Je vais maintenant générer tour à tour les images de storyboard et les vidéos de chaque épisode et vous tenir informé de l\'avancement ici.',

  // Vue d'ensemble du projet démo
  'demo_overview_synopsis': 'Par une chaude après-midi, Alice s\'élance à la poursuite d\'un lapin en gilet muni d\'une montre à gousset et tombe dans un terrier où les règles de taille, de bienséance et de logique disparaissent. Elle grandit, rétrécit, croise la Chenille, le Chapelier et la Reine, avant de renverser le tribunal des cartes à jouer.',
  'demo_overview_genre': 'Conte · Aventure fantastique',
  'demo_overview_theme': 'L\'absurdité des conventions d\'adultes vue par une enfant curieuse',
  'demo_overview_world': 'Un bord de rivière victorien qui bascule vers le Pays des Merveilles : une grande salle aux portes scellées, une fête du thé sans fin, et une cour de cartes tyrannique. Rendu d\'aquarelle sur papier à grain marqué et contours délicats.',

  // Titres des épisodes démo
  'demo_episode_1_title': 'Au fond du terrier du lapin',
  'demo_episode_2_title': 'La mare de larmes',
  'demo_episode_3_title': 'Les conseils de la Chenille',
  'demo_episode_4_title': 'La cuisine de la Duchesse',
  'demo_episode_5_title': 'Un thé de fous',
  'demo_episode_6_title': 'La partie de croquet de la Reine',
  'demo_episode_7_title': 'L\'histoire de la Fausse-Tortue',
  'demo_episode_8_title': 'Qui a volé les tartes ?',

  // Personnages démo
  'demo_character_1_name': 'Alice',
  'demo_character_1_desc': 'Petite fille anglaise de sept ans vêtue d\'une robe bleu ciel et d\'un tablier blanc, cheveux blonds retenus par un ruban noir. Plus curieuse que craintive, elle refuse l\'absurde avant de poursuivre son chemin avec détermination.',
  'demo_character_1_voice': 'Voix enfantine vive et limpide, débit alerte, teinte de curiosité',
  'demo_character_2_name': 'Le Lapin Blanc',
  'demo_character_2_desc': 'Lapin blanc en gilet à carreaux, tenant une montre à gousset d\'une patte et des gants de l\'autre, perpétuellement pressé. Oreilles dressées par l\'inquiétude, s\'exprimant d\'un souffle précipité.',
  'demo_character_2_voice': 'Voix aiguë et essoufflée, murmures hâtifs',
  'demo_character_3_name': 'Le Chat du Cheshire',
  'demo_character_3_desc': 'Grand chat tigré gris et mauve arborant un sourire fendu jusqu\'aux oreilles. Il disparaît par bribes jusqu\'à ne laisser flotter que son large sourire.',
  'demo_character_3_voice': 'Voix grave, posée et enjôleuse, teintée d\'ironie',
  'demo_character_4_name': 'La Reine de Cœur',
  'demo_character_4_desc': 'Souveraine colérique en robe rouge et noire ornée de cœurs, sceptre au poing. Sa sentence favorite est invariable : « Qu\'on lui coupe la tête ! »',
  'demo_character_4_voice': 'Voix forte, impatiente et tranchante ; chaque phrase est un ordre',

  // Décors démo
  'demo_scene_1_name': 'Le bord de la rivière',
  'demo_scene_1_desc': 'Berge herbeuse sous les saules lors d\'un chaud après-midi d\'été. L\'eau coule lentement ; à côté gît un livre sans images ni dialogues.',
  'demo_scene_2_name': 'La salle des portes',
  'demo_scene_2_desc': 'Salle souterraine basse flanquée de portes fermées à clé. Au centre trône une petite table de verre à trois pieds portant une minuscule clé d\'or.',
  'demo_scene_3_name': 'Le jardin du thé fou',
  'demo_scene_3_desc': 'Longue table dressée sous un grand arbre, couverte de tasses et de théières empilées. Toutes les horloges sont figées sur six heures.',

  // Accessoires démo
  'demo_prop_1_name': 'Montre à gousset du Lapin Blanc',
  'demo_prop_1_desc': 'Montre de poche en laiton au bout d\'une chaîne patinée. Ses aiguilles tournent plus vite que le temps réel.',
  'demo_prop_2_name': 'Flacon « BOIS-MOI »',
  'demo_prop_2_desc': 'Petite fiole en verre portant une étiquette en papier imprimée « BOIS-MOI ». Réduit quiconque la boit à dix pouces de hauteur.',
  'demo_prop_3_name': 'Maillet flamant rose',
  'demo_prop_3_desc': 'Flamant rose tenu sous le bras en guise de maillet de croquet. Son long cou se contorsionne au moment de frapper la balle.',

  // Plans démo — épisode 1
  'demo_shot_1_text': 'L\'après-midi était lourd et tiède. Alice commençait à s\'ennuyer sur la berge auprès de sa sœur et fermait doucement les yeux.',
  'demo_shot_1_image': 'Berge estivale sous les saules ; Alice en robe bleue et tablier blanc somnole sur l\'herbe auprès de sa sœur lisant un livre. Style aquarelle douce sur papier texturé.',
  'demo_shot_1_lighting': 'Contre-jour chaud de fin de journée, ombres tamisées par le feuillage',
  'demo_shot_1_ambiance': 'Torpeur estivale, calme, rêverie',
  'demo_shot_1_video': 'La caméra effectue un lent travelling le long de la berge ; le vent caresse les herbes et les paupières d\'Alice s\'alourdissent.',
  'demo_shot_1_audio': 'Clapotis de l\'eau, cigales lointaines, bruissement léger de page',
  'demo_shot_2_text': 'Soudain, un lapin blanc aux yeux roses passa en courant tout près d\'elle, tirant une montre de son gousset en soupirant : je vais être en retard !',
  'demo_shot_2_image': 'Le Lapin Blanc en gilet dressé sur ses pattes arrière traverse l\'herbe, une montre en laiton levée ; à l\'arrière-plan, Alice se redresse surprise. Style aquarelle.',
  'demo_shot_2_lighting': 'Plein jour radieux, lumière dorée sur la fourrure',
  'demo_shot_2_ambiance': 'Surprise soudaine, pointe comique, course effrénée',
  'demo_shot_2_video': 'La caméra suit le Lapin de profil : il consulte sa montre, presse le pas et s\'éloigne sous le regard intrigué d\'Alice.',
  'demo_shot_2_audio': 'Pas précipités dans l\'herbe, tic-tac rapide, soupir essoufflé du Lapin',
  'demo_shot_3_text': 'Alice bondit sur ses pieds et s\'élança à sa suite, juste à temps pour le voir plonger dans un large terrier sous la haie. Sans hésiter, elle s\'y engouffra.',
  'demo_shot_3_image': 'Terrier obscur au pied d\'une haie ; Alice à quatre pattes s\'y penche, la queue du Lapin disparaissant dans les profondeurs. Rendu aquarelle.',
  'demo_shot_3_lighting': 'Contraste saisissant entre l\'herbe baignée de soleil et l\'obscurité béante du terrier',
  'demo_shot_3_ambiance': 'Instant décisif où la curiosité l\'emporte sur la prudence',
  'demo_shot_3_video': 'Zoom avant vers l\'entrée du terrier ; Alice s\'incline pour y pénétrer alors que l\'image s\'enfonce dans la pénombre.',
  'demo_shot_3_audio': 'Craquements de brindilles, terre qui s\'effrite, écho feutré',
  'demo_shot_4_text': 'Le terrier descendait tout droit comme un puits infini. Alice tombait avec lenteur, observant au passage placards, cartes géographiques et étagères suspendues.',
  'demo_shot_4_image': 'Vue en coupe d\'un puits vertigineux ; Alice flotte en suspension dans sa robe déployée, entourée d\'armoires et d\'étagères de livres. Style aquarelle.',
  'demo_shot_4_lighting': 'Puits de lumière lointain au sommet, lueurs chaudes des lampes accrochées aux parois',
  'demo_shot_4_ambiance': 'Apesanteur onirique, temps suspendu',
  'demo_shot_4_video': 'La caméra descend au rythme de sa chute ; les meubles et étagères défilent doucement vers le haut.',
  'demo_shot_4_audio': 'Souffle d\'air dans le puits, bruissement d\'étoffe, tintement lointain',
  'demo_shot_5_text': 'Elle atterrit sans heurt dans une vaste salle entourée de portes verrouillées. Sur une table de verre reposait une petite clé d\'or qui n\'ouvrait qu\'une porte minuscule.',
  'demo_shot_5_image': 'Gros plan sur une table en verre à trois pieds soutenant une clé dorée et un petit flacon étiqueté ; au fond filtre la lumière d\'une porte basse. Rendu aquarelle.',
  'demo_shot_5_lighting': 'Rayon doré filtrant sous la porte, le reste de la pièce baignant dans une ombre douce',
  'demo_shot_5_ambiance': 'Silence pesant, mystère et espoir',
  'demo_shot_5_video': 'Plan fixe ; un éclat lumineux glisse sur la clé dorée tandis que quelques poussières dansent dans la lumière.',
  'demo_shot_5_audio': 'Écho de la salle vide, tintement cristallin de la clé sur le verre',
  'demo_shot_6_text': 'L\'étiquette du flacon indiquait « BOIS-MOI ». Alice en but une gorgée et sentit son corps rétrécir comme une longue-vue jusqu\'à ne plus mesurer que dix pouces.',
  'demo_shot_6_image': 'Alice portant le flacon à ses lèvres ; sa silhouette rapetisse, sa robe s\'amasse au sol tandis que la petite porte se retrouve désormais à sa hauteur. Rendu aquarelle.',
  'demo_shot_6_lighting': 'Lumière chaleureuse inondant la silhouette d\'Alice',
  'demo_shot_6_ambiance': 'Émerveillement et métamorphose magique',
  'demo_shot_6_video': 'Recul de la caméra à mesure qu\'Alice rétrécit, le point de vue glissant au ras du sol vers la porte illuminée.',
  'demo_shot_6_audio': 'Glouglou du liquide, froissement du tissu qui s\'abaisse, fiole posée sur le carreau',

  // Paramètres → Général
  'replay_title': 'Visite guidée de l\'application',
  'replay_desc': 'Rejouez la visite de premier démarrage pour revoir l\'interface et les flux clés.',
  'replay_action': 'Relancer la visite guidée',
} satisfies Record<keyof typeof enOnboarding, string> & Record<string, string>;

